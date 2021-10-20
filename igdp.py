# before all instaloader module contains profile visibility check
# means so you don't need to get profile visibility input form users in the beginngin of the script
# so this will be the next correction
from sys import exit
import platform
import instaloader
from colorama import Fore, Back, Style


system = platform.system()
version = platform.version()
machine = platform.machine()
platforme = platform.platform()
processor = platform.processor()

print("====================================================================")
print("______......--------======$$$$$$ " + Back.BLUE+ Fore.WHITE +"IGDP" + Style.RESET_ALL +" $$$$$$======------......______")
print("====================================================================")

try:
    username = input("\nUsername: ")
except KeyboardInterrupt as ki:
    exit()
    print("\nBye !")

while not username:
    username = input("Username: ")


loader = instaloader.Instaloader()

try:
    print("--> Searching...")
    profile = instaloader.Profile.from_username(loader.context, username)

    if profile.is_private:
        pass
    
    # profile informations
    else:
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



