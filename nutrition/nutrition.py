# Get input from the user that consists of a fruit and output the calories of that fruit

def main():

    get_calories(input("Item: "))


def get_calories(fruit):

    calories = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80"
    }

    if fruit.lower() in calories:
        print("Calories: " + calories[fruit.lower()])


if __name__ == "__main__":
    main()