# Prompt user for their date of birth in YYYY-MM-DD format and print how old they are 
# in minutes, rounded to the nearest integer, using English words instead of numerals


from datetime import date
import sys
#from validator_collection import checkers
import inflect


def main():
    
    print(convert(input("Date of Birth: ")))


def convert(s):

    p = inflect.engine()
    try:
        result = date.fromisoformat(s)
        now = date.today()

        difference = now - result
        difference = round(int(difference.total_seconds()) / 60)

        words = p.number_to_words(difference, andword="")

    except ValueError:
        sys.exit("Invalid")

    return f"{words.capitalize()} minutes"



if __name__ == "__main__":
    main()