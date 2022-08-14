# Get user input as fractions and convert it to percentage. All while catching errors


def main():

    s = calculate("Fraction: ")
    print(s)


def calculate(s):

    while True:
        try:
            x, y = input(s).split("/")

            if int(y) >= int(x):
                a = (int(x) / int(y)) * 100
                
                if a <= 1:
                    return "E"
                elif a >= 99:
                    return "F"
                else:
                    return f"{round(a)}%"

        except (ValueError, ZeroDivisionError):
            pass


    


if __name__ == "__main__":
    main()