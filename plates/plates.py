# Check if custom vanity plates are valid or invalid
# Must start with atleast 2 letters
# Max of 6 characters and Min of 2 characters
# Numbers must come at the end and cannot start numbers with a 0
# No puctuation marks


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
#    if is_length_valid(s) == False:
#        return False
#
#    elif is_first_two_letters(s) == False:
#        return False
#
#    elif is_numbers_valid(s) == False:
#        return False

    return is_length_valid(s) and is_first_two_letters(s) and is_numbers_valid(s) and is_no_punctuation(s)

def is_length_valid(s):

    if len(s) >= 2 and len(s) <= 6:
        return True
    
    else:
        return False


def is_first_two_letters(s):
    
    return s[0:2].isalpha()


def is_numbers_valid(s):

    is_number_started = False

    for c in s:
        
        if is_number_started and c.isalpha():
            return False
        
        elif is_number_started == False and c == "0":
            return False

        elif is_number_started == False and c.isnumeric():
            is_number_started = True

    return True


def is_no_punctuation(s):

    return s.isalnum()


main()