
class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def summarize (self):
        result = ([self.x1 + self.x2], [self.y1 + self.y2])
        return result

    def substraction (self):
        result = ([self.x1 - self.x2], [self.y1 - self.y2])
        return result

    def multiplication(self):
        result = ([self.x1 * self.x2],[self.y1 * self.x2])
        return result

while True:
    print("Welcome to class Vector! Please input preferable operation: summ, substr or multi")
    command = input()

    if command == 'summ':
        coordinate1 = input('Please input coordinates of the first vector: x y ').split()
        coordinate2 = input('Please input coordinates of the second vector: x y ').split()
        exemplar = Vector(x1=coordinate1[0], y1=coordinate1[1], x2=coordinate2[0], y2=coordinate2[1])
        result = Vector.summarize(exemplar)
        print(result)

    if command == 'substr':
        coordinate1 = input('Please input coordinates of the first vector: x y ').split()
        coordinate2 = input('Please input coordinates of the second vector: x y ').split()
        exemplar = Vector(x1=coordinate1[0], y1=coordinate1[1], x2=coordinate2[0], y2=coordinate2[1])
        result = Vector.substraction(exemplar)
        print(result)

    if command == 'multi':
            coordinate1 = input('Please input coordinates of the first vector: x y ').split()
            multiplicatior = input('Please input multiplicator: ')
            exemplar = Vector(x1=coordinate1[0], y1=coordinate1[1], x2=multiplicatior[0], y2=1)
            result = Vector.multiplication(exemplar)
            print(result)                     
