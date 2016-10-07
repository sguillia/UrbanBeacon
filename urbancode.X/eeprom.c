#include "urban.h"

void    eeprom_unselect(void);                      // Ends current transaction
u8      eeprom_rdsr(void);                          // Returns status register
u8      eeprom_sendbyte(u8 code);                   // Sends a byte to eeprom and returns received byte. Does not end transaction
void    eeprom_wren(void);                          // Enables write operation
void    eeprom_wrdi(void);                          // Disables write operation
void    eeprom_write_byte(u16 addr, u8 data);       // Write one byte to memory
void    eeprom_write(u16 addr, u8* data, u32 size); // Write bytes to memory, max 32
u8      eeprom_read_byte(u16 addr);                 // Read one byte from memory
void    eeprom_read(u16 addr, u8* buf, u32 size);            // Read multiple bytes to memory

void eeprom_unselect(void)
{
    LATBbits.LATB7 = 1;
}

u8  eeprom_rdsr(void)
{
    u8 status;
    while (!SPI1STATbits.SPITBE);   // Transmit buffer empty
    LATBbits.LATB7 = 0;             // CS
    SPI1BUF = EEPROM_RDSR;          // Opcode
    while (!SPI1STATbits.SPIRBF);   // Receive buffer full
    status = SPI1BUF;               // Unused byte, clear buffer
    SPI1BUF = 0;                    // Unused pushed byte to receive
    while (!SPI1STATbits.SPIRBF);   // Receive buffer full
    status = SPI1BUF;               // Response
    LATBbits.LATB7 = 1;             // CS
    return (status);
}

u8  eeprom_sendbyte(u8 code)
{
    u8 tmp;
    while (!SPI1STATbits.SPITBE);
    LATBbits.LATB7 = 0;
    SPI1BUF = code;
    while (!SPI1STATbits.SPIRBF);
    tmp = SPI1BUF;
    return (tmp);
}

void eeprom_wren(void)
{
    eeprom_sendbyte(EEPROM_WREN);
    eeprom_unselect();
}

void eeprom_wrdi(void)
{
    eeprom_sendbyte(EEPROM_WRDI);
    eeprom_unselect();
}

void eeprom_write_byte(u16 addr, u8 data)
{
   // eeprom_sendbyte(EEPROM_WREN, 0);
    eeprom_wren();
    eeprom_sendbyte(EEPROM_WRITE);
    eeprom_sendbyte(addr >> 8);
    eeprom_sendbyte(addr & 0xFF);
    eeprom_sendbyte(data);
    eeprom_unselect();
}

void eeprom_write(u16 addr, u8* data, u32 size)
{
    eeprom_wren();
   // eeprom_sendbyte(EEPROM_WREN);
    eeprom_sendbyte(EEPROM_WRITE);
    eeprom_sendbyte(addr >> 8);
    eeprom_sendbyte(addr & 0xFF);
    while (size--)
    {
        eeprom_sendbyte(*(data++));
    }
    eeprom_unselect();
}

u8  eeprom_read_byte(u16 addr)
{
    u8 data;
    eeprom_sendbyte(EEPROM_READ);
    eeprom_sendbyte(addr >> 8);
    eeprom_sendbyte(addr & 0xFF);
    data = eeprom_sendbyte(0);
    //data = eeprom_sendbyte(0);
    eeprom_unselect();
    return (data);
}

void eeprom_read(u16 addr, u8* buf, u32 size)
{
    eeprom_sendbyte(EEPROM_READ);
    eeprom_sendbyte(addr >> 8);
    eeprom_sendbyte(addr & 0xFF);
    while (size--)
    {
        *buf = eeprom_sendbyte(0);
        buf++;
    }
    eeprom_unselect();
}