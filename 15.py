# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# from math import pi


d = int (input('Введите точность числа пи до 16ти знаков:  '))
x=  9.869604401 **0.5
print(round(x,d))
