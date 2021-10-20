# before all instaloader module contains profile visibility check
# means so you don't need to get profile visibility input form users in the beginngin of the script
# so this will be the next correction
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

print("====================================================================")
print("______......--------======$$$$$$ " + Back.BLUE+ Fore.WHITE +"IGDP" + Style.RESET_ALL +" $$$$$$======------......______")
print("====================================================================")

print(Back.LIGHTWHITE_EX + Fore.BLACK + "\n-> System informations:" + Style.RESET_ALL)
print("--> System   : ", system)
print("--> Machine  : ", machine)
print("--> Platform : ", platforme)
print("--> Processor: ", processor)

print(Back.LIGHTWHITE_EX + Fore.BLACK + "\n-> Select profile visibility: " + Style.RESET_ALL)
print("--> 1- Public")
print("--> 2- Private")

try:
    profile_visibility = input("---> Profile visibility: ")
except KeyboardInterrupt as ki:
    print("\nBye !")
    sys.exit()

while profile_visibility not in ['1', '2']:
    try: 
        profile_visibility = input("---> Profile visibility: ")
    except KeyboardInterrupt as ki:
        print("\nBye !")
        sys.exit()

loader = instaloader.Instaloader()
username = None

if profile_visibility == '2':
    try:
        USER = input("-> Username: ")
        PASS = input("-> password: ")
    except KeyboardInterrupt as ki:
        print("\nBye !")
        sys.exit()
    try:
        print("--> Connecting...")
        loader.login(USER, PASS)
        print(Fore.GREEN + "---> Connected :)" + Style.RESET_ALL)
        try:
            username = input("-> Username: ")
        except KeyboardInterrupt as ki:
            print("\nBye !")
            sys.exit()

    except Exception as e:
        print(Fore.RED + "!!! " +str(e) + Style.RESET_ALL)

if profile_visibility == '1':
    try:
        username = input("-> Username: ")
    except KeyboardInterrupt as ki:
        print("\nBye !")
        sys.exit()

if not username:
    print("Bye !")
    sys.exit()
else:
    try:
        print("--> Searching...")
        profile = instaloader.Profile.from_username(loader.context, username)
        # profile informations
        print("\nFull name    : ", profile.full_name)
        print("User ID      : ", profile.userid)
        print("Followees    : ", profile.followees)
        print("Followers    : ", profile.followers)
        print("Biography    : ", end=" ")
        for i in profile.biography:
            if ord(i) == 10:
                print(" ", end="")
            else:
                print(i, end="")
        print("\n")

        print("\->Downloading Posts...")
        for post in profile.get_posts():
            loader.download_post(post, target=profile.username)
        print(Fore.GREEN + "->Done " + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "!!! " +str(e) + Style.RESET_ALL)



