#ifndef TYPES_H
# define TYPES_H

typedef unsigned char		u8;
typedef unsigned short		u16;
typedef unsigned long		u32;

typedef signed char		s8;
typedef signed short		s16;
typedef signed long		s32;

#define OUTPUT  0
#define INPUT   1
#define HIGH    1
#define LOW     0
#define TRUE    1
#define FALSE   0

#endif

#include <p32xxxx.h>
#include <xc.h>
#include <sys/attribs.h>

#define DELAY_1000_MS   256 * 8 * 16
#define DELAY_500_MS    256 * 8 * 8
#define DELAY_250_MS    256 * 8 * 4
#define DELAY_125_MS    256 * 8 * 2
#define DELAY_62_MS     256 * 8 * 1

#define RISE            1
#define FALL            0

const int g_mstab[5] = {DELAY_1000_MS,
                        DELAY_500_MS,
                        DELAY_250_MS,
                        DELAY_125_MS,
                        DELAY_62_MS};
const int g_ms_irl[5] = {1000, 500, 250, 125, 62};

int g_index = 0;
int PWMmode = FALSE;
int clocksSinceLastPress = 0;
int wanted_pct = 100;  // PWM voulu
int change_delta = -1;
int incycle_pct = 0; // avancement dans un meme cycle ON/OFF
int g_buttonmode = FALL;
int g_doskip = 0;

int     check_button(void)
{
    return (!PORTDbits.RD8);
}

int     toggle_led(void)
{
    LATFbits.LATF1 ^= HIGH;
}

void init_io()
{
    LATFbits.LATF1 = HIGH;      // LED on
    TRISFbits.TRISF1 = OUTPUT;  // LED is output
    TRISDbits.TRISD8 = INPUT;   // Button is input
}

void init_button_interrupt()
{
         // ------------- Button interrupt -------------

    /* From pic32mx datasheet : Interrupts :
     * INT1 ? External Interrupt
     * IRQ - 7
     * Vector 7
     * Flag::IFS0<7>
     * Enable:: IEC0<7>
     * Priority: IPC1<28:26>
     * Sub-PriorityIPC1<25:24>
     * */

    IEC0bits.INT1IE = 0;    // Disable interrupts to change registers
    IFS0bits.INT1IF = 0;    // Clear flag
    IPC1bits.INT1IP = 5;    // Priority
    INTCONbits.INT1EP = FALL;  // Catch falling edge (button pressed)
                            // Found in reference manual, section 08 interrupts
    IEC0bits.INT1IE = 1;    // Enable

    // Multi-vector mode
    // Found in reference manual pic32mx::Interrupts::MultiVectorMode
    INTCONbits.MVEC = 1;

}

void init_timer_interrupt()
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

void init_timer()
{
        // ------------- Timer enable -------------
    //  Everytinh was found in pic32mx :: reference manual :: Section 14 timers ::
    //  block diagram page 3
    T1CONbits.TCS = 1;
    T1CONbits.TCKPS = 0b00; // Ref manual section 14 timers, search TCKPS, prescale
    TMR1 = 0;
    PR1 = DELAY_1000_MS;
}

void enable_timers()
{
    T1CONbits.ON = 1;       // enable timer 1 (see block diagram)
    IEC0bits.T1IE = 1;      // Enable interrupt
}

void    enterPWMmode()
{
    IEC0bits.T1IE = 0;
    PR1 = 7;
    TMR1 = 0;
    IEC0bits.T1IE = 1;
    PWMmode = TRUE;
}

int     main(void)
{
    // This was found in MPLABX Help Center : Interrupts : Enabling/Disabling Interrupts
    __builtin_enable_interrupts();

    init_io();
    init_button_interrupt();
    init_timer_interrupt();
    init_timer();
    enable_timers();

    while (1)
    {
    }
    return (0);
}

// IPL5soft was found in MPLABX Help Center : Interrupts :
//      "IPL2SOFT creates an interrupt handler function for the core timer interrupt
//       that has an interruptpriority level of two"
// In main, priority is set to 5, so macro is IPL5SOFT

void __ISR(7, IPL5SOFT) button_handler(void)
{
    IEC0bits.T1IE = 0;              // Disable timer interrupt
    IFS0bits.INT1IF = 0;            // Clear button interrupt flag

    if (PWMmode)                    // Do nothing
        ;
    else if (g_buttonmode == FALL)  // Button pressed
    {
        g_index++;
        g_index %= 5;
        PR1 = g_mstab[g_index];     // Change timer freq
        TMR1 = 0;
    }
    else                            // Button released
    {
        clocksSinceLastPress = 0;
    }

    // Change edge so we can catch both rise and fall edge in the same handler
    g_buttonmode ^= 1;
    INTCONbits.INT1EP = g_buttonmode;
    IEC0bits.T1IE = 1;              // Enable timer interrupt
}


void __ISR(4, IPL4SOFT) timer_handler(void)
{
    IFS0bits.T1IF = 0;              // Clear flag

    if (PWMmode)
    {
        incycle_pct++;
        if (incycle_pct == 101)
        {
            incycle_pct = 0;
            wanted_pct += change_delta;
            if (wanted_pct == 101)
            {
                wanted_pct = 99;
                change_delta = -1;
            }
            else if (wanted_pct == -1)
            {
                wanted_pct = 1;
                change_delta = +1;
            }
        }
        if (incycle_pct >= wanted_pct)
            LATFbits.LATF1 = LOW;
        else
            LATFbits.LATF1 = HIGH;
    }
    else
    {
        toggle_led();
        if (check_button())
        {
            clocksSinceLastPress += g_ms_irl[g_index];
            if (clocksSinceLastPress >= 2000)
              enterPWMmode();
        }
    }
}