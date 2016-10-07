#include "urban.h"

extern u8 errcode;

// Todo : stop game, shut down light, do nothing except listening to serial

void    error(u8 err)
{
    static u8 first_err = 0;

    if (!first_err)
        first_err = err;

    gps_led_mode(GPS_LED_BLINK_FAST);       // Set gps led in error mode
    serial_send('E');                       // Send error byte over serial
    serial_send(err + '0');
    serial_send(err);
    serial_send('F');                       // Send error byte over serial
    serial_send(first_err + '0');
    serial_send(first_err);
    errcode = err;
    //while(1);
}
