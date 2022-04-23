import os
import sys
import time

os.system("clear")
os.system("figlet WebInfo")
print ("================================")
print ("Admin : RedSec")
print ("Team : LIT | IndoSecHax | Cardinal")
print ("Copyright © whois.com | redsec.6te.net")
print ("================================")
print
target = input("IP/Web Target ==> ")
print
print ("Wait Loading....")
print
time.sleep(3)
os.system("figlet Whois")
os.system (f" whois {target} ")
print
time.sleep(3)
os.system("figlet PortScan")
os.system(f" nmap {target} ")
