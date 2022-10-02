# Задайте список из n чисел
# последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
print((round(1 + 1 / n) ** n))
# list = [22, 33, 66, 44, 55, 99, 77]
# sum = 0
# index = int((1 + 1 / n) ** n)
# for i in range(0,len(list),index):
#     if i == index:
#         sum += i
# print(sum, end=',')

from msilib import sequence

n = int(input('Введите число: '))

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))




print('Введите число')
n = int(input())
print('[', end='')

for i in range(1, n + 1):
    res = round((1 + 1 / n) ** n, 3)
    sum = int(sum([res for res in range(i + 1)]))
    if i < (n + 1) - 1:
        print(f'{sum}', end=', ')
    else:
        print(f'{sum}', end='')
print(']', end='')