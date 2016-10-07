#include "urban.h"

void get_waypoint(u8* buf, u8 index)
{
    u8 tmp;
    eeprom_sendbyte(EEPROM_READ);
    u16 addr = (u16)index * STRUCT_SIZE;
    eeprom_sendbyte(addr >> 8);
    eeprom_sendbyte(addr & 0xFF);
    for (tmp = 0; tmp < 32; tmp++)
        buf[tmp] = eeprom_sendbyte(0);
    eeprom_unselect();
}

void get_hard_waypoint(u8 *buf, u8 index)
{
    urban_t hard1 = {48.8925077, 2.3008609, 30.0, "Hard 1", 1};
    urban_t hard2 = {48.8958365, 2.3173643, 30.0, "Lycee", 1};
    urban_t hard3 = {48.8964576, 2.3185032, 30.0, "Ecole 42 (18z)", 1};
    urban_t hard4 = {48.896865, 2.318126, 30.0, "Food truck", 1};

    u8 *mem = (u8*)&hard4;
    u8 tmp;
    for (tmp = 0; tmp < 32; tmp++)
        buf[tmp] = mem[tmp];
    /*wp->lat = hard1.lat;
    wp->lon = hard1.lon;
    wp->alt = hard1.alt;
    wp->str[0] = '\0';
    wp->active = 1;*/
}