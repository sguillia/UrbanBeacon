#include "urban.h"

extern u8  uart_buf[512];
extern u16 uart_r;
extern u16 uart_w;
extern u8  errcode;

void __ISR(_UART2_VECTOR, IPL6SOFT) uart_rx(void)
{
    _nop();
    u8 tmp = U2RXREG;
    IFS1bits.U2RXIF = 0;
    //toggle_led();

    // UART buffer overrun handling
    if (U2STAbits.OERR || U2STAbits.FERR || U2STAbits.PERR)
    {
        error(E_UART_BUF_OVERRUN);
        if (U2STAbits.OERR)                     // If the error is an overrun
        {
            unsigned char mysave = U2RXREG;     // Clear UART reception register
            U2STAbits.OERR = 0;                 // Clear overrun flag
        }
        return ;
    }
    _nop(); // Do nothing
    /*while(!U2STAbits.URXDA)
    {
        _nop();
    }*/
    //uart_buf[uart_w] = U2RXREG;
    uart_buf[uart_w] = tmp;
    uart_w = (uart_w + 1) % UART_BUF_SIZE;
    if (uart_w == uart_r)
        error(E_UART_BIGBUF_OVERRUN);
    //IFS1bits.U2RXIF = 0;
}