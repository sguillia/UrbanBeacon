Project source code for PIC32MX150F128B

Developed using MPLABX & ICD3

Important files are :
	- urban.h: summary
	- main.c:  all globals
	- check_gps_input.c: NMEA parser (without checksum)
	- game_timer.c: main game calculations

The purpose of the game is to find treasures (waypoints) using red/blue LEDs, that become red when you're approaching the goal, blue when your're getting away.

When you are not moving, led percentage (red ~ blue) represents absolute percentage between goal and furthest point you've been.
When you are moving, led percentage represents if you are moving in the right direction.
