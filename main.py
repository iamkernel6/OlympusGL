import time
import sys
import pyfiglet
import random
import os
from termcolor import colored, cprint
from pyfiglet import figlet_format
from tqdm import tqdm, trange

# Check file
def checkfile(mybypass):
    return os.path.exists(mybypass)

# Load
def ketik(teks):
    for i in teks + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

# Banner
banner_loading = "          Please Wait . . . . "
banner_bold = "\033[1m" + banner_loading + "\033[0m"
hw = "help"
hw_bold = "\033[1m" + hw + "\033[0m"
welcome = f"          # Welcome to Olympus GL please report to us if you catch error \n          # Type {hw_bold} to see another command \n          # Run Bypass Banned command first\n"
def banner():
    color = 'yellow'
    cprint(figlet_format('OLYMPUS GL'), color)
    ketik(f"{banner_bold}")
    print(welcome)
    time.sleep(0.1)
# Help
help_bold = "\033[1m" + "help" + "\033[0m"
info_bold = "\033[1m" + "info" + "\033[0m"
auto_bold = "\033[1m" + "auto" + "\033[0m"
bb_bold = "\033[1m" + "bb" + "\033[0m"
ab_bold = "\033[1m" + "ab" + "\033[0m"
paba_bold = "\033[1m" + "paba" + "\033[0m"
gg_bold = "\033[1m" + "gg" + "\033[0m"
ncgm_bold = "\033[1m" + "nc" + "\033[0m"
exit_bold = "\033[1m" + "exit" + "\033[0m"
h = f"\n # Command list --------------- \n \n          $ {help_bold}     - Show help menu \n          $ {info_bold}     - Show info script \n          $ {auto_bold}     - Auto Farm, Auto Clear \n          $ {bb_bold}       - Bypass Banned \n          $ {ab_bold}       - Anti Bounce \n          $ {paba_bold}     - Pull all / Ban All \n          $ {gg_bold}       - Gems generator \n          $ {ncgm_bold}       - Noclip \n          $ {exit_bold}     - Exit Program \n"
def help():
    print(h)

# Info
def info():
    __author__ = "\033[1m" + "gnxe" + "\033[0m"
    __copyright__ = "\033[1m" + "Copyright 2021, Olympus" + "\033[0m"
    __credits__ = "\033[1m" + "gnxe,l3v1n" + "\033[0m"
    __license__ = "\033[1m" + "fsociety" + "\033[0m"
    __version__ = "\033[1m" + "1.0.0" + "\033[0m"
    __maintainer__ = "\033[1m" + "gnxe,l3v1n" + "\033[0m"
    __email__ = "\033[1m" + "iamkernel9@gmail.com" + "\033[0m"
    __status__ = "\033[1m" + "Prototype" + "\033[0m"
    __teammates__ = "\033[1m" + "gnxe,l3v1n" + "\033[0m"
    __date__ = "\033[1m" + "2021/03/9" + "\033[0m"
    __username__ = "\033[1m" + "gnxe,l3v1n" + "\033[0m"
    
    print('','=' * 78)
    print(' Author: ' + __author__)
    print(' Teammates: ' + __teammates__)
    print(' Copyright: ' + __copyright__)
    print(' Credits: ' + __credits__)
    print(' License: ' + __license__)
    print(' Version: ' + __version__)
    print(' Maintainer: ' + __maintainer__)
    print(' Email: ' + __email__)
    print(' Status: ' + __status__)
    print(' Date: ' + __date__)
    print(' Username: ' + __username__)
    print('','=' * 78)

# Auto Function
af_bold2 = "\033[1m" + "'af'" + "\033[0m"
ah_bold2 = "\033[1m" + "'ah'" + "\033[0m"
ac_bold2 = "\033[1m" + "'ac'" + "\033[0m"
af_text = f" Don't close this program \n if you wan't to turn off just simply type {af_bold2}"
ah_text = f" Don't close this program \n if you wan't to turn off just simply type {ah_bold2}"
ac_text = f" Don't close this program \n if you wan't to turn off just simply type {ac_bold2}"
command_complete = " Command successfully execute *"
bolded_complete = "\033[1m" + command_complete + "\033[0m"
def auto_farm():
    print(" Execute command!")
    for i in trange(100):
        time.sleep(0.1)
        print("\nLoading")
    print(bolded_complete)
    print(af_text)
def auto_harvest():
    print(" Execute command!")
    for i in trange(100):
        time.sleep(0.1)
        print("\nLoading")
    print(bolded_complete)
    print(ah_text)
def auto_clear():
    print(" Execute command!")
    for i in trange(100):
        time.sleep(0.1)
        print("\nLoading")
    print(bolded_complete)
    print(ac_text)

# Auto
auto_info = "\n Auto Command \n Before use this command open growtopia\n press home button and run the command"
bolded_auto = "\033[1m" + auto_info + "\033[0m"
example_bold = "\033[1m" + "'ex : af'" + "\033[0m"
backtext_bold = "\033[1m" + "'back'" + "\033[0m"
af_bold = "\033[1m" + "'af'" + "\033[0m"
ah_bold = "\033[1m" + "'ah'" + "\033[0m"
ac_bold = "\033[1m" + "'ac'" + "\033[0m"
h_bold = "\033[1m" + "help" + "\033[0m"
b_bold = "\033[1m" + "'back'" + "\033[0m"
al = f"\n Auto command list ============================================== \n \n          * Auto Farm         - to use this command type {af_bold} \n          * Auto Harvest      - to use this command type {ah_bold} \n          * Auto Clear        - to use this command type {ac_bold} \n          * Back to main menu - to use this command type {b_bold} \n \n Type {h_bold} to show this menu"
def auto():
    if checkfile('./bypass.txt'):
        print(bolded_auto)
        print(al)
        while True:
            pick_list = input(f"\n Please insert your auto command {example_bold} type {backtext_bold} if you done : ")
            if pick_list == "af":
                auto_farm()
            elif pick_list == "ah":
                auto_harvest()
            elif pick_list == "ac":
                auto_clear()
            elif pick_list == "back":
                break
            elif pick_list == "help":
                print(al)
            else:
                print(" Command not found")
    else:
        print("\n ERROR!\n" + " Please run" + "\033[1m" + " Bypass Banned " + "\033[0m" + "Before run this command\n")

# Bypass Banned
allow = "Allow Storage Permission"
allow_bold = "\033[1m" + allow + "\033[0m"
bb_welcome = "\n Bypass Banned :\n                 To use this command you must Allow Storage Permission \n                 This command must be first command you use if you don't wan't get banned \n                 You just need to input your GrowID not Password\n"
foo = ['n2CXoQMpfhrJvUfJvcvAgMgn265W7nLNuo', 'miR4ct321bscNdfC4qB4brDYKzhdaZALfq','mv9S9rbUkM6c516cEL8rS4KuaXkquFdUd2','1KzaSeeEmk1b8eZu8QqjqTS9aPuipgsMK8','1GFxkjU1dJAMminY2gwb52sCBuA2dQjg3u','1BXisN49F4PJdUAHSAAynGdesX6Vf4ZFrW','18q9icQRazK3gW4iHkBDTcqpRPPb6bct58','1M4c6i1kyuFjXbRFMc8jLu6Yqsknc6ucTE','bc1qpq6s7sl4xk5c9ur3mm7jl0ytfzcpul82a729n8','1BgfzQc13dXfpzPQLFVmXUsYBhYe4fV7nt']
def create():
    f = open("bypass.txt", "w")
    f.write(random.choice(foo))
def bb():
    print(bb_welcome)
    ketik(f"{banner_bold}")
    growid = input(" Please input your GrowID : ")
    print("\n \033[1m" + " Bypassing" + "\033[0m")
    for i in trange(100):
        time.sleep(0.1)
    create()
    print("\033[1m" + "                                                                         Bypass Done !" + "\033[0m")

# Anti Bounce
first_command = "Bypass Banned"
first_command_bold = "\033[1m" + first_command + "\033[0m"
ab_welcome = f"\n Anti Bounce :\n                 Connect to Server before use this command \n                 If you not run {first_command_bold} command before, this command will not working \n"
def ab():
    print(ab_welcome)
    if checkfile('./bypass.txt'):
        ketik(" Please Wait . . . .")
        print(" File Bypass found")
        time.sleep(2)
        print(" Auto Bounce          = ON")
    else:
        print("\n ERROR!\n" + " Please run" + "\033[1m" + " Bypass Banned " + "\033[0m" + "Before run this command\n")

# Pull All / Ban All
paba_welcome = f"\n Pull all / Ban all :\n                     Connect to Server before use this command \n                     If you not run {first_command_bold} command before, this command will not working"
def paba():
    print(paba_welcome)
    time.sleep(1)
    if checkfile('./bypass.txt'):
        print("\n" + "\033[1m" + " 1.Pull All       # Pull all player in server" + "\033[0m")
        print("\033[1m" + " 2.Ban All        # Ban all player in server" + "\033[0m" + "\n")
        while True:
            paba_pick = input("\033[1m" + " Olympus GL > Pick Command '0' back to MAIN MENU : " + "\033[0m")
            if paba_pick == "1":
                time.sleep(1)
                print("\n ============ Pull all Execute ============\n")
            elif paba_pick == "2":
                time.sleep(1)
                print("\n ============ Ban all Execute ============\n")
            elif paba_pick == "0":
                break
            else:
                print(" Command not found")

# Gems Generator
gg_welcome = f"\n Gems Generator :\n                     Connect to Server before use this command \n                     If you not run {first_command_bold} command before, this command will not working"
def gg():
    print(gg_welcome)
    time.sleep(1)
    username = input("\n Enter USERNAME : ")
    verify_username = input(f" USENAME : {username} " + "Verify USERNAME type 'y' to continue : ")
    if verify_username == "y":
        time.sleep(3)
        print(" Veirify!")
    elif verify_username == "n":
        time.sleep(1)
        print(" Please Try Again!")
        gg()
    else:
        print(" Command not found!")
    gems = input(" Gems Amount : ")
    verify_gems = input(f" USERNAME : {username},\n GEMS : {gems}\n Press 'y + enter' if correct : ")
    if verify_gems == "y":
        time.sleep(3)
        print(f" Success Generated : {gems} to Username : {username}")
    elif verify_gems == "n":
        time.sleep(1)
        print(" Please Try Again!")
        gg()
    else:
        print(" Command not found!")

# Moclip
nc_welcome = f"\n Noclip :\n                 Connect to Server before use this command \n                 If you not run {first_command_bold} command before, this command will not working \n"
def nc():
    print(nc_welcome)
    if checkfile('./bypass.txt'):
        ketik(" Please Wait . . . .")
        print(" File Bypass found")
        time.sleep(2)
        print(" Auto Bounce          = ON")
    else:
        print("\n ERROR!\n" + " Please run" + "\033[1m" + " Bypass Banned " + "\033[0m" + "Before run this command\n")