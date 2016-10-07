#include "urban.h"

extern u8  gps_buf[512];
extern u16 gps_r;
extern u16 gps_w;

// Todo : add errcode handling in case of error


void __ISR(_UART1_VECTOR, IPL6SOFT) gps_rx(void)
{
    _nop();
    u8 tmp = U1RXREG;
    IFS1bits.U1RXIF = 0;
    //toggle_led();

    // UART buffer overrun handling
    if (U1STAbits.OERR || U1STAbits.FERR || U1STAbits.PERR)
    {
        error(E_GPS_BUF_OVERRUN);
        if (U1STAbits.OERR)                     // If the error is an overrun
        {
            unsigned char mysave = U1RXREG;     // Clear UART reception register
            U1STAbits.OERR = 0;                 // Clear overrun flag
        }
        return ;
    }
    _nop(); // Do nothing
    gps_buf[gps_w] = tmp;
    gps_w = (gps_w + 1) % GPS_BUF_SIZE;
    if (gps_w == gps_r)
        error(E_GPS_BIGBUF_OVERRUN);
}