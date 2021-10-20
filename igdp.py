import sys
import instaloader
import platform

system = platform.system()
version = platform.version()
machine = platform.machine()
platforme = platform.platform()
processor = platform.processor()

print("=========================================================")
print("_____.....------=====$$$$$ IGDP $$$$$=====-----....._____")
print("=========================================================")

print("\n-> System informations:")
print("--> System   : ", system)
print("--> Machine  : ", machine)
print("--> Platform : ", platforme)
print("--> Processor: ", processor)

profile_visibility = input("Profile visibility(public/private): ")
while profile_visibility not in ["public", "private"]:
    profile_visibility = input("Profile visibility(public/private): ")

loader = instaloader.Instaloader()
username = None

if profile_visibility == "private":
    USER = input("Username: ")
    PASS = input("password: ")
    loader.login(USER, PASS)

if profile_visibility == "public":
    username = input("Username: ")

if not username:
    sys.exit()



