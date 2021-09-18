"""
Задание 1(5 - баллов):
Напишите программу, которая преобразует из значение температуры из Цельсия в Фарангейты.
Значние температуры в Цельсиях вводится пользователем
Формулу погуглите))
"""

#  BEGIN
print('Exercise #1')
print('please input value in Celsius')
n = int(input())
f = (n * 1.8) + 32
print('Fahrenheit', f)
#  END

"""
Задание 2(5 - балоов):
В python кроме стандартных операций ==, !=, <, >
есть еще операции
1. >= это больше или равно 2 >= 1 -> True, 2 >= 2 -> True, 2 >= 3 -> False
2. <= это меньше или равно 2 <= 3 -> True, 2 <= 2 -> True, 2 <= 1 -> False
Напишите программу, которая вычисляет модуль числа.
Модуль числа это такая математическая функция:
|x| = x, если x >= 0
|x| = -x, если x < 0
Число вводится пользоваетелем.
"""
#  BEGIN
print('Exercise #2')
print('please input a number')
n = int(input())
if n >= 0:
    n = n
    print("absolute value is", n)
elif n <= 0:
    n = -n
    print("absolute value is", n)
else:
    print("absolute value is 0")
#  END

"""
Задание 3(7 - баллов):
Напишите программу, которая считает функцию голосования.
Функция голосование это логическая функция f(x, y, z) от трех
логических(это значит они принимают значение либо True либо False) аргументов x, y, z
и вычисляется следющим образом:
f(x, y, x) = True, если ХОТЯ БЫ два из трех аргументов True, иначе она равна False
Пример: f(True, False, True) = True
В этом задании нужно считать три значение x, y, z.
0 будет отвечать за False
1 будет отвечать за True
И вывести на экран значение фукнции голосования от этих трех значений.
Пример взаимодействия:
0
1
1
>> True
Пример взаимодействия:
0
0
1
>> False
"""

#  BEGIN
print('Exercise #3')
print('please input 1 or 0 for the first time')
first = int(input())
print('please input 1 or 0 for the second time')
second = int(input())
print('please input 1 or 0 for the last time')
third = int(input())
if first == second == 1 or first == third == 1 or second == third == 1:
    print('True')
else:
    print('False')
#  END

"""
Задание 4(7 - баллов):
Напишите программу, которая для введенного целого числа n считает значение
факториала  n!. n! = 1 * 2 * 3 * ... * n
"""

#  BEGIN
print('Exercise #4')
print('please input integer value')
n = int(input())
factorial = 1
number = 1
for number in range(1, n+1):
    factorial = factorial*number
    number += 1
print('factorial is', factorial)
#  END


"""
Задание 5(8 - баллов):
Напишите программу, которая для введенного целого числа n считает значение произведения
всех четных чисел до n(n >= 2)включительно.
Пример: n = 6: 2 * 4 * 6 = 48
        n = 4: 2 * 4 = 8
        n = 2: 2
"""

#  BEGIN
print('Exercise #5')
print('please input positive integer value')
n = int(input())
multi = 1
number = 0
for number in range(2, n+1):
    if number % 2 == 0:
        multi = multi*number
    number += 1
print('result is', multi)
#  END


"""
Задание 6(8 - баллов):
Напишите программу, которая для введененой строки считает количество символов латинской 'a' в ней
и печатает на экран
Вводится строка только в нижнем регистре
Пример: для "margarita" это выведется 3
        для "python is the best" выведется 0
"""

#  BEGIN
print('Exercise #6')
print('please input string value')
string = input()
count = 0
for c in string:
    if c == 'a':
        count += 1
print('result is', count)
#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество гласных букв в ней
и печатает на экран. Гласными считаются: a, e, i, o, u, y
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 4 (a - 3, i - 1)
        для "python is the best" выведется 5 (y - 1, o - 1, i - 1, e - 2)
"""
#  BEGIN
print('Exercise #7.1')
print('please input string value in lower case')
string = input()
a = 0
aprint = ""
e = 0
eprint = ""
i = 0
iprint = ""
o = 0
oprint = ""
u = 0
uprint = ""
y = 0
yprint = ""
vowels = 0
for c in string:
    if c == 'a':
        a += 1
        vowels += 1
    elif c == 'e':
        e += 1
        vowels += 1
    elif c == 'i':
        i += 1
        vowels += 1
    elif c == 'o':
        o += 1
        vowels += 1
    elif c == 'u':
        u += 1
        vowels += 1
    elif c == 'y':
        y += 1
        vowels += 1
if a != 0:
    a = str(a)
    aprint = ('a - ' + a +',')
if e != 0:
    e = str(e)
    eprint = ('e - ' + e +',')
if i != 0:
    i = str(i)
    iprint = ('i - ' + i +',')
if o != 0:
    o = str(o)
    oprint = ('o - ' + o +',')
if u != 0:
    u = str(u)
    uprint = ('u - ' + u +',')
if y != 0:
    y = str(y)
    yprint = ('y - ' + y)
print('there are', vowels, 'vowels (', aprint, eprint, iprint, oprint, uprint, yprint,")")
#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество согласных букв в ней
и печатает на экран. В этой задаче будем считать, что строка не содержит пробелов.
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 5
"""
#  BEGIN
print('Exercise #7.2')
print('please input string value in lower case without spaces')
string = input()
consonants = 0
for c in string:
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u' and c != 'y':
        consonants += 1
print('there are', consonants, 'consonants')
#  END


"""
Задание 8(20 - баллов):
Напишите программу, которая для введененой строки печатает ее символы в обрамном порядке
Пример: для "margarita" выведется "atiragram"
        для "python is the best" выведется "tseb eht si nohtyp"
Вводится строка только в нижнем регистре
"""
#  BEGIN
print('Exercise #8')
print('please input string value in lower case')
string = input()
length = len(string)
newstring = ''
while length != 0:
    newstring = 'newstring'+string[length-1]
    length = length-1
print(newstring)
#  END


"""
Задание 9(20 - баллов):
Напишите программу, которая для введенного целого числа n печатает такую вот пирамиду
1
2 2
3 3 3
4 4 4 4
....
n n n ... n
В последней строке n раз напечатали n
"""

#  BEGIN
print('Exercise #9')
print('please input positive integer value')
n = int(input())
for rows in range(1,n+1):
    for columns in range(rows):
        print(rows, end=" ")
    print(" ")
#  END
