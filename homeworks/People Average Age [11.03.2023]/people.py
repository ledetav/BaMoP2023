import json
import os
from datetime import datetime, date

current_dir = os.path.dirname(os.path.abspath(__file__))

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Открытие файла с данными
with open(os.path.join(current_dir, 'people.json')) as f:
    data = json.load(f)

# Список дат рождения в формате datetime
birthdays = []

# Обход всех записей в файле
for person in data:
    # Обработка даты рождения в разных форматах
    try:
        dt = datetime.strptime(person['birthday'], '%d/%m/%Y')
    except ValueError:
        try:
            dt = datetime.strptime(person['birthday'], '%d.%m.%Y')
        except ValueError:
            try:
                dt = datetime.strptime(person['birthday'], '%Y-%m-%d')
            except ValueError:
                print(f"Ошибка: не удалось распознать дату {person['birthday']}")
                continue

    # Добавление даты рождения в список
    birthdays.append(dt.date())

# Расчет среднего возраста
total_age = 0
for bdate in birthdays:
    total_age += calculate_age(bdate)
average_age = total_age / len(birthdays)

# Вывод результата на экран
years = int(average_age)
months = int((average_age - years) * 12)
days = int(((average_age - years) * 12 - months) * 30)

print(f"Средний возраст: {years} лет {months} месяцев {days} дней")