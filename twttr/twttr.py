# Get input from a user and shorten it up by taking out the vowels A, E, I, O and U. Then output it to the screen
# ie. "Twitter" would then be "Twttr"

def main():

    print("Output: " + convert(input("Input: ")))


def convert(user_input):

    converted = ""

    for c in user_input:
        if c != "a" and c != "A" and c != "e" and c != "E" and c != "i" and c != "I" and c != "o" and c != "O" and c != "u" and c != "U":
            converted += c

    return converted


if __name__ == "__main__":
    main()