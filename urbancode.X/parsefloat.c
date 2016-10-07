#include "urban.h"

float parse_float(u8 *str);

float parse_lat(u8 str[11])
{
    float degrees;
    float minutes;

    degrees = (float)((str[0] - '0') * 10 + (str[1] - '0'));
    minutes = (float) (parse_float(str + 2));
    minutes = minutes / 60.0;
    float result = (float)(degrees + minutes);
    return (result);
}

float parse_lon(u8 str[11])
{
    float degrees;
    float minutes;

    degrees = (float)((str[0] - '0') * 100 + (str[1] - '0') * 10 + (str[2] - '0'));
    minutes = (float) (parse_float(str + 3));
    return ((float)(degrees + minutes / 60));
}

float parse_float(u8 *str)
{
    float dec = 0.0;
    float comma = 0.0;
    float divider = 1.0;
    while (*str)
    {
        if (*str == '.')
        {
            str++;
            break;
        }
        dec = (dec * 10.0) + (*str - '0');
        str++;
    }
    if (!*str)
    {
        error(E_NOT_FLOAT);
        return (0.0);
    }
    _nop();
    while (*str)
    {
        comma = (comma * 10.0) + (*str - '0');
        divider *= 10.0;
        str++;
    }
    _nop();
    comma /= divider;
    return (dec + comma);
}