# Validate an IPv4 address.  Should be #.#.#.# with each number between 0 - 255



import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    validated = re.search(r"^\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\b\.\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\b\.\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\b\.\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\b$", ip.strip())

    if validated:
        return True
    
    else:
        return False



if __name__ == "__main__":
    main()