"""
В функцию передаются координаты двух противоположных вершин одного
прямоугольника и двух противоположных вершин второго прямоугольника.

Найти, пересекаются ли эти прямоугольники?
Немного посложнее – найти площадь пересечения


def task(x1,y1,x2,y2,x3,y3,x4,y4):
    pass

print(task(1,1,2,2,3,3,4,4))
# >> OUT: False

"""
from typing import Tuple, Optional


def task(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int,
         y4: int) -> int:
    first_shape_dots = get_full_coordinates(x1, y1, x2, y2)
    second_shape_dots = get_full_coordinates(x3, y3, x4, y4)
    if all(check_dot_belongs(dot, (x1, y1, x2, y2)) for dot in
           second_shape_dots):
        return calculate_area((x3, y3), (x4, y4))

    if all(check_dot_belongs(dot, (x3, y3, x4, y4)) for dot in
           first_shape_dots):
        return calculate_area((x1, y1), (x2, y2))

    second_dot_in_first = get_dot_belonging_to_shape(second_shape_dots,
                                                     (x1, y1, x2, y2))

    if not second_dot_in_first:
        return -1

    first_dot_in_second = get_dot_belonging_to_shape(first_shape_dots,
                                                     (x3, y3, x4, y4))

    return calculate_area(second_dot_in_first, first_dot_in_second)


def check_dot_belongs(dot_coor: Tuple[int, int],
                      shape_coordinates: Tuple[int, int, int, int]) -> bool:
    x, y = dot_coor
    x1, y1, x2, y2 = shape_coordinates
    return (x1 <= x <= x2 or x2 <= x <= x1) and (
            y1 <= y <= y2 or y2 <= y <= y1)


def get_full_coordinates(x1: int, y1: int, x2: int, y2: int) -> Tuple[
        Tuple[int, int], ...]:
    return (
        (x1, y1),
        (x1, y2),
        (x2, y2),
        (x2, y1),
    )


def get_dot_belonging_to_shape(shape_coor: Tuple[Tuple[int, int], ...],
                               opposite_shape_coor: Tuple[
                                   int, int, int, int]) -> Optional[
        Tuple[int, int]]:
    for dot in shape_coor:
        if check_dot_belongs(dot, opposite_shape_coor):
            return dot
    return None


def calculate_area(dot1: Tuple[int, int], dot2: Tuple[int, int]) -> int:
    x1, y1 = dot1
    x2, y2 = dot2
    return abs(abs(x1) - abs(x2)) * abs(abs(y1) - abs(y2))
