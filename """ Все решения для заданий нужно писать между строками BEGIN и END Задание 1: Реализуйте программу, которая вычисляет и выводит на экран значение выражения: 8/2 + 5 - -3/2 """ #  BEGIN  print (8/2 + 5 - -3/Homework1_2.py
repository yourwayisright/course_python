"""
Все решения для заданий нужно писать между строками BEGIN и END
Задание 1:
Реализуйте программу, которая вычисляет и выводит на экран значение выражения:
8 / 2 + 5 - -3 / 2
"""
#  BEGIN

print (8 / 2 + 5 - -3 / 2)

#  END

"""
Задание 2:
Напишите программу, которая выведет на экран:
"Khal Drogo's favorite word is "athjahakar""
Программа должна вывести на экран эту фразу в точности. Обратите внимание на кавычки в начале и в конце фразы.
"""

#  BEGIN

print ('\"Khal Drogo\'s favorite word is \"athjahakar""')

#  END


"""
Задание 3:
Выведите на экран

Winter came for the House of Frey.

используя конкатенацию слов
"""

#  BEGIN

#option 1
a = "Winter"
b = "came"
c = "for"
d = "the"
e = "House"
f = "of"
g = "Frey"
print (a,b,c,d,e,f,g)

#option 2
print ("Winter"+" "+"came"+" "+"for"+" "+"the"+" "+"House"+" "+"of"+" "+"Frey")

#  END


"""
Задание 4:
Присвойте переменной word значение "First text" и напечатайте ее
Поменяйте значние переменной word на "Second text" и напечатайте ее
"""

#  BEGIN

a = "First text"
print (a)
a = "Second text"
print (a)

#  END


"""
Задание 5:
Напишите программу, которая спришивает у пользователя его имя и приветсвует его.

Пример общения:
>>> What's your name?
Maruf
>> Hello, Maruf!

Программа должная задавать вопрос What's your name?, считать имя и потом напечатать приветсвенное сообщение

"""

#  BEGIN

print ('What\'s your name?')
a = input ()
print ('Hello,',a+"!")

#  END
