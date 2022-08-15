# Game of professor. Output math problems


import random

x = []
y = []

def main():
    
    score = 0
    wrong = 0
    question = 0
    right_answer = 0

    get_level()
    
    while True:
        try:
            if question < 10:
                answer = int(input(f"{x[question]} + {y[question]} = "))
                right_answer = x[question] + y[question]
                
                if answer == right_answer:
                    score += 1
                    question += 1
                else:
                    raise ValueError
            else:
                break

        except ValueError:
            print("EEE")
            wrong += 1
            if wrong >= 3:
                print(f"{x[question]} + {y[question]} = {right_answer}")
                question += 1
                wrong = 0

    print(f"Score: {score}")



def get_level():
    
    while True:
        try:
            level = int(input("Level: "))
            
            if int(level) < 1 or int(level) > 3:
                raise ValueError

            else:
                break

        except ValueError:
            pass

    for _ in range(10):
        x.append(generate_integer(level))
        y.append(generate_integer(level))



def generate_integer(level):

    if level == 1:
        xy_min = 0
        xy_max = 9
    
    elif level == 2:
        xy_min = 10
        xy_max = 99

    elif level == 3:
        xy_min = 100
        xy_max = 999

    return random.randint(xy_min, xy_max)        
    


if __name__ == "__main__":
    main()