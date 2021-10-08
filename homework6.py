"""
Здесь вам нужно реализовать несколько фукнкций.
Для каждой функции есть другая тестовая функция, которая ее проверяет.
Чтобы убедиться, что ваше решение работает запустите ее.
Если функция нвзывется some_function, то тестирующия функция называется test_some_function.
Для проверки просто запустите тестирующую функцию, если после запуска увидели сообщение
"Tests passed" значит все ок!
Если возникла ошибка AssertionError значит решение не работает.
Если вдруг вы нашли ошибку в тестах, пишите в чат мы обсудим.
"""


def sum_diagonal(table):
    """
    Дан двумерный массив(список списков, таблица) размером n x n(квадратная таблица).
    Каждая строка состоит из m элементов, всего n строк.
    Вычислите сумму диагональных элементов
    """
    n = len(table)
    result = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                result = result + int(table[i][j])
    return result


def test_sum_diagonal():
    assert sum_diagonal([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]) == 6
    assert sum_diagonal([
        [0, 2, 3],
        [1, 0, 3],
        [1, 2, 0]
    ]) == 0
    assert sum_diagonal([
        [-1, 2, 3],
        [1, 2, 3],
        [1, 2, -3]
    ]) == -2
    assert sum_diagonal([
        [1, 2],
        [1, 2],
    ]) == 3
    assert sum_diagonal([
        [1],
    ]) == 1
    print("sum_diagonal - Tests passed")

test_sum_diagonal()

def max_in_row(table):
    """
    Дан двумерный массив(список списков, таблица) размером n x m.
    Каждая строка состоит из m элементов, всего n строк.
    Верните список, где будут максимумы для каждой строки таблицы:
    1-ый элемент это максимум в первой строке таблицы, 2-ой максимум во второй и тд
    """
    n = len(table)
    result = []
    for i in range(n):
        m = len(table[i])
        for j in range(m):
            max_element = table[i][0]
            if table[i][j] > max_element:
                max_element = table[i][j]
        result.append(max_element)
    return result


def test_max_in_row():
    assert max_in_row([
        [1, 2, 3, 4],
        [1, -1, 1, 2],
        [-4, -3, -2, -1]
    ]) == [4, 2, -1]
    assert max_in_row([
        [1],
        [2],
        [3],
    ]) == [1, 2, 3]
    assert max_in_row([
        [-1, -2, -3, -4],
        [-1, -1, -1, -2],
        [-4, -3, -2, -1]
    ]) == [-1, -1, -1]
    print("max_in_row - Tests passed")

test_max_in_row()

def sum_of_row(table):
    """
    Дан двумерный массив(список списков, таблица) размером n x m.
    Каждая строка состоит из m элементов, всего n строк.
    Верните список, где будут суммы элементов для каждой строки таблицы:
    1-ый элемент это сумму в первой строке таблицы, 2-ой сумма во второй и тд
    """
    n = len(table)
    result = []
    sum = 0
    for i in range(n):
        m = len(table[i])
        for j in range(m):
            sum = sum + table[i][j]
        result.append(sum)
        sum = 0
    return result


def test_sum_of_row():
    assert sum_of_row([
        [1, 2, 3, 4],
        [1, -1, 1, 2],
        [-4, -3, -2, -1]
    ]) == [10, 3, -10]
    assert sum_of_row([
        [1, 2, 3, 4],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ]) == [10, 0, 4]
    assert sum_of_row([
        [1, 2, 3],
        [1, -1, 1],
        [-4, -3, -2]
    ]) == [6, 1, -9]
    print("sum_of_row - Tests passed")

test_sum_of_row()

def fibonacci(n):
    """
    Числа Фибоначи опредляются след следующей последовательностью:
    1, 1, 2, 3, 5, 8, 13, 21 ...
    Первые два числа это 1 и 1
    Каждое следующее число сумма двух предыдущих.
    Математически это описывается рекурсивным уравнением:
    fib(n) = fib(n - 1) + fib(n - 2), когда n > 2
    fib(1) = 1, fib(2) = 2
    Напишите функцию, которая возвращает n-ое число Фибоначчи.
    P.S. Попробуйте посчитать 50-е число Фибоначчи. Как долго работает ваша программа?
    Попробуйте 100-ое число. Теперь как долго? А попробуйте 1000-ое))
    Как думаете, что происходит и почему это происходит?
    """

    if n == 1:
        f_number = 1
    elif n == 2:
        f_number = 1
    elif n > 2:
        f_number = fibonacci(n-1) + fibonacci(n-2)
    return f_number


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    print("test_finonacci - Tests passed")

test_fibonacci()

def recursive_pow(a, n):
    """
    Возведите число a в степень n рекурсивно.
    Формула такая:
    pow(a,n) = pow(a, n - 1) * a, когда n >= 1
    pow(a, 0) = 1
    """

    if n >= 1:
        result = recursive_pow(a, n - 1) * a
    elif n == 0:
        result = 1
    return result

def test_recursive_pow():
    assert recursive_pow(2, 5) == 2 ** 5
    assert recursive_pow(2, 0) == 1
    assert recursive_pow(1, 100) == 1
    assert recursive_pow(1, 0) == 1
    assert recursive_pow(3, 2) == 9
    assert recursive_pow(4, 4) == 4 ** 4
    print("recursive_pow - Tests passed")

test_recursive_pow()
