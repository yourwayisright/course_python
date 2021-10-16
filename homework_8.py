def cinderella(mixed_cereals:list, pattern: str) -> list:
    '''
    С помощью filter необходимо реализовать функцию Золушка, которая принимает на вход
    список из разных зернышек и возвращает список, где все элементы равны заданному патерну
    :param mixed_cereals: список из зернышек, которые нужно отфильтровать
    :param pattern: зернышки, которые нужно отобрать
    :return: список, содержащий все элементы, подходящие под паттерн
    '''

    def filter_function(cereal):
        if cereal == pattern:
            return True
        else:
            return False

    filtered = []
    filtered = filter(filter_function,mixed_cereals)
    result = list(filtered)
    return result

def check_cinderella():
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'мак') == ['мак', 'мак']
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'просо') == ['просо']
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'пшеница') == ['пшеница', 'пшеница', 'пшеница']
    print('Check cinderella - It works!')

check_cinderella()


def even_numbers(list_of_numbers: list, check_even: bool) -> list:
    '''
    Необходимо с помощью filter реализоавать функцию, которая проанализирует элементы входящего списка
    и вернет только четные/нечетные из них в зависимости от значения флага check_even
    :param list_of_numbers: список чисел
    :param check_even: флаг проверки четных чисел (True - проверяем четные, False - нечетные)
    :return: список четных чисел
    '''


    def filter_function(number):
        if check_even == True:
            if number % 2 == 0:
                return True
            else:
                return False
        elif check_even == False:
            if number % 2 != 0:
                return True
            else:
                return False

    filtered = []
    filtered = filter(filter_function,list_of_numbers)
    result = list(filtered)
    return result


def check_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6], True) == [2, 4, 6]
    assert even_numbers([1, 2, 3, 4, 5, 6], False) == [1, 3, 5]
    assert even_numbers([11, 22, 33, 45, 55, 64], False) == [11, 33, 45, 55]
    assert even_numbers([11, 22, 33, 45, 55, 64], True) == [22, 64]
    print('Check even - It works!')


check_even_numbers()


def secret_names(real_names: list, secret_names: list):
    '''
    С помощью Map реализовать функцию, которая присваивает реальному имени - кодовое имя.
    Для реализации выбора кодового имени использовать random.choice()
    :param real_names: список реальных имен
    :param secret_names: список кодовых имен
    :return: список кодовых имен (равное количество реальных)
    Проверочную функцию здесь не делаю, просто буду запускать ваш код
    '''

    import random
    def new_name_function(name):
        name = random.choice(secret_names)
        return name

    renamed = []
    renamed = map(new_name_function,real_names)
    result = list(renamed)
    return result


print(*secret_names(['Iren', 'Alex'], ['Agent Carter', 'Hulk', 'IronMan']))
print(*secret_names(['Iren', 'Alex', 'Ann'], ['Flash', 'Wonder Woman', 'Harley Queen', 'Batman', 'Joker']))
