"""
Задача №3.
Мы сохраняем время присутствия каждого пользователя на уроке в виде интервалов.
В функцию передается словарь, содержащий три списка с таймстемпами
(время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из
четного количества элементов. Под четными индексами (начиная с 0)
время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и
возвращает время общего присутствия ученика и учителя на уроке (в секундах).
"""
from typing import List, Dict


def appearance(intervals: Dict[str, List[int]]) -> int:
    lesson = merge_intervals(transform_list(intervals.get('lesson')))
    pupil = merge_intervals(transform_list(intervals.get('pupil')))
    tutor = merge_intervals(transform_list(intervals.get('tutor')))
    lesson_pupil_intersection = find_intersections_interval(lesson, pupil)
    intersection_btw_all = find_intersections_interval(
        lesson_pupil_intersection, tutor)

    return sum([i[1] - i[0] for i in intersection_btw_all])


def find_intersections_interval(first: List[List[int]],
                                second: List[List[int]]) -> List[
        List[int]]:
    res = []
    i = j = 0

    while i < len(first) and j < len(second):

        low = max(first[i][0], second[j][0])
        high = min(first[i][1], second[j][1])
        if low < high:
            res.append([low, high])

        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return res


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def transform_list(intervals_list: List[int]) -> List[List[int]]:
    result = []
    for i in range(0, len(intervals_list), 2):
        result.append([intervals_list[i], intervals_list[i + 1]])
    return result
