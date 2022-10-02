# 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
from unittest import result


n = int(input("Введите количество вводимых чисел:  "))
list = [i for i in range(-n, n + 1)] 
print(list)
x = input("Укажите нумерацию тех чисел, через пробел, которую вы хотите переумножить  ").split()
print(x)
result = 1
for i in range(len(x)):
    x[i] = int(x[i]) - 1
    result *= list[x[i]]  
print(result)