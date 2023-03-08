import random
import os

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "game.txt")

secret_number = random.randint(1, 100)
name = input("Привет! Как тебя зовут? ")
num_guesses = 0

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    num_guesses += 1
    if guess == secret_number:
        print("Поздравляю, {}! Ты угадал число {} за {} попыток.".format(name, secret_number, num_guesses))
        with open(file_path, "a") as f:
            f.write("{} {}\n".format(num_guesses, name))
        break
    elif guess < secret_number:
        print("Твое число слишком маленькое. Попробуй еще раз.")
    else:
        print("Твое число слишком большое. Попробуй еще раз.")