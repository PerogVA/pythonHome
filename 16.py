# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите натуральное число N: '))
x = []
i = 2
while i <= n:
  if n % i == 0:  #875
    x.append(i)
    n //= i
    i = 2
  else: 
    i += 1
print (x)