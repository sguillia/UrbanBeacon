#include "urban.h"
#include <string.h>

void  activate_last_waypoint(void);
u8  create_waypoint(void);
u8 vacant_wp_id(void);

extern gps_coord_t  input_buffer[GPS_INPUT_BUFFER_SIZE];
extern u8           input_index;
extern u8           input_initialized;
extern u8           gps_fixed;
extern u8           wp_done;
extern u8           wp_num;
extern urban_t      wp_data;
extern u8           leds_busy;
extern u8           route_done;
extern u8           mode_prog;
extern float        max_dist;
extern gps_coord_t  last_pos;
extern u8           erase_trigger;
extern u8           erase_done;

static u16          ticks = 0;

/*
 * If wp_done : go to next waypoint
 * Else :
 *  If gps_fixed and input_initialized :
 *      If eeprom has free space:
 *          Save coordinates
 *      Else
 *          Error no free space // clignoter led rouge quelques fois
 * Else
 *      Cannot save no gps // ne rien faire
 */

void setup_t5(void)
{
    T5CONbits.TCKPS = 0b110;    //prescale 256
    TMR5 = 0;
    PR5 = 1250;                  //8Mhz / 2 / 256 ~*~ 1250 = 25hz
    IFS0bits.T5IF = 0;
    IPC5bits.T5IP = 2;
    IEC0bits.T5IE = 1;
    //T5CONbits.ON = 1;
}

void __ISR(11, IPL5SOFT) gps_button_handler(void)
{
    IFS0bits.INT2IF = 0;            // Clear button interrupt flag

    if (INTCONbits.INT2EP == RISE)
    {
        INTCONbits.INT2EP = FALL;
        //serial_send('b');
        if (route_done)
        {
            // Do nothing
            _nop();
        }
        else if (wp_done && !mode_prog)
        {
            u8 next_active_wp = get_next_active_wp_id(wp_num + 1);
            if (next_active_wp == (u8)-1)
            {
                // game is done -- but it shoudn't happen here
                wp_num = -1;
                error(E_DEVELOPER_IS_SHIT);
                return ;
            }
            wp_num = next_active_wp;
            get_waypoint(&wp_data, wp_num);
            eeprom_write_byte(CURRENT_WP_ADDR, wp_num);
            max_dist = distance((gps_coord_t*)&wp_data, &last_pos);
            max_dist *= FURTHEST_POINT_PCT;
            enable_gps_rx();
            wp_done = FALSE;
        }
        else
        {
            TMR5 = 0;
            IFS0bits.T5IF = 0;
            ticks = 0;
            T5CONbits.ON = 1;
        }
    }
    else
    {
        INTCONbits.INT2EP = RISE;
        //serial_send('f');
        //leds_busy = FALSE;
        if (erase_trigger)
        {
            // Do nothing, stay purple
        }
        else if (erase_done)
        {
            // Go back blue
            set_leds_pct(100);
            OC3RS = BLUE_PR;
            OC1RS = 0;
            leds_busy = FALSE;
            erase_done = FALSE;
        }
        else if (mode_prog)
        {
            // Just created a waypoint
            set_leds_pct(100);
            smooth_leds(TRUE);
        }
        else
        {
            smooth_leds(TRUE);
        }
        T5CONbits.ON = 0;
        TMR5 = 0;
    }
}


void __ISR(20, IPL2SOFT) timer5_handler(void)
{
    IFS0bits.T5IF = 0;

    static u8 succeeded;
    
    if (!PORTBbits.RB13)
    {
        ticks = 0;
        T5CONbits.ON = 0;
    }
    ticks++;
    /*if (!(ticks % 25))
        serial_send('X');
    return ;*/

    if (!mode_prog)
        ;
    else if (ticks == 25 * ERASE_DELAY * 2)
    {
        disable_gps_rx(); // Erasing can take seconds
        erase_trigger = TRUE;
        //set_leds_pct(50);
        leds_busy = TRUE;
        OC3RS = BLUE_PR;
        OC1RS = RED_PR;
        //erase_all_waypoints();
        //enable_gps_rx();
        //route_done = FALSE;
        //erase_done = PORTBbits.RB13;
    }
    //-------------------------------------------------------------------------- Bug here - if not fixed after 3 secondes but fixed after 5 seconds, will crash ------------------------------------------------
    else if (!gps_fixed || !input_initialized)
        ;
    else if (ticks < 25 * 3)
        ;
    else if (ticks == 25 * 3)
    {
        //serial_send('c');
        if (create_waypoint())
        {
            succeeded = TRUE;
            OC1RS = 0;
            // ok
            // blink blue led
            //gps_led_mode(GPS_LED_BLINK_FAST);
        }
        else
        {
            succeeded = FALSE;
            OC3RS = 0;
            // error
            // blink red led
            //ticks = 0;
            //T5CONbits.ON = 0;
        }
        //ticks = 0;
        //T5CONbits.ON = 0;
        leds_busy = TRUE;
    }
    else if (succeeded)
    {
        if (ticks <= (25 * 4) + (25 / 2))
        {
            // Blink blue
            u8 led_on = ((ticks % 4) < 2);
            OC3RS = led_on * RED_PR;
        }
        else if (ticks < 25 * 6)
        {
            // Leds off
            OC3RS = 0;
        }
        else if (ticks == 25 * 6)
        {
            activate_last_waypoint();
        }
        else if (ticks < 25 * 7)
        {
            // Blink blue
            u8 led_on = ticks % 2;
            OC3RS = led_on * RED_PR;
        }
        else
        {
            OC3RS = 0;
            //leds_busy = FALSE;
            smooth_leds(TRUE);
            ticks = 0;
            T5CONbits.ON = 0;
            wp_done = FALSE;
        }
    }
    else
    {
        // Error.
        if (ticks < 25 * 5)
        {
            u8 led_on = ((ticks % 4) < 2);
            OC1RS = led_on * RED_PR;
        }
        else
        {
            OC1RS = 0;
            //leds_busy = FALSE;
            smooth_leds(TRUE);
            ticks = 0;
            T5CONbits.ON = 0;
            wp_done = FALSE;
        }
    }
}

u8 vacant_wp_id(void)
{
    urban_t wp;
    u8 i;

    for (i = 0; i < 31; i++)
    {
        get_waypoint(&wp, i);
        if (wp.active != 255)
            ;
        else
            return i;
    }
    return i;
}

u8 get_next_active_wp_id(u8 from)
{
    urban_t wp;
    u8 i;

    for (i = from; i < 31; i++)
    {
        get_waypoint(&wp, i);
        if (wp.active == 1)
            return i;
        if (wp.active == 255)
            return ((u8)-1);
    }
    return ((u8)-1);
}

u8  create_waypoint()
{
    u8 id;
    urban_t new;
    gps_coord_t last;

    if (!gps_fixed)
        return FALSE;
    id = vacant_wp_id();
    if (id == 31)
        return FALSE;
    last = input_buffer[(input_index + (GPS_INPUT_BUFFER_SIZE - 1)) % GPS_INPUT_BUFFER_SIZE];
    memcpy(&new, &last, sizeof(last));
    strcpy(new.str, "New IRL point");
    new.active = 0;
    _nop();
    eeprom_write(((u16)id) * STRUCT_SIZE, &new, sizeof(new));
    if (id != 30)
        eeprom_write_byte(((u16)id + 1) * STRUCT_SIZE + (STRUCT_SIZE - 1), 0xFF);
    return (TRUE);
}

void  activate_last_waypoint()
{
    u8 id;

    id = vacant_wp_id() - 1;
    eeprom_write_byte(((u16)id) * STRUCT_SIZE + (STRUCT_SIZE - 1), 0x01);
}