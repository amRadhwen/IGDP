# imports 
from time import sleep
from sys import exit
import instaloader
from colorama import Fore, Back, Style
from instaloader.exceptions import ProfileNotExistsException
from __loader import Loader
from getpass import getpass


# get string input
def getStringInput(message):
    try:
        _input = input(message)
        while not _input:
            _input = input(message)
        return _input
    except KeyboardInterrupt as ki:
        print("\nBye !")
        exit()


# get hidden string (password)
def getStringinputHidden(message):
    try:
        print(message, end="")
        _inputHidden = getpass()
        while not _inputHidden:
            print(message, end="")
            _inputHidden = getpass()
        return _inputHidden
    except KeyboardInterrupt as ki:
        print("\nBye !")
        exit()

# start the loading thread
def loading(message):
    with Loader(message):
        for i in range(10):
            sleep(0.25)


# main screen header
print("=======================================================================")
print("______......--------======****** IGDP V1 ******======------......______")
print("=======================================================================")


loader = instaloader.Instaloader(save_metadata=False)
found = False
connected = False
session = False
while not found:
            
    username = getStringInput("Instagram Username: ")
    while not username:
        username = getStringInput("Instagram Username: ")

    try:
        loading("Searching...")
        profile = instaloader.Profile.from_username(loader.context, username)
        print("Found :)")
        found = True

        # check if profile is private (if yes login)
        if profile.is_private:
            try:
                loader.load_session_from_file(username="", filename="session")
                session = True
                connected = True
            except Exception as e:
                print(Fore.RED + "Cannot load session !" + Style.RESET_ALL)
                #print(Fore.RED + str(e) + "!!!" + Style.RESET_ALL)

            if not session:
                print("Account is Private !")
                print(Back.MAGENTA + "Login: " + Style.RESET_ALL)
                USER = getStringInput("USER: ")
                PASS = getStringinputHidden("PASS: ")
                try:
                    loading("Connecting...")
                    loader.login(USER, PASS)
                    print("Connected :)")
                    loader.save_session_to_file("session")
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

            # download posts
            print("\n->Downloading Posts...")
            try:
                for post in profile.get_posts():
                    print("inside downloader")
                    loader.download_post(post, target=profile.username)
                print(Fore.GREEN + "->Done " + Style.RESET_ALL)
            except KeyboardInterrupt:
                print("Download Interrupted !")
    except ProfileNotExistsException:
        print(Fore.RED + "Username " + username + " does not exists !" + Style.RESET_ALL);
    except Exception as e:
        print(Fore.RED + str(e) + "!!!" + Style.RESET_ALL)
