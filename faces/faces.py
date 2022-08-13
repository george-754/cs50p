# Get input from the user and convert :) and :( to their corresponding faces or emoji's

def main():
    txt = input()

    convert(txt)

def convert(input):
    
    converted = input.replace(":)", "🙂")

    converted = converted.replace(":(", "🙁")

    print(converted)


main()
    

