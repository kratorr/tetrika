from collections import defaultdict

from bs4 import BeautifulSoup

import requests


base_url = 'https://ru.wikipedia.org'
start_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'


def get_animals_count_by_first_letter() -> dict:
    result = defaultdict(int)
    page_url = start_url
    get_english_word = False
    while True:
        r = requests.get(page_url).content.decode('utf-8')
        soup = BeautifulSoup(r, 'html.parser')
        div_with_animals = soup.find("div", {"class": "mw-category-group"})
        animals = div_with_animals.find_all('a')

        for animal in animals:
            if animal.text[0] == 'A':  # english A for break loop
                get_english_word = True
                break
            result[animal.text[0]] += 1
        if get_english_word:
            break

        page_url = soup.findAll('a', href=True, text='Следующая страница')[0]['href']
        page_url = base_url + page_url
        print(result)
    return result


if __name__ == '__main__':
    get_animals_count_by_first_letter()