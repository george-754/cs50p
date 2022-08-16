# Open a csv file and output it in a table form

from tabulate import tabulate
import sys
import csv


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    print(tabulate(show_menu(sys.argv[1]), headers="firstrow", tablefmt="grid"))



def show_menu(menu):

    pizza = []

    try:
        with open(menu) as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append({"pizza": row[0], "small": row[1], "large": row[2]})

    except FileNotFoundError:
        sys.exit("File does not exist")

    return pizza



if __name__=="__main__":
    main()