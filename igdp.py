from time import sleep
from sys import exit
import platform
import instaloader
from colorama import Fore, Back, Style
from __loader import Loader

def getStringInput(message):
    try:
        return input(message)
    except KeyboardInterrupt as ki:
        exit()
        print("\nBye !")

def loading(message):
    with Loader(message):
        for i in range(10):
            sleep(0.25)

print("====================================================================")
print("______......--------======$$$$$$ IGDP $$$$$$======------......______")
print("====================================================================")

found = False
while not found:
    username = getStringInput("Username: ")
    while not username:
        username = getStringInput("Username: ")

    loader = instaloader.Instaloader(save_metadata=False)


    try:
        loading("Searching...")
        profile = instaloader.Profile.from_username(loader.context, username)
        found = True
        connected = False

        #check if profile is private
        if profile.is_private:
            print("Account is Private !")
            print(Back.MAGENTA + "Login: " + Style.RESET_ALL)
            USER = getStringInput("USER: ")
            PASS = getStringInput("PASS: ")
            print("Connecting...")
            try:
                loader.login(USER, PASS)
                connected = True
            except Exception as e:
                print("inside the exception: "+Fore.RED + str(e) + Style.RESET_ALL)
        
        # profile informations
        if not profile.is_private or (profile.is_private and connected):
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

            print("\n->Downloading Posts...")
            print(profile.get_profile_pic_url())
            #for post in profile.get_posts():
            #    loader.download_post(post, target=profile.username)
        print(Fore.GREEN + "->Done " + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "!!! " +str(e) + Style.RESET_ALL)




