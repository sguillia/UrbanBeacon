#include "urban.h"

void serial_send(unsigned char cx)
{
    // While transmit shift register is not empty
    while (!U2STAbits.TRMT);
    U2TXREG = cx;
}

void serial_line(u8 *str)
{
    while (*str)
    {
        while (!U2STAbits.TRMT);
        U2TXREG = *str;
        str++;
    }
}

void serial_write(u8 *mem, u32 size)
{
    while (size--)
    {
        while (!U2STAbits.TRMT);
        U2TXREG = *mem;
        mem++;
    }
}