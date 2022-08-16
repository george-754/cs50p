# Clean csv files data

import csv
import sys


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a valid CSV file")

    lst_students = get_data(sys.argv[1])
    clean_data(sys.argv[2], lst_students)



def get_data(orig_file):

    students = []

    try:
        with open(orig_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    return students



def clean_data(new_file, orig_list):

    with open(new_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for record in orig_list:
            last, first = record["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": record["house"]})



if __name__=="__main__":
    main()