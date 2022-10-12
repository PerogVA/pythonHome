from random import randint


can = 100
print('Игра "Конфеты". В вазе 2021 конфета, за раз вы можете взять не более 28 конфет, ')
print('выигрывает тот, кто возьмет последнюю конфету')
while can >= 0:
    man = int(input('Сколько конфет возьмешь? '))
    if man > 28 or man > can:
        print('Столько брать нельзя, жадина!')
        break
    else:    
        can -= man
        if can == 0:
            print('Поздравляю! Вы выиграли!')
            break

    if can >= 28:
        bot = randint(1, 29)
        print(f'Бот взял конфет: {bot}')
        can -= bot
        print(f'Осталось конфет: {can}')
    elif can <= 28:
        bot = randint(1, can)
        print(f'Бот взял конфет: {bot} ')
        can -= bot
        print(f'Осталось конфет: {can}')
    if can == 0:
        print('Вы проиграли!')
        break