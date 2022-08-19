# Implement a cookie jar in which to store cookies

import emoji



class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be greater than 0")
        self.max = capacity
        self.amount = 0

    def __str__(self):
        #return (emoji.emojize(":cookie:") * self.amount)
        return ("🍪" * self.amount)

    def deposit(self, n):
        self.amount += n
        if self.amount > self.capacity:
            raise ValueError("Not enough room in the cookie jar")

    def withdraw(self, n):
        self.amount -= n
        if self.amount < 0:
            raise ValueError("Not enough cookies in cookie jar")

    @property
    def capacity(self):
        return self.max

    @property
    def size(self):
        return self.amount


def main():

    jar = Jar()
    print(jar)


if __name__ == "__main__":
    main()

