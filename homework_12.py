class Vector:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


    def __add__(self, other):
        result = (self.x + other.x, self.y + other.y)
        return result

    def __sub__(self,other):
        result = (self.x - other.x, self.y - other.y)
        return result

    def __mul__(self,other):
        result = (self.x * int(other), self.y * int(other))
        return result

while True:
    print("Welcome to class Vector! Please input preferable operation: summ, substr or multi")
    command = input()

    if command == 'summ':
        coordinate1 = input('Please input coordinates of the first vector: x y ').split()
        coordinate2 = input('Please input coordinates of the second vector: x y ').split()
        exemplar1 = Vector(x=coordinate1[0], y=coordinate1[1])
        exemplar2 = Vector(x=coordinate2[0], y=coordinate2[1])
        result = exemplar1+exemplar2
        print(result)

    if command == 'substr':
        coordinate1 = input('Please input coordinates of the first vector: x y ').split()
        coordinate2 = input('Please input coordinates of the second vector: x y ').split()
        exemplar1 = Vector(x=coordinate1[0], y=coordinate1[1])
        exemplar2 = Vector(x=coordinate2[0], y=coordinate2[1])
        result = exemplar1-exemplar2
        print(result)

    if command == 'multi':
            coordinate1 = input('Please input coordinates of the first vector: x y ').split()
            multiplicatior = input('Please input multiplicator: ')
            exemplar1 = Vector(x=coordinate1[0], y=coordinate1[1])
            result = exemplar1*multiplicatior
            print(result)
