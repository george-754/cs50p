# Get user input for names and add them to a list until the user escapes out with ctrl-d then output
# To screen with inflict engine example:
# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa

import inflect

p = inflect.engine()

names = []

while True:
    try:
        n = input("Name: ")
        names.append(n)

    except EOFError:
        break

p_names = p.join(names)

print("Adieu, adieu, to " + p_names)