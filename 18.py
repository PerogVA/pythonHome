# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# x = list(map(int,input('Введите числа через пробел: ').split(0,100)))

import random
my_f = open("result.txt", "w")
#with open("result.txt", "w+", encoding='utf-8') as my_f:
k = int(input("Введите число:   "))
lst = [random.randint(0,100) for i in range(k + 1)]
print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + "*x" + str(k-i)  +  " + " 
        x += str(lst[i]) + "*x^" + str(k-i)  +  " + " 
    else:
        x += str(lst[i])
print(x)