"""
Напишите программу, которая считывает со стандартного ввода целые числа,
по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
input 5 -3 8 4 0
output 14

"""

счётчик = int(input())
сумма = 0
while счётчик != 0:
    сумма = сумма + счётчик
    счётчик = int(input())
print(сумма)
