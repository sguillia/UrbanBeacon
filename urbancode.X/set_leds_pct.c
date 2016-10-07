#include "urban.h"

extern float    target_blue, target_red, oc_blue, oc_red;

void set_leds_pct(u8 pct)
{
    u16 npct;

    npct = (u16)pct;
    if (npct >= 50)
    {
        target_blue = BLUE_PR;
        target_red = (100-2*(npct-50)) * RED_PR / 100;
    }
    else
    {
        target_blue = 2 * npct * BLUE_PR / 100;
        target_red = RED_PR;
    }
}