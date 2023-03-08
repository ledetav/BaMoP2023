def equilibrium_time_periods(S, D):
    count = 0
    for i in range(len(S)):
        if S[i] == D[i]:
            count += 1
    return count

def input_equilibrium_time_periods():
    # запрос ввода массивов
    S = list(map(int, input("Введите массив S через пробел: ").split()))
    D = list(map(int, input("Введите массив D через пробел: ").split()))

    # проверка на одинаковое количество элементов в массивах
    if len(S) != len(D):
        print("Массивы должны быть одинаковой длины!")
        return 0
    else:
        print(equilibrium_time_periods(S, D))

input_equilibrium_time_periods()
