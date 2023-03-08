checked_nicknames = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']

user_nickname = input("Введите свой никнейм: ")

if user_nickname in checked_nicknames:
    print(f"Ты - свой. Приветствую, любезный {user_nickname}!")
else:
    print("Тут ничего нет. Еще есть вопросы?")