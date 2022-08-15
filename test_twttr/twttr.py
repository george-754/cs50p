# Get input from a user and shorten it up by taking out the vowels A, E, I, O and U. Then output it to the screen
# ie. "Twitter" would then be "Twttr"

def main():

    print("Output: " + shorten(input("Input: ")))


def shorten(word):

    converted = ""
    vowels = ["a", "e", "i", "o", "u"]

    for c in word:
        if c.lower() not in vowels:
            converted += c

    return converted


if __name__ == "__main__":
    main()