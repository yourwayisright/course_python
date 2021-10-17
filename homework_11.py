import math

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def to_polar(self):
        r = math.sqrt(pow(self.x, 2)+pow(self.y, 2))
        fi = math.atan(self.y / self.x)
        return (r, fi)

while True:
    data = input('Please input rectangular coordinates x and y: ').split()
    converted = Point.to_polar(Point(x=data[0], y=data[1]))
    print(f'Converted to polar ---> {converted}')
