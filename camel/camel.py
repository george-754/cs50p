# Get users input as camelCase and output it as snake_case

def main():
    
    print("snake_case: " + convert(input("camelCase: ")))


def convert(camelCase):

    snake = ""
    for c in camelCase:
        if c.isupper():
            snake += "_"
            snake += c.lower()
        else:
            snake += c

    return snake


if __name__ == "__main__":
    main()