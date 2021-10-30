import pytest

def unique(numbers):
    """
    Дна список чисел. Некоторые числа в нем могут повторяться.
    Верните новый список чисел, который состоит из чисел numbers, но уже без повторений.
    """
    return list(set(numbers))

@pytest.mark.parametrize('numbers, result',
                         [
                             ([1, 1, 2, 3, 4, 4, 5, 5],[1, 2, 3, 4, 5]),
                             ([1, 1, 1, 1],[1]),
                             ([],[]),
                         ]
                        )

def test_unique_parametrized(numbers, result):
    print("test_unique_parametrized is called")
    assert unique(numbers) == result


def count_words(strings):
    """
    Дан список строк strings.
    Нужно для каждой строки посчитать сколько раз она встретилось в списке.
    """

    counter = {}
    for string in strings:
        if string not in counter:
            counter[string] = 1
        else:
            counter[string] += 1
    return counter

@pytest.mark.parametrize('strings, result',
                          [
                              (["text", "text", "apple", "orange", "yellow", "orange"],{"text": 2,"orange": 2,"yellow": 1,"apple": 1}),
                              (["text", "text", "text", "text", "text", "orange"],{"text": 5,"orange": 1,}),
                              ([],{})
                          ]
                         )

def test_count_words_parametrized(strings,result):
    print("test_count_words_parametrized is called")
    assert count_words(strings) == result


def consistent_string(strings, allowed):
    """
    Дан список строк strings, и строка allowed, которая состоит из уникальных символов.
    Реализуйте функцию, которая из списка строк strings отфильтрует только те, которые состоят из символов
    содержащихся в allowed и не содержат других символов. Нужное вернуть множество(set) из нужных строк.
    """

    result = set()
    for string in strings:
        is_consistent = True
        for symbol in string:
            if symbol not in allowed:
                is_consistent = False
        if is_consistent:
            result.add(string)
    return result

@pytest.mark.parametrize(    'allowed, strings, result',
                          [
                             ("ab",  ["ad", "bd", "aaab", "baa", "badab"],      {"aaab", "baa"}),
                             ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"],  {"a", "b", "c", "ab", "ac", "bc", "abc"}),
                             ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],  {"cc", "acd", "ac", "d"}),
                          ])

def test_consistent_string_parametrized(allowed, strings, result):
    print("test_consistent_string_parametrized is called")
    assert consistent_string(allowed=allowed, strings=strings) == result


def sort_desc(strings):
    """
    Дан список строк. Отсортируйте его в порядке обратном алфавитному.
    """
    strings.sort(reverse=True)
    return strings

@pytest.mark.parametrize('strings,result',
                         [
                             (["ad", "bd", "aaab", "baa", "badab"],['bd', 'badab', 'baa', 'ad', 'aaab']),
                             (["a", "b", "c", "ab", "ac", "bc", "abc"],['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a'])
                         ]
                         )

def test_sort_desc_parametrized(strings, result):
    print("test_sort_desc_parametrized is called")
    assert sort_desc(strings) == result


def filter_even(numbers):
    """
    При помощи встроенный функции фильтр, отфильтруйте только четные числа из списка numbers
    в отсортированном по возрастанию порядке
    """

    evens = list(filter(lambda number: number % 2 == 0, numbers))
    evens.sort
    return evens

@pytest.mark.parametrize('numbers, result',
                         [
                             ([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12],[2, 4, 6, 8, 10, 12]),
                             ([2, 2, 4, 6, 6, 8, 10, 12],[2, 2, 4, 6, 6, 8, 10, 12]),
                             ([1, 1, 2, 3],[2]),
                             ([1, 3, 5],[])
                         ]
                         )

def test_filter_even_parametrized(numbers,result):
    print("test_filter_even_parametrized is called")
    assert filter_even(numbers) == result
