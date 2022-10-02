# . Реализуйте алгоритм перемешивания списка.
import random 
x = input("Введите символы для списка:    ").split()
random.shuffle(x)
print(x)