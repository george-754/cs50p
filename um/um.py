# Count how many times "um" appears in a str case-insensitively as a word itself not a substring of a word

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    t = re.findall(r"\bum\b", s, re.I)

    return int(len(t))




if __name__ == "__main__":
    main()