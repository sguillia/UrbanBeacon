#include "urban.h"

float distance(gps_coord_t *a, gps_coord_t *b)
{
    float delta_lat;
    float delta_lon;
    float dist;

    delta_lat = a->lat - b->lat;
    delta_lon = a->lon - b->lon;
    _nop();
    dist = fuckoff_hypot(delta_lat, delta_lon);
    //dist = delta_lat + delta_lon;
    _nop();
    return(dist);
}