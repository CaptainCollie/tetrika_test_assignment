"""
Задача №1.
Дан массив чисел, состоящий из некоторого количества
подряд идущих единиц, за которыми следует
какое-то количество подряд идущих нулей: 111111111111111111111111100000000.

Найти индекс первого нуля
(то есть найти такое место, где заканчиваются единицы, и начинаются нули)
def task(array):
    pass

print(task("111111111110000000000000000"))
# >> OUT: 10
…
"""


def task(string: str):
    left, right = 0, len(string) - 1
    while left <= right:
        mid = (left + right) // 2
        curr = string[mid] == "0"
        prev = string[mid - 1] == "1"
        if curr and prev:
            return mid
        elif curr and mid == 0:
            return mid
        elif curr and not prev:
            right = mid - 1
        else:
            left = mid + 1
    return -1
