# Math interpreter

def main():

    print(check(input("Expression: ")))


def check(expression):

    x, y, z = expression.split(" ")

    if y == "+":
        return float(int(x) + int(z))

    elif y == "-":
        return float(int(x) - int(z))

    elif y == "*":
        return float(int(x) * int(z))

    elif y == "/":
        return float(int(x) / int(z))

    else:
        return "Invalid"


main()