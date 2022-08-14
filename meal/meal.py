# Meal time. User inputs a time and the output needs to let the user know if its breakfast time or lunch time or diner time
# Breakfast 7:00 - 8:00, Lunch 12:00 - 13:00, Diner 18:00 - 19:00


def main():
    time = convert(input("What time is it? "))

    if time >= 7 and time <= 8:
        print("breakfast time")
    
    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    
    if "a.m." in time:
        hour, minute = time.split(":")
        minute, frame = minute.split(" ")

    elif "p.m." in time:
        hour, minute = time.split(":")
        minute, frame = minute.split(" ")
        hour = float(hour) +  12

    else:
        hour, minute = time.split(":")

    return float(hour) + (float(minute) / 60)


if __name__ == "__main__":
    main()