# Get user input as a date  ie.  8/14/2022 or August 8, 2022 and output date format 2022-08-14


def main():

    print(convert())


def convert():

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        d = input("Date: ").capitalize().strip()
        
        try:
            for month in month_list:
                if d.startswith(month):
                    # If date is ie. January 1, 2000 strip the ", " and just make it a space then split it up to the corresponding values between spaces
                    #d_modify = d.replace(", ", ",,")
                    m, d, y= d.split(" ")
                    
                    if d.isnumeric() == False:
                        d = d.strip(',')
                        
                        m = month_list.index(m) + 1

                        if int(m) <= 12 and int(m) > 0 and int(d) > 0 and int(d) <= 31:
                            return f"{y}-{int(m):02}-{int(d):02}"

            m, d, y = d.split("/")

            if int(m) <= 12 and int(m) > 0 and int(d) > 0 and int(d) <= 31:
                return f"{y}-{int(m):02}-{int(d):02}"

        except ValueError:
            pass



if __name__ == "__main__":
    main()