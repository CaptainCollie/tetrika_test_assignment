"""
В нашей школе мы не можем разглашать персональные данные пользователей,
но чтобы преподаватель и ученик смогли объяснить нашей поддержке,
кого они имеют в виду (у преподавателей, например, часто учится несколько Саш),
мы генерируем пользователям уникальные и легко произносимые имена.
Имя у нас состоит из прилагательного, имени животного и двузначной цифры.
В итоге получается, например, "Перламутровый лосось 77".

Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и
вывести количество животных на каждую букву алфавита.
Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
"""

import requests
from bs4 import BeautifulSoup

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def task():
    result = {}
    base_url = "https://ru.wikipedia.org"
    url = f"{base_url}/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%" \
          f"B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%B" \
          f"F%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
    english_words_count = 0
    while english_words_count < 30:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')

        animals = soup.find(class_='mw-category mw-category-columns').find_all(
            "li")
        for animal in animals:
            text = animal.text

            if text[0].lower() not in alphabet:
                english_words_count += 1
                continue
            result.setdefault(text[0], 0)
            result[text[0]] += 1

        url = base_url + soup.find('a', string='Следующая страница').get(
            'href')
    return format_result(result)


def format_result(result: dict) -> str:
    result = [f"{sym}: {result[sym]}" for sym in alphabet.upper() if
              sym in result]
    return '\n'.join(result)


res = task()
print(res)
