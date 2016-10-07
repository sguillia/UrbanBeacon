#include "urban.h"

/*** Global variables ***/
// GPS LED
u8  g_gps_led_mode;
u8  g_gps_led_ticks = 0;

// GPS UART
u8  gps_buf[GPS_BUF_SIZE];
u16 gps_r = 0;
u16 gps_w = 0;

// SERIAL UART 
u8  uart_buf[UART_BUF_SIZE];
u16 uart_r = 0;
u16 uart_w = 0;

// ERRORS
u8  errcode = 0;

u8 mode = MODE_DEFAULT;

// Gps input checker
u8 rxmode = WAIT_DOLLAR;

// Game info
u8          wp_num;
urban_t     wp_data;
float       max_dist;
gps_coord_t input_buffer[GPS_INPUT_BUFFER_SIZE];
u8          input_index;
u8          input_initialized;
gps_coord_t last_pos;
gps_coord_t prev_pos;
u8          gps_fixed;
u8          game_ticks = 0;
u8          last_gps_signal = 0;
u8          wp_done;
u8          route_done = FALSE;

u8          leds_busy = FALSE;

u8          mode_prog;

u8          erase_trigger = FALSE;
u8          erase_done = FALSE;

float       target_blue = 0.0, target_red = 0.0, oc_blue = 0.0, oc_red = 0.0;

void    check_uart_input(void);
void    init_spi(void);

int main()
{
    __builtin_enable_interrupts();

        /*
         * Backup 1 and 2 for GPS
         * Backup 6 for blue led
         *
         */
    LATBbits.LATB9 = LOW;
    TRISBbits.TRISB9 = OUTPUT;


    // Setup GPS led
    TRISBbits.TRISB12 = OUTPUT;
    LATBbits.LATB12 = LOW;
    // Setup GPS button
    ANSELBbits.ANSB13 = 0;
    TRISBbits.TRISB13 = INPUT;

    // LED and button
    mvec();
    init_button_interrupt();
    init_timer1(DELAY_125_MS);
    init_timer1_interrupt();
    //init_timer1(DELAY_1000_MS); // delay should be adjusted inside timer1 :: tckps
    enable_timers();

    setup_t5();

    // UART
    init_uart_ftdi(4800);
    init_uart_gps(9600);

    // PWM
    /*OC1CONbits.ON = 0; // disable to change parameters
    PR2 = 1000; // period (timer 2 threshold)
    OC1R = 10; // current duty cycle (readonly if non disabled)
    OC1RS = 100; // next duty cycle
    //OC1R = 25000;
    OC1CONbits.OCM = 0b110; // enable in pwm mode, no fault pin
    TMR2 = 0; // clear timer 2
    OC1CONbits.OCTSEL = 0; // timer 2
    OC1CONbits.ON = 1; // enable pwm
    T2CONbits.ON = 1; //enable timer
     */

    setup_leds_oc();

    // SPI
    //LATBbits.LATB7 = HIGH;
    //TRISBbits.TRISB7 = OUTPUT;
    init_spi();

    gps_led_mode(GPS_LED_OFF);

    /*
     * Mecanisme de jeu propose:
     * - Garder en permanence les 5 derniers points recus par le GPS
     *      pour faire une moyenne, et donc avoir une position plus stable
     * - Toutes les 5 secondes, on stocke cette moyenne comme la position actuelle
     *    en fait il faut la stocker deux fois, une pour la position d'il y a 5 secondes,
     *    une pour la position actuelle
     * - Toutes les 5 secondes, on calcule deux distances (anciennne pos vers cible et pos actuelle vers cible)
     * - On calcule la couleur voulue et on set les duty cycles des PWM par rapport a cela
    */

    /*
     * Donc, niveau code :
     *  - On set une interruption de timer toutes les 5 secondes
     *  - calculate_average_position()
     *  - old_pos = act_pos
     *  - act_pos = new_pos
     *  - color_from_distances()
     *  - set_leds_color()
     */

    mode_prog = PORTBbits.RB13;

    /*
     *
     */
    u8 next_active_wp;

    wp_done = FALSE;
    gps_fixed = FALSE;
    input_initialized = FALSE;
    if (mode_prog)
    {
        wp_num = -1;
        set_leds_pct(100);
    }
    else
    {
        wp_num = eeprom_read_byte(CURRENT_WP_ADDR);
        next_active_wp = get_next_active_wp_id(wp_num);
        if (next_active_wp == (u8)-1)
        {
            wp_num = -1;
            error(E_NO_ACTIVE_WAYPOINT);
            disable_gps_rx(); // not in prog mode, no waypoint, nothing to do
            _nop();
        }
        else
        {
            wp_num = next_active_wp;
            get_waypoint(&wp_data, wp_num);
            _nop();
        }
    }

    /*
    get_waypoint(&wp_data, 0);
    if (wp_data.active == 255)
    {
        wp_num = -1;
        // No waypoint in memory !
        error(E_NO_WAYPOINT);
        //while(1);
    }
    else if (wp_data.active == 0)
    {
        u8 next_active_wp = get_next_active_wp_id(0);
        if (next_active_wp == (u8)-1)
        {
            wp_num = -1;
            error(E_NO_ACTIVE_WAYPOINT);
        }
        else
        {
            wp_num = next_active_wp;
        }
    }*/

    setup_game_timer();

    //disable_gps_rx();

    while (1)
    {
        _nop();
        check_gps_input();
        check_uart_input();
        smooth_leds(FALSE);
        if (erase_trigger)
            handle_erase();
    }

    return (0);

}