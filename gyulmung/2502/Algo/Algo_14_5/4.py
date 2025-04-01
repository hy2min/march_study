class Mart:

    def __init__(self, strawberry, melon, watermelon):
        self.strawberry = strawberry
        self.melon = melon
        self.watermelon = watermelon

    def Average(self):
        return (self.strawberry + self.melon + self.watermelon) / 3

A = Mart(300, 500, 1000)
B = Mart(450, 450, 900)
C = Mart(200, 150, 700)

mart_dict = {"A": A, "B": B, "C": C}

char = input()

print(int(mart_dict[char].Average()))