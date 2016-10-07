#include "urban.h"

extern u8 g_gps_led_mode;
extern u8 g_gps_led_ticks;

void gps_led_mode(u8 cmd)
{
    g_gps_led_mode = cmd;
}

void gps_led_set(u8 status)
{
    LATBbits.LATB12 = status ? HIGH : LOW;
}

void gps_led_toggle(void)
{
    LATBbits.LATB12 ^= HIGH;
}

void gps_led_tick()
{
    if (g_gps_led_mode == GPS_LED_ON)
        gps_led_set(HIGH);
    else if (g_gps_led_mode == GPS_LED_OFF)
        gps_led_set(LOW);
    else
    {
        g_gps_led_ticks++;
        if ((g_gps_led_mode == GPS_LED_BLINK_SLOW) && (g_gps_led_ticks >= GPS_LED_BLINK_SLOW_TICKS)
            || (g_gps_led_mode == GPS_LED_BLINK_FAST) && (g_gps_led_ticks >= GPS_LED_BLINK_FAST_TICKS))
        {
            g_gps_led_ticks = 0;
            gps_led_toggle();
        }
    }
}