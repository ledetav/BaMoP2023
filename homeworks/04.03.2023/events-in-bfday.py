import requests
import urllib.parse
import re

def season_events(number_of_month, year):
    # Формируем URL для страницы категории на Википедии
    month_name = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"][number_of_month - 1]
    url = f"https://ru.wikipedia.org/wiki/Категория:{month_name}_{year}_года"
    url = urllib.parse.quote(url, safe=":/")

    # Делаем GET-запрос к странице категории и получаем ее содержимое в виде текста
    response = requests.get(url)
    content = response.text

    # Извлекаем названия статей из содержимого страницы
    pattern = r'<a href="\/wiki\/[^"]*" title="(?!Категория\:|Википедия\:)([^"]*)">'
    article_titles = re.findall(pattern, content)[:5]

    # Сохраняем информацию в текстовый файл
    with open("wiki.txt", "w", encoding="utf-8") as file:
        file.write(f"Вы родились в {month_name} в {year} году. \n")
        if len(article_titles) > 0:
            file.write("События в этом месяце: \n" + ". \n".join(article_titles) + ".")
        else:
            file.write(f" В {month_name} {year} года ничего не происходило.")
month = int(input("Введите месяц вашего рождения (число): "))
year = int(input("Введите год вашего рождения: "))

season_events(month, year)