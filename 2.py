#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
#после друга. Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
#у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота интеллектом

#ОТВЕТ: 
#Сколько конфет возьмёт второй, первый игрок не знает. Но, начиная со второго хода
#первый игрок может опираться на предыдущий ход второго. На что здесь можно 
#опереться? Второй игрок может взять от 1 до 28 конфет. Тогда первый игрок может
#брать столько конфет, сколько нужно, чтобы за его ход и за предыдущий ход второго
#игрока в сумме получалось 29. Теперь, в первом ходе нужно взять столько конфет,
#чтобы остаток делился на 29. Т.е., в на первом ходе нужно взять 2021%29 = 20

from random import randint

def step(current_player, max_step, total):
    step = int(input(f'Твой ход, {current_player} = '))
    if max_step > total: max_step = total
    if step > max_step:
        step = int(input(f'Можно взять только {max_step} конфет. {current_player}, попробуй еще раз: '))
    total = total - step
    if total > 0:
        print(f'Осталось {total} конфет')
    else:
        print('Конфеты закончились')
    return step

def game_man_to_man():
    total = 2021
    max_step = 28
    player_1 = input('Игрок 1, как тебя зовут? ')
    player_2 = input('Игрок 2, как тебя зовут? ')
    print('Теперь определим, кто начнёт игру')
    players = [player_1, player_2]
    current_player_num = randint(-1, 0)
    print(f'{players[current_player_num+1]} ты ходишь первым !')
 
    while total > 0:
        current_player_num += 1
        current_player = players[current_player_num%2]
        total-=step(current_player, max_step, total)
 
    print(f'{current_player} ПОБЕДИЛ')

def game_man_to_bot():
    total = 2021
    max_step = 28
    player_1 = input('Игрок 1, как тебя зовут? ')
    player_2 = 'Бот'
    players = [player_1, player_2]
    print('Теперь определим, кто начнёт игру')

    current_player_num = randint(-1, 0)
    print(f'{players[current_player_num+1]} ты ходишь первым !')

    while total > 0:
        current_player_num += 1
        current_player = players[current_player_num%2]
        if current_player == 'Бот':
            print(f'Твой ход {current_player}: ')
            if total < max_step + 1:
                step = total
            else:
                quotient = total//(max_step+1)
                step = total - (quotient*(max_step+1))
                if step == -1:
                    step = max_step -1
                if step == 0:
                    step = max_step
            while step > max_step or step < 1:
                step = randint(1,max_step)
            print(step)
        else:
            step = int(input(f'Твой ход,  {current_player}:  '))
            while step > max_step or step > total:
                step = int(input(f'Можно взять только  {max_step} конфет, попробуй еще раз: '))
        total = total - step
        print(f'Осталось конфет {total}')

    print(f'Победил {current_player}')

game_man_to_bot()