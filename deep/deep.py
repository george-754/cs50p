# Promt user for an answer and if the answer is 42, fort two, forty-two output yes otherwise no

def main():

    print(check(input("What is the answer to the Great Question of Life, the Universe and Everything? ")))


def check(answer):

    answer = answer.strip()
    answer = answer.lower()

    if answer == "42" or answer == "forty two" or answer == "forty-two":
        return "Yes"

    else:
        return "No"


main()