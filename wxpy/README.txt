A GUI interface to flash the waypoints from Google maps to the UrbanBeacon device

This was my second project in Python. I haven't documented it at the time.

Pictures to come. The program uses wxpython library.

Some code snippets and icons came from google / stack overflow / etc. It is impossible to me to get back to their author. If there is a copyright problem, contact me, I'll remove the content.




editor.py
Panel to edit waypoints

grumpycat.py
Panel to throw 'Unimplemented feature' error

map_panel.py
Browser panel

notebook.py
The notebook panel and tabs

test.py
Main app

unpack.py
Serial data unpacker

urban.py
Class for serial handling

utils.py
Utils : nmea, gps, images, buttons, ...

::: List of functionalities :::

Connect / Disconnect
Refresh serial list
Test serial connection

Show GPS points
Dump eeprom
See in map

New point
Delete point
Change point

Erase all (delete ID)
Erase all (overwrite eeprom)
Recovery

Download points
Upload points

Export as txt or binary file
Import as txt or binary file

GPS position emulator

Get errcode
About
