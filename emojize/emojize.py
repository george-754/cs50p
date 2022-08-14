# Get input from the user and convert it to an emoji with emoji package

import emoji


s = input("Input: ")
print("Output: " + emoji.emojize(s))