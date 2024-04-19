import subprocess
import time
import os


print(os.system("ifconfig\n"))
print("----> Mac Changer <---- \n\n\n escolha uma das interfaces acima listadas \n" ) 

interfce = input("Enter the interface: ")

print(f"You selected {interfce} interface! \n")

new_mac = input("Enter the new mac address: ")
print("\n\n")

subprocess.call("ifconfig " + interfce + " down", shell=True )
print(f"shutdown interface {interfce}, wait...\n\n ")
subprocess.call(["ifconfig", interfce, "hw", "ether", new_mac])
print(f"switch to new mac: {new_mac}... \n\n")
subprocess.call("ifconfig " + interfce + " up", shell=True)
time.sleep(5)

print(os.system("ifconfig"))

