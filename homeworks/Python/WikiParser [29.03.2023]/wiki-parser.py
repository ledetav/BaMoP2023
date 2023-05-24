import requests
from bs4 import BeautifulSoup
import re
import json

# Получаем HTML-код страницы
url = "https://ru.wikipedia.org/wiki/Категория:События_19_мая"
html = requests.get(url).text

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, "html.parser").find("div", {"class": "mw-category-generated", "dir": "ltr"})

# Ищем все ссылки на странице
links = soup.find_all("a")

# Создаем списки для каждой категории ссылок
links_with_numbers = []
links_with_letters_and_numbers = []
links_with_only_russian_letters = []
other_links = []

# Проходимся по каждой ссылке и определяем ее категорию
for link in links:
    title = link.get("title")
    if title:
        if re.search(r"\d", title):
            links_with_numbers.append(title)
        elif re.search(r"[a-zA-Z]\d", title):
            links_with_letters_and_numbers.append(title)
        elif re.search(r"^[а-яА-Я\s]+$", title):
            links_with_only_russian_letters.append(title)
        else:
            other_links.append(title)

# Сохраняем каждую категорию ссылок в отдельный файл
with open("links_with_numbers.txt", "w") as f:
    f.write("\n".join(links_with_numbers))

with open("links_with_letters_and_numbers.txt", "w") as f:
    f.write("\n".join(links_with_letters_and_numbers))

with open("links_with_only_russian_letters.txt", "w") as f:
    f.write("\n".join(links_with_only_russian_letters))

with open("other_links.txt", "w") as f:
    f.write("\n".join(other_links))

# Сохраняем каждую категорию ссылок в отдельный файл формате JSON
with open("links_with_numbers.json", "w") as f:
    json.dump(links_with_numbers, f)

with open("links_with_letters_and_numbers.json", "w") as f:
    json.dump(links_with_letters_and_numbers, f)

with open("links_with_only_russian_letters.json", "w") as f:
    json.dump(links_with_only_russian_letters, f)

with open("other_links.json", "w") as f:
    json.dump(other_links, f)