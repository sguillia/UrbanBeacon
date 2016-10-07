#include "urban.h"

extern u8  gps_buf[GPS_BUF_SIZE];
extern u16 gps_r;
extern u16 gps_w;
extern u8  uart_buf[UART_BUF_SIZE];
extern u16 uart_r;
extern u16 uart_w;
extern u8  errcode;
extern u8  mode;
extern u8  wp_num;
extern u8  wp_done;
extern urban_t  wp_data;

void get_waypoint(u8* buf, u8 index);

static void dump_eeprom(void)
{
    u16 tmp;
    eeprom_sendbyte(EEPROM_READ);
    eeprom_sendbyte(0);
    eeprom_sendbyte(0);
    for (tmp = 0; tmp < 1000; tmp++)
        serial_send(eeprom_sendbyte(0));
    eeprom_unselect();
    serial_send('*');
}

void clear_error_flag(void)
{
    errcode = 0;
    gps_led_mode(GPS_LED_OFF);
}

void    check_uart_input(void)
{
    static u8 count = 0;
    static u16 addr;
    u8 rxchar;

    if (uart_r != uart_w)
    {
        rxchar = uart_buf[uart_r];
        _nop();
        if (mode == MODE_PROGRAM)
        {
            if (count == 0)
            {
                if (rxchar >= STORAGE_SIZE)//----------------------------------------------------------
                {
                    error(E_ADDR_TOO_HIGH);
                    mode = MODE_DEFAULT;
                    return ;
                }
                addr = (u16)rxchar * STRUCT_SIZE;
                count++;
            }
            else
            {
                eeprom_write_byte(addr + count - 1, rxchar);
                count++;
                if (count == STRUCT_SIZE + 1)
                {
                    mode = MODE_DEFAULT;
                    if (WAYPOINT_FLASH_CONFIRM_DONE)
                        serial_send('$');
                }
            }
        }
        else if (mode == MODE_EMULATE)
        {
            if (rxchar == '#')
                mode = MODE_DEFAULT;
            else
            {
                gps_buf[gps_w] = rxchar;
                gps_w = (gps_w + 1) % GPS_BUF_SIZE;
            }
        }
        else if (mode == MODE_WP_NUM)
        {
            /*
             * Modifying wp_num always return 2 bytes :
             * 'ee' if wp_num is -1
             * '00' if wp_num if 0, '01' if wp_num is 1, ...
             * 'eW' if wp_num changing was succesful but does not match any existing waypoint
             * 'ok' if wp_num changing was succesful
             * '!!' if command was not understood (example : '!x' is invalid)
            */
            if (rxchar == '!')
            {
                if (wp_num == (u8)-1)
                {
                    serial_send('e');
                    serial_send('e');
                }
                else
                {
                    //serial_send(wp_num); // Sending null byte or something does terminate wxpy string
                    serial_send((wp_num / 10) + '0');
                    serial_send((wp_num % 10) + '0');
                }
            }
            else if (rxchar == '-')
            {
                wp_num = -1;
                serial_line("ok");
            }
            else if ((rxchar >= 0 && rxchar <= 30) || (rxchar >= 'A' && rxchar <= '_'))
            {
                // Input can be a raw byte, or an ascii printable character
                if (rxchar >= 'A' && rxchar <= '_')
                    rxchar -= 'A';
                urban_t wp;
                get_waypoint((u8*)&wp, rxchar);
                if (wp.active == 255)
                {
                    serial_line("eW"); // error :: Warning
                    //serial_line("WARNING: Wrong wp num");
                    //error(E_WRONG_WPNUM);
                }
                else
                    serial_line("ok");
                u8 old_wp_num = wp_num;
                wp_num = rxchar;
                wp_done = FALSE;
                eeprom_write_byte(CURRENT_WP_ADDR, wp_num);
                if (old_wp_num != (u8)-1)
                    get_waypoint((u8*)&wp_data, wp_num);
            }
            else
                serial_line("!!");
            mode = MODE_DEFAULT;
        }
        else if (rxchar == '$')
        {
            count = 0;
            mode = MODE_PROGRAM;
        }
        else if (rxchar == '*')
            dump_eeprom();
        else if (rxchar == '@')
        {
            serial_send('E');                       // Send error byte over serial
            serial_send(errcode + '0');
            serial_send(errcode);
        }
        else if (rxchar == '~')
            while(1);
        else if (rxchar == '!')
            mode = MODE_WP_NUM;
        else if (rxchar == '>')
            serial_send('<');
        else if (rxchar == '<')
            ;
        else if (rxchar == '(')
            enable_gps_rx();
        else if (rxchar == ')')
            disable_gps_rx();
        else if (rxchar == '#')
            mode = MODE_EMULATE;
        else if (rxchar == '/')
            clear_error_flag();
        else if (rxchar == 'R') // read status
           serial_send(eeprom_rdsr());
        else if (rxchar == 'E') // enable write enable
            eeprom_wren();
        else if (rxchar == 'D')
            eeprom_wrdi();
        
        // Debug
        else if (rxchar == '1') // Write
            eeprom_write_byte(0x0, 0b11001100);
        else if (rxchar == '2') // Read
        {
            u8 tmp = eeprom_read_byte(0);
            serial_send(tmp);
        }
        else if (rxchar == '3') // Write
            eeprom_write_byte(0x0, 0b10101010);


        else if (rxchar == '4')
        {
            urban_t test;
            get_waypoint((u8*)&test, 0);
            _nop();
            u8 tmp;
            for (tmp = 0; test.str[tmp]; tmp++)
                serial_send(test.str[tmp]);
            serial_send('.');
        }
        else if (rxchar == '5')
        {
            serial_send(sizeof(urban_t));
        }
        else if (rxchar == '6')
        {
            serial_send(eeprom_rdsr());
        }
        else if (rxchar == '7')
        {
            eeprom_wren();
        }

        else
            serial_send('?');
        uart_r = (uart_r + 1) % UART_BUF_SIZE;
    }
}
