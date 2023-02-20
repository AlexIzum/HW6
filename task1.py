# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите кол-во элементов: '))

# arif_numbers = []
# for i in range(1, n+1):
#     arif_numbers.append(a1 + (i - 1) * d)

arif_numbers = [a1 + (i - 1) * d for i in range(1, n+1)]
print(*arif_numbers)