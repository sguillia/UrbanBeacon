#include "urban.h"

void setup_leds_oc(void){
// --- Output compare for blue leds

    // init light
    RPB10R = 0b0101;
    // PWM
    OC3CONbits.ON = 0; // disable to change parameters
    PR3 = BLUE_PR; // period (timer threshold)
    OC3R = 0; // current duty cycle (readonly if non disabled)
    OC3RS = 0; // next duty cycle
    //OC1R = 25000;
    OC3CONbits.OCM = 0b110; // enable in pwm mode, no fault pin
    TMR3 = 0; // clear timer
    OC3CONbits.OCTSEL = 0;
    OC3CONbits.ON = 1; // enable pwm
    T3CONbits.ON = 1; //enable timer

    // --- Output compare for red leds

    // init light
    RPB15R = 0b0101;
    // PWM
    OC1CONbits.ON = 0; // disable to change parameters
    PR2 = RED_PR; // period (timer threshold)
    OC1R = 0; // current duty cycle (readonly if non disabled)
    OC1RS = 0; // next duty cycle
    //OC1R = 25000;
    OC1CONbits.OCM = 0b110; // enable in pwm mode, no fault pin
    TMR2 = 0; // clear timer
    OC1CONbits.OCTSEL = 1;
    OC1CONbits.ON = 1; // enable pwm
    T2CONbits.ON = 1; //enable timer
}