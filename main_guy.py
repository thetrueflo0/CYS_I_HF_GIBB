import os

def nmap():
   user_nmap_target = input("Please enter the target IP: ")
   user_nmap_port = input("Please enter the port range: ")
   user_nmap_options = input("Please enter the options: ")
   user_nmap_output = input("Please enter the output file: ")
   
   command_nmap = "sudo nmap " + "-p " + user_nmap_port + " " + user_nmap_target + " " + user_nmap_options + " -oA " + user_nmap_output 
   
   os.system(command_nmap)
   
def dirbister():
   user_dirbust_target = input ("Please enter the target IP or Hostname")
   user_dirbust_wordlist = input ("Plese enter the wordlist file")
   
   command_dirbuster = "sudo dirbuster -w " + user_dirbust_wordlist + " " + user_dirbust_target
   os.system(command_dirbuster)

def sqlmap():
   user_sqlmap_target = input("Please enter the target IP: ")
   user_sqlmap_port = input("Please enter the port range: ")
   user_sqlmap_options = input("Please enter the options: ")
   user_sqlmap_output = input("Please enter the output file: ")
   
   command_sqlmap = "sudo sqlmap " + "-p " + user_sqlmap_port + " " + user_sqlmap_target + " " + user_sqlmap_options + " -oA " + user_sqlmap_output 
   
   os.system(command_sqlmap)

def searchexploit():
   user_searchexplit = input("Enter the exploit: ")
   
   command_searchexploit = "sudo searchsploit " + user_searchexplit
   os.system(command_searchexploit)

def main():
   os.system("clear")
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
   print("                  H4ck 1s a cR1m3               ")
   print ("")
   print ("1. Nmap               | 2. Dirbuster             | 3. SQLmap        |")
   print ("4. Searchesploit      | 5. WPScan                | 6. John          |")
   print ("7. Hydra              | 8. ---------             | 9. ------        |")
   print ("10. ----              | 11. ---------            | 12. ------       |")
   print("")
   user_dec = input("Please enter your choice: ")
   user_dec_ip = input("Please enter Target IP")
   
   if user_dec == "1":
      nmap()
   elif user_dec == "2":
      dirbister()
   elif user_dec == "3":
      sqlmap()
   elif user_dec == "4":
      searchexploit()
main()


   