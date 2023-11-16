import pytest

import List


# Тест покрывает такие сценарии:
# 1)неверно определен средний элемент
# 2)средний элемент не равен 0
# 3)если элемент один-он же и есть средний элемент
def tests_find_average():
    assert List.find_average([1, 2, 3]) == 2, 'Ожидание не совпало с результатом'
    assert List.find_average([0]) == 0
    assert List.find_average([5]) == 5


# Тест покрывает такие сценарии:
# 1)если вместо листа в метод будет переданы другие типы данных отработает ошибка TypeError
def test_find_average_type():
    with pytest.raises(TypeError):
        List.find_average('qwerty')


# Тесты покрывает такие сценарии:
# 1)если максимальное среднее в первом списке, правильно посчитает и выведет текст:
# "Первый список имеет большее среднее значение"
def test_compare_to_lists_1():
    list1 = List.MyCollection([5, 6, 7])
    list2 = List.MyCollection([1, 2, 3])
    assert List.compare_to_lists(list1, list2) == List.find_average(list1)


# 2)если максимальное среднее во втором списке, правильно посчитает и выведет текст:
# "Второй список имеет большее среднее значение"
def test_compare_to_lists_2():
    list1 = List.MyCollection([1, 2, 3])
    list2 = List.MyCollection([5, 6, 7])
    assert List.compare_to_lists(list1, list2) == List.find_average(list1)


# 3)если максимальное среднее в первом списке равно максимальному числу второго списка,
# правильно посчитает и выведет текст:
# "Средние значения равны"
def test_compare_to_lists_3():
    list1 = List.MyCollection([5, 6, 7])
    list2 = List.MyCollection([5, 6, 7])
    assert List.compare_to_lists(list1, list2) == List.find_average(list1)
