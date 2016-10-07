#include "urban.h"

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
extern float        target_blue;
extern float        target_red;
extern u8           last_gps_signal;
extern u8           mode_prog;
extern u8           wp_done;
extern u8           route_done;

void acknowledge_unfixed_gps(u8 nb_sats)
{
    gps_fixed = FALSE;
    last_gps_signal = 0;
    gps_led_mode(GPS_LED_BLINK_SLOW);
    serial_line("\nAcknowledged unfixed GPS !\n");
    /*if (nb_sats < 10)
    {
        serial_line("Number of satellites : ");
        serial_send(nb_sats + '0');
        serial_send('\n');
    }*/
    if (!mode_prog)
    {
        target_blue = 0.0;
        target_red = 0.0;
    }
}

void acknowledge_fixed_gps(u8 nb_sats, gps_coord_t data)
{
    _nop();
    gps_fixed = TRUE;
    last_gps_signal = 0;
    gps_led_mode(GPS_LED_ON);
    serial_line("Acknowledged fixed GPS !\n");
    if (!mode_prog && wp_num == (u8)-1)
    {
        serial_line("Ignoring - no wp num");
        return ;
    }
    else if (route_done)
    {
        serial_line("Ignoring - route done");
        return ;
    }
    else if (wp_done)
    {
        serial_line("Ignoring - wp done");
        return ;
    }
    if (!input_initialized)
    {
        if (!mode_prog)
        { // In program mode, there is no wp_num, no wp_data, no distance
            max_dist = distance((gps_coord_t*)&wp_data, &data);
            max_dist *= FURTHEST_POINT_PCT;
            _nop();
        }
        u8 tmp;
        for (tmp = 0; tmp < GPS_INPUT_BUFFER_SIZE; tmp++)
            input_buffer[tmp] = data;
        last_pos = data;
        prev_pos = data;
        input_initialized = 1;
    }
    else
        input_buffer[input_index] = data;
    if (!mode_prog)
        game_loop();
    input_index = (input_index + 1) % GPS_INPUT_BUFFER_SIZE;
}