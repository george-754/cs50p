# Get input from the user and use the figlet package to output the text to the screen


from pyfiglet import Figlet

import sys


figlet = Figlet()

if len(sys.argv) > 3:
    sys.exit("Invalid Usage")

if len(sys.argv) == 2:
    sys.exit("Invalid Usage")
    
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        
        f = figlet.getFonts()

        if sys.argv[2] in f:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid Usage")

    else:
        sys.exit("Invalid Usage")

s = input("Input: ")

print(figlet.renderText(s))