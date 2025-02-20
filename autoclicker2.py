from pyautogui import click,position 
from keyboard import is_pressed
from time import sleep
from threading import Event, Thread

click_event = Event()
fixed_position=None

def click_mouse():
    while click_event.is_set():
        click(fixed_position)
        sleep(0.1)

def start_clicking():
    global fixed_position
    if not click_event.is_set():
        fixed_position=position()
        click_event.set()
        Thread(target=click_mouse, daemon=True).start()

print("Tıklmayı başlatmak için E tuşuna basın.")
print("Tıklmayı başlatmak için X tuşuna basın.")

while True:
    if is_pressed("e"):
        start_clicking()
    if is_pressed("x"):
        click_event.clear()
        sleep(0.1)