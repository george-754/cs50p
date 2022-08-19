# Validate an email address using "validator-collection"

from validator_collection import checkers


def main():

    print(validate_email(input("What's your email address? ")))



def validate_email(s):

    is_email_address = checkers.is_email(s)
    if is_email_address:
        return "Valid"

    else:
        return "Invalid"


if __name__ == "__main__":
    main()