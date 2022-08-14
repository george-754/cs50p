# Simulate a coke machine.  Display amount due and get input from the user as insert coin as an integer whereas the user can
# only insert 5, 10, 25 cents. Drinks cost 50 cents. Stop the program once enough change has been inserted displaying the amount owed.

def main():
    
    start_transaction()


def start_transaction():

    amount_due = 50

    while True:
        print(f"Amount Due: {amount_due}")
        
        inserted_coin = input("Insert Coin: ")
        if int(inserted_coin) == 5 or int(inserted_coin) == 10 or int(inserted_coin) == 25:
            amount_due -= int(inserted_coin)

        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            break


if __name__ == "__main__":
    main()