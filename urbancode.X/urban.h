#include <xc.h>
#include <sys/attribs.h>
#include "types.h"

// -------- General purpose defines
#define INPUT           1
#define OUTPUT          0
#define HIGH            1
#define LOW             0
#define RISE            1
#define FALL            0
#define TRUE            1
#define FALSE           0

// -------- Timer related defines

/*
 * Frequency calculation. See "Oscillators" reference manual.
 * Secondary Oscillator is 32.768 Khz and is selected by T1CON.TCS
*/
/*
#define DELAY_1000_MS   256 * 8 * 16 / 4
#define DELAY_500_MS    256 * 8 * 8  / 4
#define DELAY_250_MS    256 * 8 * 4  / 4
#define DELAY_125_MS    256 * 8 * 2  / 4
#define DELAY_62_MS     256 * 8 * 1  / 4
*/
#define DELAY_1000_MS   62500
#define DELAY_500_MS    31250
#define DELAY_250_MS    15625
#define DELAY_125_MS    7812    // Lost of precision here
#define DELAY_62_MS     3906

// -------- GPS LED
#define GPS_LED_OFF                 0x0
#define GPS_LED_ON                  0x1
#define GPS_LED_BLINK_SLOW          0x2
#define GPS_LED_BLINK_FAST          0x3
#define GPS_LED_BLINK_SLOW_TICKS    8
#define GPS_LED_BLINK_FAST_TICKS    1

// -------- GPS COM
#define GPS_BUF_SIZE                512
#define WAIT_DOLLAR                 0x1
#define WAIT_TYPE                   0x2
#define BUFFER_GPRMC                0x3
#define BUFFER_GPGGA                0x4

// -------- EEPROM
#define UART_BUF_SIZE               512
#define EEPROM_WREN                 0b0110
#define EEPROM_WRDI                 0b0100
#define EEPROM_RDSR                 0b0101
#define EEPROM_WRSR                 0b0001
#define EEPROM_READ                 0b0011
#define EEPROM_WRITE                0b0010

// -------- UART
#define MODE_DEFAULT                0x1
#define MODE_PROGRAM                0x2
#define MODE_EMULATE                0x3
#define MODE_WP_NUM                 0x4

// -------- ERRORS
#define E_UART_BUF_OVERRUN          0x1
#define E_UART_BIGBUF_OVERRUN       0x2
#define E_GPS_BUF_OVERRUN           0x3
#define E_GPS_BIGBUF_OVERRUN        0x4
#define E_EMPTY_SATNUM              0x5
#define E_INVALID_SATNUM1           0x6
#define E_INVALID_SATNUM2           0x7
#define E_NOT_FLOAT                 0x8
#define E_ADDR_TOO_HIGH             0x9
#define E_NO_WAYPOINT               0xA
#define E_ABS_OVERLIMIT             0xB
#define E_ABS_UNDERLIMIT            0xC
#define E_NO_ACTIVE_WAYPOINT        0xD
#define E_DEVELOPER_IS_SHIT         0xE
#define E_WRONG_WPNUM               0xF

// -------- MEMORY
#define STRUCT_SIZE                 32      // Taille de la structure trame_s
#define STORAGE_SIZE                31      // Nombre maximum de structures, a partir de 1

// -------- RANDOM
#define WAYPOINT_FLASH_CONFIRM_DONE 1       // Confirmer un octet flashe en renvoyant un '$'

// -------- LEDS
#define BLUE_PR                     600
#define RED_PR                      600

// -------- GAME
#define GAME_TIMER_DELAY            1       // Seconds
#define GPS_INPUT_BUFFER_SIZE       5       // Consider average of N last gpgga positions
#define FURTHEST_POINT_PCT          1.1     // At wp init, furthest point is current distance from wp * percentage
                                            // So absolute color is not blue at beginning
#define GPS_TIMEOUT                 15
#define GOAL_RADIUS                 1.0     // n / 10000.0 degrees
#define DIST_STATIONARY             0.09     //If user stops // n / 10000.0 degrees
#define CURRENT_WP_ADDR             999     // This is the last byyyyyte
#define WP_MAX_TICKS                4
#define ERASE_DELAY                 6

typedef struct  urban_s
{
    float lat;
    float lon;
    float alt;
    u8 str[19];
    u8 active;
}               urban_t;

typedef struct  gps_coord_s
{
    float lat;
    float lon;
    float alt;
}               gps_coord_t;


float parse_lat(u8 str[11]);
float parse_lon(u8 str[11]);
float distance(gps_coord_t *a, gps_coord_t *b);
float fuckoff_abs(float x);
float close_enough(float x, float g);
float better_guess(float a, float b);
float test(float x, float g);
float sqrt(float x);
float fuckoff_hypot(float x, float y);
u8 get_next_active_wp_id(u8 from);
void erase_all_waypoints(void);
void set_leds_pct(u8 pct);