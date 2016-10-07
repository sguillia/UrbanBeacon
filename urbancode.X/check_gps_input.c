#include "urban.h"

extern u8  gps_buf[GPS_BUF_SIZE];
extern u16 gps_r;
extern u16 gps_w;

extern u8 rxmode;

static u8 buffercmp(u8* str)
{
    u16 i = gps_r;
    while (*str)
    {
        if (*str != gps_buf[i])
            return (1);
        i = (i + 1) % GPS_BUF_SIZE;
        str++;
    }
    return (0);
}

u8  check_gps_input(void)
{
    static u16 rxsize;                 // Number of unread bytes in buffer
    static u8  index_tab;              // Current tab index (as if exploded by ',')
    static u8  index_char;             // Current writer position (in a string)
    static u8  ggabuf[9][11];          // Exploded GPGGA sentence (7 strings with max strlen 10 + null byte)
    
    // Get number of unread bytes
    rxsize = gps_w - gps_r;
    if (rxsize < 0)
        rxsize += GPS_BUF_SIZE;
    if (gps_r != gps_w && (rxmode != WAIT_TYPE || (rxmode == WAIT_TYPE && rxsize >= 6)))
    {

        /*
        // This redumps gps input to ftdi output
        while (!U2STAbits.TRMT);
            U2TXREG = gps_buf[gps_r];
        gps_r = (gps_r + 1) % GPS_BUF_SIZE;
        return 0;
        // */
        
        _nop();
        // Waiting a NMEA instruction
        if (rxmode == WAIT_DOLLAR)
        {
            if (gps_buf[gps_r] == '$')
                rxmode = WAIT_TYPE;
            gps_r = (gps_r + 1) % GPS_BUF_SIZE;
        }            // Waiting type (GPRMC or GPGGA)
        else if (rxmode == WAIT_TYPE)
        {
            if (rxsize >= 6) {
                if (0 && buffercmp("GPRMC") == 0)
                {
                    rxmode = BUFFER_GPRMC;
                    index_tab = 0;
                    index_char = 0;
                    //serial_send('C');
                }
                else if (buffercmp("GPGGA") == 0)
                {
                    rxmode = BUFFER_GPGGA;
                    index_tab = 0;
                    index_char = 0;
                    //serial_send('D');
                }
                else
                    rxmode = WAIT_DOLLAR;
                if (rxmode != WAIT_DOLLAR) {
                    gps_r = (gps_r + 5) % GPS_BUF_SIZE;
                    if (gps_buf[gps_r] != ',')
                        rxmode = WAIT_DOLLAR; // Error, going back
                    else
                        gps_r = (gps_r + 1) % GPS_BUF_SIZE;
                }
            }
        }
        else if (rxmode == BUFFER_GPRMC || rxmode == BUFFER_GPGGA)
        {
            u8 rxchar = gps_buf[gps_r];
            if (rxchar == '$')
            {
                rxmode = WAIT_DOLLAR;
                //serial_send('S');
            }
            else
            {
                // Empty GPGGA : $GPGGA,124513.304,,,,,0,0,,,M,,M,,*4F
                // Full GPGGA :  $GPGGA,134205.000,4853.8025,N,00219.1076,E,1,5,1.92,39.5,M,47.3,M,,*62
                // $GPGGA, 134205.000 , 4853.8025 , N , 00219.1076 , E , 1 , 5 , 1.92 , 39.5 , M , 47.3 , M , , *62
                //              0           1       2        3       4   5   6
                // Bufferize char
                if (rxchar == ',') // Found separator
                {
                    //serial_send(',');
                    if (index_tab == 8)
                    {
                        // End of bufferising !
                        ggabuf[index_tab][index_char] = '\0';
                        consider_gpgga_sentence(ggabuf);
                        rxmode = WAIT_DOLLAR;
                    }
                    else
                    {
                        ggabuf[index_tab][index_char] = '\0';
                        index_tab++;
                        index_char = 0;
                    }
                }
                else if (rxchar == '$') // Unexpected token, exiting buffering mode
                {
                    rxmode = WAIT_DOLLAR; // This dollar won't be taken into account because gps_r is gonna be increased
                }
                else
                {
                    if (index_char == 10) // String is full and char is not a comma
                    {
                        rxmode = WAIT_DOLLAR;
                    }
                    else
                    {
                        ggabuf[index_tab][index_char] = rxchar;
                        index_char++;
                        //serial_send('x');
                    }
                }
            }
            gps_r = (gps_r + 1) % GPS_BUF_SIZE;
        }
        //serial_send('H' + rxmode);
        return (TRUE);
    }
    else
        return (FALSE);
}