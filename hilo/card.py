from random import randint


class Card:
    def __init__(self, min, max) -> None:
        self.number = randint(min, max)

    def __eq__(self, o):
        return self.number == o.number

    def __lt__(self, o):
        return self.number < o.number

    def __gt__(self, o):
        return self.number > o.number
