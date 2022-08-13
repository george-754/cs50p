# Promt user for input.  If input starts with "hello" then output $0, or starts with "h" then output $20 otherwise output $100

def main():

    print(check(input("Greeting: ")))


def check(greeting):

    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return "$0"
    
    elif greeting.startswith("h"):
        return "$20"

    else:
        return "$100"


main()
