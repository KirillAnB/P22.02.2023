"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    #Проверяем ,что массив не пустой
    if len(arr) == 0:
        raise ValueError("Empty array")
    #Допускаем, что первый элемент минимальный
    min_item = arr[0]
    #Задаем счетчик индекса для первого элемента
    item_index = 0
    #Записываем индекс минимального элемента
    min_item_index = item_index
    for i in arr:
        if min_item > i:
            min_item = i
            min_item_index = item_index
        item_index +=1
    return min_item_index


if __name__ == '__main__':
    list_with_data= [1, 25, -2, 34, 10, -42, -3] #Ищем минимум
    print(list_with_data)
    empty_list = [] #Проверяем с пустым списком
    print(min_search(empty_list))