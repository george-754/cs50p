# Convert 12 hour time to 24 hour time

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Search for pattern ie. "9 AM to 5 PM" or "9:00 AM to 5:00 PM"
    t_pattern = r"(^\b(((1[0-2]|[1-9])\s(AM|PM))|((1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM)))\sto\s(((1[0-2]|[1-9])\s(AM|PM))|((1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM)))\b$)"
    #((1[0-2]|[1-9])\s(AM|PM))
    #((1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM))
    # ((1[0-2]|[1-9])\s(AM|PM))|((1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM))
    #long_pattern = "(^\b(1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM)\sto\s(1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM)\b$)"
    
    t = re.search(t_pattern, s)
    if t:
        # IF time was entered with the correct format then extract each time and format it through the fromat_time function
        first, second = t.group().split(" to ")
        
        formated_first = format_time(first)
        formated_second = format_time(second)
        #return t
        return f"{formated_first} to {formated_second}"
    else:
        # IF match was not found for the correct format throw a ValueError
        raise ValueError


def format_time(time):
    if ":" in time:
        # If time has a ":" then replace the : with a space and then split at the spaces to extract the hours, minutes and "AM or PM"
        time = time.replace(":", " ")
        h, m, z = time.split(" ")
        h = int(h)
        m = int(m)

        # IF time is PM then add 12 to the hours to make it 24 hour time
        if z == "PM" and h != 12:
            h += 12

        elif z == "AM" and h == 12:
            h = 0
        
        return f"{h:02}:{m:02}"
    
    else:
        # IF time was only given an hour then split at the spaces to extract the hour and "AM or PM"
        h, z = time.split(" ")
        h = int(h)
        # Give the variable for minutes a 0
        m = 0

        # IF time is PM then add 12 to the hours to make it 24 hour time
        if z == "PM" and h != 12:
            h += 12
        
        elif z == "AM" and h == 12:
            h = 0

        return f"{h:02}:{m:02}"



if __name__ == "__main__":
    main()