#include "urban.h"

extern u8   rxmode;
extern u8   gps_fixed;

void enable_gps_rx(void)
{
    rxmode = WAIT_DOLLAR;
    IFS1bits.U1RXIF = 0;
    U1STAbits.URXEN = 1;
}

void disable_gps_rx(void)
{
    U1STAbits.URXEN = 0;
    rxmode = WAIT_DOLLAR;
    gps_fixed = FALSE;
}

void serial_dump_ggabuf(u8 buf[9][11])
{
    u8 i, j;

    serial_line("\nDumping tab\n");
    for (i = 0; i < 9; i++)
    {
    serial_send('_');
    serial_send('0' + i);

        for (j = 0; buf[i][j]; j++)
        {
            serial_send(buf[i][j]);
        }
    serial_send('\n');
    }
}




void consider_gpgga_sentence(u8 ggabuf[9][11])
{
    gps_coord_t data;
    serial_line("Got GPGGA sentence !\n");
    //serial_dump_ggabuf(ggabuf);
    // Empty GPGGA : $GPGGA,124513.304,,,,,0,0,,,M,,M,,*4F
    // Full GPGGA :  $GPGGA,134205.000,4853.8025,N,00219.1076,E,1,5,1.92,39.5,M,47.3,M,,*62
    // $GPGGA, 134205.000 , 4853.8025 , N , 00219.1076 , E , 1 , 5 , 1.92 , 39.5 , M , 47.3 , M , , *62
    //              0           1       2        3       4   5   6    7      8
    // $GPGGA, 124513.304 ,           ,   ,            ,   , 0 , 0 ,      ,      , M ,      , M , , *4F
    // Nb satellites = 6
    // Nb of satellites is arbitrarily limited to 99 in this software
    // Gps locked = strlen(1) ? true : false;
    // Latitude = 1
    // Latitude type = 2
    // Longitude = 3
    // Longitude type = 4

    u8 nb_sats;
    if (ggabuf[6][0] == '\0')
    {
        error(E_EMPTY_SATNUM);
        return ; // Invalid sentence
    }
    nb_sats = ggabuf[6][0] - '0';
    if (nb_sats > 9)
        error(E_INVALID_SATNUM1);
    if (ggabuf[6][1] != '\0')
    {
        nb_sats *= 10;
        u8 tmp = ggabuf[6][1] - '0';
        if (tmp > 9)
            error(E_INVALID_SATNUM2);
        nb_sats += tmp;
    }

    if (ggabuf[2][0] == '\0') // No GPS data
        acknowledge_unfixed_gps(nb_sats);
    else
    {
        float lat = parse_lat(ggabuf[1]);
        if (ggabuf[2][0] == 'S')
            lat = -lat;
        float lon = parse_lon(ggabuf[3]);
        if (ggabuf[4][0] == 'O')
            lon = -lon;
        float alt = parse_float(ggabuf[8]);
        
        data.lat = lat;
        data.lon = lon;
        data.alt = alt;

        acknowledge_fixed_gps(nb_sats, data);
        
        /*serial_send('X');
        serial_line(ggabuf[1]);
        serial_send('X');
        serial_line(ggabuf[3]);
        serial_send('X');
        serial_line(ggabuf[8]);
        serial_send('\n');*/
        _nop();
    }
    //serial_send('&');
    //serial_send(nb_sats);
}
