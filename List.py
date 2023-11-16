class MyCollection(list):
    def __init__(self, *args):
        super(MyCollection, self).__init__(args[0])


def find_average(numbers: list) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Данный обьект не является листом!")
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def compare_to_lists(list1, list2):
    max_average = 0
    if find_average(list1) > find_average(list2):
        max_average = find_average(list1)
        print("Первый список имеет большее среднее значение")
    if find_average(list1) < find_average(list2):
        max_average = find_average(list1)
        print("Второй список имеет большее среднее значение")
    if find_average(list1) == find_average(list2):
        print("Средние значения равны")
        max_average = find_average(list1)
    return max_average
