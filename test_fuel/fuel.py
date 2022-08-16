# Get user input as fractions and convert it to percentage. All while catching errors


def main():

    fraction = convert(input("Fracton: "))
    s = gauge(fraction)

    print(s)


def convert(fraction):

    x, y = fraction.split("/")

    if int(y) <= 0:
        raise ZeroDivisionError

    elif int(x) > int(y):
        raise ValueError

    else:
        a = (int(x) / int(y)) * 100
        a = round(a)

        return int(a)



def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()