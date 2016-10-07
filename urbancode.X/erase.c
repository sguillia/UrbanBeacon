#include "urban.h"

extern u8 leds_busy;
extern u8 erase_trigger;
extern u8 erase_done;

void erase_all_waypoints()
{
    u8 i, byte;

    for (i = 0; i < (u8)STORAGE_SIZE; i++)
        for(byte = 0; byte < sizeof(urban_t); byte++)
            eeprom_write_byte(((u16)((u16)i * sizeof(urban_t))) + byte, (u8)-1);
}

void handle_erase()
{
    erase_all_waypoints();
    erase_trigger = FALSE;
    enable_gps_rx();
    if (PORTBbits.RB13)
    {
        erase_done = TRUE;
    }
    else
    {
        leds_busy = FALSE;
        OC3RS = BLUE_PR;
        OC1RS = 0;
        set_leds_pct(100);
    }
}