# Get input from a user assume it is going to be an int and convert it to E = mc squared. input is for m
# E = energy, c = speed of light (approx. 300000000 meters per second)


def main():

    x = input("m: ")

    calculate(int(x))

def calculate(input):

    c = 300000000

    answer = input * pow(c, 2)

    print(f"E: {answer}")

main()
