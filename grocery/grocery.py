# Make a list.  Get user input of items and add the items to a dict then output the items in alphabetical order with the quantities of each item


def main():

    item_list()


def item_list():

    items = {}

    while True:
        try:
            item = input("").upper()

            # if item is not in the dictianary yet then add it with a quantity of 1. If it exists then add 1 to the quantity
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1

        except EOFError:
            print("") # skip a line
            for item in sorted(items):
                print(items[item], item)
            break

        except KeyError:
            pass


if __name__ == "__main__":
    main()