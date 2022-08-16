# Program to count lines of code in a python file excluding commented lines and blank lines

import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    line_count = count(sys.argv[1])
    print(line_count)


def count(fname):
    counter = 0
    try:
        with open(fname) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.lstrip() == "":
                    counter += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter



if __name__=="__main__":
    main()