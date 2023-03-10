# Задача 1
Требуется написать функцию magic(), которая принимает на вход последовательность случайных чисел, длина которой от 5 до 100 и число Х (больше нуля). Функция должна выяснить, можно ли разделить сумму чисел последовательности на число Х без остатка и вернуть True или False в зависимости от результата.

## Входные данные
- последовательность случайных чисел от 0 до 9999, длина которой от 5 до 100;
- число Х (больше нуля).

## Выходные данные
- True, если сумма чисел последовательности делится на Х без остатка;
- False, если сумма чисел последовательности не делится на Х без остатка.

## Пример
**Входные данные**
```
1 2 3 4 5 
3
```

**Выходные данные**
```True```

# Задача 2
Требуется написать функцию eqv(a, b, c, eps), которая принимает на вход три числа: a и b (оба дробные, каждое больше 1000, но меньше 99999) и c (дробное число - сумма a и b), а также точность eps. Функция должна проверить, что c равняется сумме a и b с заданной точностью и вернуть True или False в зависимости от результата. 

## Входные данные
- дробное числа a и b;
- Сумма чисел a и b;
- Числа a и b генерируются рандомно в диапазоне от 1000 до 99999;
- eps - точность проверки, равная 0.01% от большего из чисел a или b.

## Выходные данные
- True, если сумма a и b равна c сумме заданной точностью;
- False, если сумма a и b не равна c сумме заданной точностью.

## Пример
**Входные данные**
```
12345.6789 9876.54321
22222.22211
```

**Выходные данные**
```True```