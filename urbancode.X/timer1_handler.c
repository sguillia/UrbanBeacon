#include "urban.h"

extern u8   leds_busy, wp_done, route_done, erase_done, mode_prog;

int a = 0;

void __ISR(4, IPL4SOFT) timer1_handler(void)
{
    IFS0bits.T1IF = 0;              // Clear flag
    gps_led_tick();
    if ((!mode_prog && wp_done && !route_done)
            || (mode_prog && erase_done))
    {
        static u8   blinker = 0;
        leds_busy = TRUE;
        if (blinker == (u8)WP_MAX_TICKS)
            blinker = 0;

        if (!(blinker % (u8)3))
        {
            OC1RS = 0;
            OC3RS = 0;
        }
        else
        {
            OC1RS = RED_PR;
            OC3RS = 0;
        }

        blinker++;
    }
    /*if (a == 0)
    {
        a = 2;
        OC1RS = 50;
        OC3RS = 0;
    }
    else if (a == 2)
    {
        a = 3;
        OC1RS = 50;
        OC3RS = 50;
    }
    else
    {
        a = 0;
        OC1RS = 0;
        OC3RS = 50;
    }*/
}