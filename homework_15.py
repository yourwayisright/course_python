import pytest
import math

class Figure():

    def square(self):
        pass

    def perimeter(self):
        pass

class Triangle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = (self[0]+self[1]+self[2])/2
        s = math.sqrt(p*(p-self[0])*(p-self[1])*(p-self[2]))
        return s

    def perimeter(self):
        p = self[0]+self[1]+self[2]
        return p

@pytest.mark.parametrize('self,result',
                         [
                             ([2,3,4],2.9047375096555625)
                         ]
                         )
def test_square(self,result):
    assert Triangle.square(self) == result

@pytest.mark.parametrize('self,result',
                         [
                             ([2,3,4],9)
                         ]
                         )
def test_perimeter(self,result):
    assert Triangle.perimeter(self) == result

class Square(Figure):
    def __init__(self,a):
        self.a = a

    def square(self):
        s = pow(self[0],2)
        return s

    def perimeter(self):
        p = 4*self[0]
        return p


class Round(Figure):
    def __init__(self,a):
        self.a = a

    def square(self):
        s = 3.1415*pow(self[0],2)
        return s

    def perimeter(self):
        p = 2*3.1415*self[0]
        return p
