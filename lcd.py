#!/bin/python3

from RPLCD import i2c

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap, cols=cols, rows=rows)
lcd.backlight_enabled = True 
# Clear the LCD screen
lcd.close(clear=False)
# Write a string on first line and move to next line
while True:
        try:
            line = input()
            lcd.write_string(line)
            lcd.crlf()
        except EOFError:
            # no more information
            break