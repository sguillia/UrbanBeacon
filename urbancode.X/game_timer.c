#include "urban.h"
#include "math.h"

// Game info
extern u8           wp_num;
extern urban_t      wp_data;
extern float        max_dist;
extern gps_coord_t  input_buffer[GPS_INPUT_BUFFER_SIZE];
extern u8           input_index;
extern u8           input_initialized;
extern gps_coord_t  last_pos;
extern gps_coord_t  prev_pos;
extern u8           gps_fixed;
extern float          target_blue;
extern float          target_red;
extern u8           game_ticks;
extern u8           last_gps_signal;
extern u8           wp_done;
extern u8           route_done;
extern u8           mode_prog;
extern u8           leds_busy;

// Vector 0 0 4 4 16
void setup_game_timer(void)
{
    // Setup timer
    T4CONbits.TCS = 0;
    T4CONbits.TCKPS = 0b111;
    TMR4 = 0;
    PR4 = 15625;
    // Setup interrupt
    IEC0bits.T4IE = 0;
    IFS0bits.T4IF = 0;
    IPC4bits.T4IP = 3;
    // Enable
    T4CONbits.ON = 1;
    IEC0bits.T4IE = 1;
}

/*static gps_coord_t input_average(void)
{
    u8 tmp;
    float av_lat;
    float av_lon;
    gps_coord_t av;
    
    av.lat = (float)(input_buffer[0].lat);
    av.lon = (float)(input_buffer[0].lon);
    av.alt = (float)(input_buffer[0].alt);

    _nop();

    if (GPS_INPUT_BUFFER_SIZE == 1)
        return (av);
    
    for (tmp = 1; tmp < GPS_INPUT_BUFFER_SIZE; tmp++)
    {
        av.lat += input_buffer[tmp].lat;
        av.lon += input_buffer[tmp].lon;
    }
    
    av.lat /= (float)tmp;
    av.lon /= (float)tmp;
    
    return (av);
}*/

void __ISR(16, IPL3SOFT) game_timer(void)
{
    IFS0bits.T4IF = 0;

    //game_ticks++; // game_ticks are unused yet
    if (!wp_done && ((!mode_prog && (wp_num != (u8)-1)) || mode_prog))
        last_gps_signal++;
    if (last_gps_signal == GPS_TIMEOUT)
        gps_led_mode(GPS_LED_OFF);
    if (last_gps_signal >= GPS_TIMEOUT)
    {
        // No GPS data !
        gps_fixed = FALSE;
        if (!mode_prog)
        {
            target_blue = 0.0;
            target_red = 0.0;
        }
    }

    /*if (game_ticks == GAME_TIMER_DELAY)
    {
        if (!input_initialized || !gps_fixed)
        {
            game_ticks = 0;
            return ;
        }
        //game_loop();
        ticks = 0;
    }*/
}

float bearing(gps_coord_t *a, gps_coord_t *b)
{
    float lat1 = a->lat;
    float lat2 = b->lat;
    float lon1 = a->lon;
    float lon2 = b->lon;
    _nop();
    lat1 = lat1 * M_PI / 180.0;
    lat2 = lat2 * M_PI / 180.0;
    lon1 = lon1 * M_PI / 180.0;
    lon2 = lon2 * M_PI / 180.0;
    float y = sin(lon2 - lon1) * cos(lat2);
    float x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1);
    float brng = atan2(y, x);
    brng = brng * 180 / M_PI;
    brng += 180.0;
    return (brng);
    //brng /= 2.0;
    /*u16 brngx = (u16)brng;
    serial_send('X');
    u8 u1 = (u8)(brngx % 10);
    u8 u2 = (u8)((brngx % 100) / 10);
    u8 u3 = (u8)((brngx % 1000) / 100);
    serial_send('0' + u3);
    serial_send('0' + u2);
    serial_send('0' + u1);
    serial_send('Y');
    serial_send('\n');
    _nop();*/
}

float bearing_angle(float a, float b)
{
    float d1, d2;

    d1 = 360.0 - a + b;
    d2 = a - b;
    if (d1 >= 360.0)
        d1 -= 360.0;
    if (d1 < 0.0)
        d1 += 360.0;
    if (d2 >= 360.0)
        d2 -= 360.0;
    if (d2 < 0)
        d2 += 360.0;

    if (d1 < d2)
        return (d1);
    else
        return (d2);
}

void game_loop(void)
{
    float dist;
    float abs_pct;
    float rel_pct;
    float abs_weight = 0.0;
    float rel_weight = 1.0 - abs_weight;
    float tot_pct;
    float brng_from;
    float brng_to;
    float brng_angle;
    float rel_dist;

    if (wp_done)
        return ;
    prev_pos = input_buffer[input_index];
    last_pos = input_buffer[(input_index + (GPS_INPUT_BUFFER_SIZE - 1)) % GPS_INPUT_BUFFER_SIZE];
    dist = distance(&last_pos, (gps_coord_t*)&wp_data);
    rel_dist = distance(&prev_pos, &last_pos);

    if (rel_dist <= (DIST_STATIONARY / 10000.0))
    { // We're moving !
        abs_weight = 1.0;
        rel_weight = 0.0;
        //set_leds_pct(0);
    }
    else
        ; //set_leds_pct(100);
   // return ;
    
    if (dist < (GOAL_RADIUS / 10000.0))
    { // We're in the waypoint !
        wp_done = TRUE;
        target_red = 0.0;
        target_blue = 0.0;
        disable_gps_rx();
        u8 next_active_wp = get_next_active_wp_id(wp_num + 1);
        if (next_active_wp == (u8)-1)
        {
            // Game is done
            route_done = TRUE;
            eeprom_write_byte(CURRENT_WP_ADDR, 0); // Reset current waypoint to 0
        }
        _nop();
        return ;
    }
    _nop();
    if (dist > max_dist)
    max_dist = dist;
    abs_pct = dist / max_dist;

    // Relative percentage starts from purple == 50%
    //rel_pct = 0.5;

    // Absolute bearing (compass) of movement
    brng_from = bearing(&prev_pos, &last_pos);

    // Absolute bearing of destination
    brng_to   = bearing(&last_pos, (gps_coord_t*)&wp_data);

    // Relative bearing angle, center is you, rays go to prev and goal
    brng_angle = bearing_angle(brng_from, brng_to);

    /*
     *  Now we got an angle comprised between 0.0 and 180.0 degrees
     *  The closer it is to 0, the better the direction we follow is
     *  0  = good, red
     *  90 = nearly perpendicular, purple (nearly because earth is not flat, except for conspirasionists
     *  180 = not good, blue
     */

    
    //rel_pct += brng_angle;

    /*u16 brngx = (u16)brng_angle;
    serial_send('X');
    u8 u1 = (u8)(brngx % 10);
    u8 u2 = (u8)((brngx % 100) / 10);
    u8 u3 = (u8)((brngx % 1000) / 100);
    serial_send('0' + u3);
    serial_send('0' + u2);
    serial_send('0' + u1);
    serial_send('Y');
    serial_send('\n');*/

    //brng_angle -= 90.0;

    rel_pct = 1.0 - (brng_angle / 180.0);

    tot_pct = abs_pct * abs_weight + rel_pct * rel_weight;

    if (tot_pct > 1.0){
        error(E_ABS_OVERLIMIT);
        _nop();
    }
    else if (tot_pct < 0.0){
        error(E_ABS_UNDERLIMIT);
        _nop();
    }
    else
    {
        _nop();
        u8 pct_int = (u8)(tot_pct * 100.0);
        _nop();
        set_leds_pct(pct_int);
    }
    _nop();
}