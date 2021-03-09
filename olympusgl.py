import main
import time
main.banner()
end = " Good Bye :)"
end_bold = "\033[1m" + end + "\033[0m"
h = "help"
h_bold = "\033[1m" + h + "\033[0m"
while True:
    cmd = input("\033[1m" + " Olympus GL > " + "\033[0m")
    if cmd == "help":
        main.help()
    elif cmd == "info":
        main.info()
    elif cmd == "auto":
    	main.auto()
    elif cmd == "bb":
        main.bb()
    elif cmd == "ab":
        main.ab()
    elif cmd == "paba":
        main.paba()
    elif cmd == "gg":
        main.gg()
    elif cmd == "nc":
        main.nc()
    elif cmd == "exit":
        print(end_bold)
        break
    else:
        print(f" Command not found type {h_bold} to see command line")
