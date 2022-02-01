from time import sleep
from sys import exit
import instaloader
from colorama import Fore, Back, Style
from __loader import Loader
from getpass import getpass


def getStringInput(message):
    try:
        _input = input(message)
        while not _input:
            _input = input(message)
        return _input
    except KeyboardInterrupt as ki:
        print("\nBye !")
        exit()


def getStringinputHidden(message):
    try:
        print(message, end="")
        _inputHidden = getpass()
        while not _inputHidden:
            print(message, end="")
            _inputHidden = getpass()
    except KeyboardInterrupt as ki:
        print("\nBye !")
        exit()


def loading(message):
    with Loader(message):
        for i in range(10):
            sleep(0.25)


print("=======================================================================")
print("______......--------======$$$$$$ IGDP V1 $$$$$$======------......______")
print("=======================================================================")

found = False
while not found:
    username = getStringInput("Instagram Username: ")
    while not username:
        username = getStringInput("Instagram Username: ")

    loader = instaloader.Instaloader(save_metadata=False)

    try:
        loading("Searching...")
        print("Found :)")
        profile = instaloader.Profile.from_username(loader.context, username)
        found = True
        connected = False

        # check if profile is private
        if profile.is_private:
            print("Account is Private !")
            print(Back.MAGENTA + "Login: " + Style.RESET_ALL)
            USER = getStringInput("USER: ")
            PASS = getStringinputHidden("PASS: ")
            try:
                loading("Connecting...")
                loader.login(USER, PASS)
                print("Connected :)")
                connected = True
            except Exception as e:
                print(Fore.RED + str(e) + Style.RESET_ALL)

        # profile informations
        if not profile.is_private or (profile.is_private and connected):
            print("\nFull name    : ", profile.full_name)
            print("User ID      : ", profile.userid)
            print("Followees    : ", profile.followees)
            print("Followers    : ", profile.followers)
            print("Posts        : ", profile.mediacount)
            print("Biography    : ", end=" ")
            for i in profile.biography:
                if ord(i) == 10:
                    print(" ", end="")
                else:
                    print(i, end="")

            print("\n->Downloading Posts...")
            for post in profile.get_posts():
                loader.download_post(post, target=profile.username)
            print(Fore.GREEN + "->Done " + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e) + "!!!" + Style.RESET_ALL)
