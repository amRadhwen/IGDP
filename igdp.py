import sys
import platform
import instaloader
from colorama import Fore, Back, Style


from instaloader.structures import Profile

system = platform.system()
version = platform.version()
machine = platform.machine()
platforme = platform.platform()
processor = platform.processor()

print("=========================================================")
print("_____.....------=====$$$$$ IGDP $$$$$=====-----....._____")
print("=========================================================")

print(Back.LIGHTWHITE_EX + Fore.BLACK + "\n-> System informations:" + Style.RESET_ALL)
print("--> System   : ", system)
print("--> Machine  : ", machine)
print("--> Platform : ", platforme)
print("--> Processor: ", processor)

print(Back.LIGHTWHITE_EX + Fore.BLACK + "\n-> Select profile visibility: " + Style.RESET_ALL)
print("--> 1- Public")
print("--> 2- Private")

profile_visibility = input("---> Profile visibility: ")
while profile_visibility not in ['1', '2']:
    profile_visibility = input("---> Profile visibility: ")

loader = instaloader.Instaloader()
username = None

if profile_visibility == '2':
    USER = input("-> Username: ")
    PASS = input("-> password: ")
    try:
        loader.login(USER, PASS)
        print("-> Connecting...")
        print(Fore.GREEN + "-> Connected :)" + Style.RESET_ALL)
        username = input("-> Username: ")
    except Exception as e:
        print(Fore.RED + e + Style.RESET_ALL)

if profile_visibility == '1':
    username = input("-> Username: ")

if not username:
    sys.exit()
else:
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except Exception as e:
        print(Fore.RED + e + Style.RESET_ALL)



