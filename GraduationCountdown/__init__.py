import time
from datetime import datetime

import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio
import RPi.GPIO as GPIO

# BCM PINS
# RS - 18
# EN - 23
# D4 - 24
# D5 - 25
# D6 - 8
# D7 - 7

# LCD Pin Constants - BCM Numbering
lcd_rs = digitalio.DigitalInOut(board.D18)
lcd_en = digitalio.DigitalInOut(board.D23)
lcd_d4 = digitalio.DigitalInOut(board.D24)
lcd_d5 = digitalio.DigitalInOut(board.D25)
lcd_d6 = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D7)
BACKLIGHT = 5

# LCD Size
LCD_COLUMNS = 16
LCD_ROWS = 2


# Button Pins - BCM Numbering
RED_BUTTON = 22
BLUE_BUTTON = 27
GREEN_BUTTON = 17

BACKLIGHT_STATUS = True
GRAD_DAY = datetime(2020, 5, 29)


def fmt_delta(delta):
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{days} Days {hours:02d}:{minutes:02d}:{seconds:02d}"


def toggle_backlight(event):
    global BACKLIGHT_STATUS
    BACKLIGHT_STATUS = not BACKLIGHT_STATUS
    GPIO.output(BACKLIGHT, BACKLIGHT_STATUS)


def safe_exit():
    lcd.clear()
    lcd.message = "Goodbye!"
    time.sleep(2)
    GPIO.output(BACKLIGHT, False)
    lcd.clear()
    exit(0)


def main():
    # Initialize the buttons
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Backlight Toggle
    GPIO.setup(BACKLIGHT, GPIO.OUT)
    GPIO.output(BACKLIGHT, BACKLIGHT_STATUS)
    GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback=toggle_backlight)

    # Initialize the lcd object
    global lcd
    lcd = characterlcd.Character_LCD_Mono(
        lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, LCD_COLUMNS, LCD_ROWS
    )
    lcd.clear()

    while True:
        today = datetime.now()
        delta = GRAD_DAY - today
        delta = fmt_delta(delta)

        lcd.message = delta + "\nUntil freedom :D"
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        safe_exit()
