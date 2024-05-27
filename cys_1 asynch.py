import asyncio
import subprocess
import os

async def run_command(command):
    proc = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    if stderr:
        print(f"Error: {stderr.decode()}")
    return stdout.decode()

def fping(target_ip):
    command = f"fping -a -g {target_ip} > fping_output.txt"
    result = subprocess.run(command, shell=True)

    fping('192.168.1.0/24')

async def arpscan(target_ip):
    command_arping = f"sudo arp-scan --interface=eth0 --localnet > arping_output.txt"
    await run_command(command_arping)
    await main_intro(target_ip)

async def nmap_tcp(target_ip):
    command_nmap_tcp = f"sudo nmap -sP {target_ip} -oN nmap_tcp_output.txt"
    await run_command(command_nmap_tcp)
    await main_intro(target_ip)

async def nmap_udp(target_ip):
    command_nmap_udp = f"sudo nmap -sU {target_ip} -oN nmap_udp_output.txt"
    await run_command(command_nmap_udp)
    await main_intro(target_ip)

async def nmap_service(target_ip):
    command_nmap_service = f"sudo nmap -sV {target_ip} -oN nmap_service_output.txt"
    await run_command(command_nmap_service)
    await main_intro(target_ip)

async def nmap_port(target_ip):
    command_nmap_port = f"sudo nmap -p- {target_ip} -oN nmap_port_output.txt"
    await run_command(command_nmap_port)
    await main_intro(target_ip)

async def dirbuster(target_ip):
    user_dirbust_wordlist = "/var/share/wordlists/dirb/big.txt"
    command_dirbuster = f"sudo dirbuster -w {user_dirbust_wordlist} -url {target_ip}"
    await run_command(command_dirbuster)

async def main_intro(target_ip):
   #os.system("clear")
   print("")
   print("                        Stay Safe | Stay 127.0.0.1         ")
   print("   ")
   print("             _____              __   __      _       _ _   ")
   print("            |  __ \             \ \ / /     | |     (_) |  ")
   print("            | |__) |__ _ __ _____\ V / _ __ | | ___  _| |_ ")
   print("            |  ___/ _ \ '_ \______> < | '_ \| |/ _ \| | __|")
   print("            | |  |  __/ | | |    / . \| |_) | | (_) | | |_ ")
   print("            |_|   \___|_| |_|   /_/ \_\ .__/|_|\___/|_|\__|")
   print("                                      | |                  ")
   print("                                      |_|                  ")
   print("")
   print("                              fca124419                    ")
   print ("")
   print ("1. Visability: fping    | 2. Visability: arping    | 3. Visability: nmap TCP|")
   print ("4. Visability: nmap UDP | 5. Service: nmap         | 6. Ports: nmap         |")
   print ("7. Enum: Dirbuster      | 8. ---------             | 9. ------              |")
   print ("10. ----                | 11. ---------            | 12. ------             |")
   print("")
   user_dec = input("Please enter the number for the software to use: ")
   if user_dec == "1":
      await fping(target_ip)
   elif user_dec == "2":
      await arpscan(target_ip)
   elif user_dec == "3":
      await nmap_tcp(target_ip)
   elif user_dec == "4":
      await nmap_udp(target_ip)
   elif user_dec == "5":
      await nmap_service(target_ip)
   elif user_dec == "6":
      await nmap_port(target_ip)
   elif user_dec == "7":
      await dirbuster(target_ip)

async def main():
    new_folder = input("Please insert the name of the folder for the workspace: ")
    new_folder_command = f"sudo mkdir {new_folder}"
    await run_command(new_folder_command)
    target_ip = input("Please enter Target IP: ")
    await main_intro(target_ip)

asyncio.run(main())
