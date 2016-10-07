#include "urban.h"

extern float    target_blue, target_red, oc_blue, oc_red;
extern u8       wp_done;
extern u8       leds_busy;
extern u8       route_done;

void    smooth_leds(u8 force)
{
    float delta = 0.02;
    //delta = 1.0;
    u8 blue_chg = TRUE;
    u8 red_chg = TRUE;
    float diff_a;
    float diff_b;

    if (force)
    {
        leds_busy = FALSE;
        OC3RS = (u32)oc_blue;
        OC1RS = (u32)oc_red;
    }

    if (leds_busy)
        return ;

    if (route_done)
        delta = 0.2;

    diff_a = target_blue - oc_blue;
    if (diff_a < 0)
        diff_a = -diff_a;
    if (target_blue == oc_blue || diff_a < 2.0 * delta)
        blue_chg = FALSE;
    else if (oc_blue < target_blue)
        oc_blue += delta;
    else if (oc_blue > target_blue)
        oc_blue -= delta;
    if (blue_chg)
        OC3RS = (u32)oc_blue;
    else if (route_done)
    {
        target_blue = 0.0;
        target_red = RED_PR;
    }

    diff_b = target_red - oc_red;
    if (diff_b < 0)
        diff_b = -diff_b;
    if (target_red == oc_red || diff_b < 2.0 * delta)
        red_chg = FALSE;
    else if (oc_red < target_red)
        oc_red += delta;
    else if (oc_red > target_red)
        oc_red -= delta;
    if (red_chg)
        OC1RS = (u32)oc_red;
    else if (route_done)
    {
        target_blue = BLUE_PR;
        target_red = 0.0;
    }
}