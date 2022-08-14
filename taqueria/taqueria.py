# Get user input as item from a menu and output the total price. Keep looping until user hits ctrl-d


def main():

    order()


def order():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.00

    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu[item]

                print(f"${total:.2f}")

        except EOFError:
            print("\n", end="")
            break



if __name__== "__main__":
    main()