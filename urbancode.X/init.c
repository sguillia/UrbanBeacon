#include "urban.h"

/* Non-init */

void enable_timers()
{
    T1CONbits.ON = 1;       // enable timer 1 (see block diagram)
    IEC0bits.T1IE = 1;      // Enable interrupt
}

int     check_button(void)
{
    return 0;
    //return (!PORTDbits.RD8);
}

/* --- */

void init_timer1_interrupt()
{
        // ------------- Timer interrupt -------------
    /* From pic32mx datasheet : Interrupts :
     * T1 ? Timer1
     * IRQ 4
     * Vector 4
     * Flag IFS0<4>
     * Enable IEC0<4>
     * Priority IPC1<4:2>
     * Sub-Priority IPC1<1:0>
     * */

    IEC0bits.T1IE = 0;      // Disable interrupts to change registers
                            // Timer 1 Interrupt Enable
                            // Found in reference manual, searching "IEC0", bit 4
    IFS0bits.T1IF = 0;      // Clear flag
                            // Timer 1 Interrupt Flag
                            // Found in reference manual, searching "IFS0", bit 4
    IPC1bits.T1IP = 4;      // Priority
}



/*void init_button_interrupt() // for proto
{
         // ------------- Button interrupt -------------
*/
    /* From pic32mx datasheet : Interrupts :
     * INT1 : External Interrupt
     * IRQ - 7
     * Vector 7
     * Flag::IFS0<7>
     * Enable:: IEC0<7>
     * Priority: IPC1<28:26>
     * Sub-PriorityIPC1<25:24>
     * */
/*
    IEC0bits.INT1IE = 0;    // Disable interrupts to change registers
    IFS0bits.INT1IF = 0;    // Clear flag
    IPC1bits.INT1IP = 5;    // Priority
    INTCONbits.INT1EP = FALL;  // Catch falling edge (button pressed)
                            // Found in reference manual, section 08 interrupts
    IEC0bits.INT1IE = 1;    // Enable
}*/

// For definitive
// Gps button is on PB13 - can only be remapped to INT2
// 0 0 2 2 vector 11
void init_button_interrupt()
{
         // ------------- Button interrupt -------------

    // Remapping RB13 to INT2 (0011)
    INT2Rbits.INT2R = 0b0011;
    // Configuring INT2
    IEC0bits.INT2IE = 0;    // Disable interrupts to change registers
    IFS0bits.INT2IF = 0;    // Clear flag
    IPC2bits.INT2IP = 5;    // Priority
    IPC2bits.INT2IS = 0;
    INTCONbits.INT2EP = RISE;  // Catch some edge (button pressed)
                            // Found in reference manual, section 08 interrupts
    IEC0bits.INT2IE = 1;    // Enable
}

void mvec()
{
    // Multi-vector mode
    // Found in reference manual pic32mx::Interrupts::MultiVectorMode
    INTCONbits.MVEC = 1;
}


void init_timer1(u16 delay)
{
        // ------------- Timer enable -------------
    //  Everytinh was found in pic32mx :: reference manual :: Section 14 timers ::
    //  block diagram page 3
    T1CONbits.TCS = 0;
    T1CONbits.TCKPS = 0b10; // Ref manual section 14 timers, search TCKPS, prescale
    TMR1 = 0;
    PR1 = delay;
}

/*void init_uart(u16 baud_rate)
{
    U1MODEbits.PDSEL = 0b00; // 8-bit data, no parity. This is default
    U1BRG = 4000000 / (16 * baud_rate) - 1;
    IFS0bits.U1RXIF = 0;   // Clear flag
    IPC6bits.U1IP = 6;     // Priority
    IPC6bits.U1IS = 1;     // Subpriority
    U1STAbits.URXISEL = 0; // defaults to 0 (interrupt when character received)
    IEC0bits.U1RXIE = 1;   // Enable interrupt
    U1STAbits.UTXEN = 1;   // Enable TX
    U1STAbits.URXEN = 1;   // Enable RX
    U1MODEbits.ON = 1;     // Enable UART1
}*/

void init_uart_gps(u16 delay) // UART1
{
    ANSELBbits.ANSB2 = 0;
    RPA0Rbits.RPA0R = 0b0001; // remap rpa0 to U1TX
    U1RXRbits.U1RXR = 0b0100; // remap RPB2 to U1RX
    U1MODEbits.PDSEL = 0b00; // 8-bit data, no parity. This is default
    U1BRG = 26; // 9600 baud // ------------------------------------------------------------------------------ to change, default is 25
    //U1BRG = 51; // 4800 baud
    IFS1bits.U1RXIF = 0;   // Clear flag
    IPC8bits.U1IP = 6;     // Priority
    IPC8bits.U1IS = 1;     // Subpriority
    U1STAbits.URXISEL = 0; // defaults to 0 (interrupt when character received)
    IEC1bits.U1RXIE = 1;   // Enable interrupt
    U1STAbits.UTXEN = 1;   // Enable TX
    U1STAbits.URXEN = 1;   // Enable RX
    U1MODEbits.ON = 1;     // Enable UART1U1STAbits.URXEN = 1;   // Enable RX
}

void init_uart_ftdi(u16 delay) // UART2
{
    ANSELAbits.ANSA1 = 0;
    U2RXRbits.U2RXR = 0b0000;
    RPA3Rbits.RPA3R = 0b0010; //output
    U2MODEbits.PDSEL = 0b00; // 8-bit data, no parity. This is default
    U2BRG = 25; // 9600 baud // default 25
    //U2BRG = 51; // 4800 baud
    IFS1bits.U2RXIF = 0;   // Clear flag
    IPC9bits.U2IP = 6;     // Priority
    IPC9bits.U2IS = 1;     // Subpriority
    U2STAbits.URXISEL = 0; // defaults to 0 (interrupt when character received)
    IEC1bits.U2RXIE = 1;   // Enable interrupt
    IEC1bits.U2TXIE = 0;
    U2STAbits.UTXEN = 1;   // Enable TX
    U2STAbits.URXEN = 1;   // Enable RX
    U2MODEbits.ON = 1;     // Enable UART2
}

void    init_spi(void)
{
    // Remapping
    SDI1Rbits.SDI1R = 0b0100; //SDI1 from RB8
    RPB6Rbits.RPB6R = 0b0011; //SDO1 to RB6;

    IEC1bits.SPI1TXIE = 0;      // Disable interrupts
    IEC1bits.SPI1RXIE = 0;      // Disable interrupts
    SPI1CONbits.ON = 0;         // Disable to change registers
    unsigned char emptier;
    emptier = SPI1BUF;          // Clear buffer

    /* SPI Interrupts
    IFS1bits.SPI2RXIF = 0;
    IPC7bits.SPI2IP = 3;
    IPC7bits.SPI2IS = 1;
    IEC1bits.SPI2RXIE = 1; */

    SPI1STATbits.SPIROV = 0;    // Clear overflow
    SPI1BRG = 416; // FRC = 8mhz, fpbdiv = /2, 4 mhz / (2 * (416 + 1)) = +- 4800 baud rate
    SPI1CONbits.MSTEN = 1;      // Master mode
    LATBbits.LATB7 = HIGH;      // SS high (unselected)
    TRISBbits.TRISB7 = OUTPUT;  // SS output
    SPI1CONbits.CKP = 1;        // Clock polarity, idle high
    SPI1CONbits.ON = 1;         // Enable SPI
}