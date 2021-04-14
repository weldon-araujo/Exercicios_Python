# melhore o jogo do desafio 28 onde o pc vai pensar num numero entre 0 e 10 so que agora o jogador vai tentar
# advinhar até acertar mostrando no fim quantas tentativas foram necessárias

import random
import emoji
pc = random.randint(0, 10)

print('\033[1;31mQUAL NUMERO A MÁQUINA TIROU ?\033[m')
esc = 0
c = 0

while pc != esc:
    esc = int(input('Quantas vezes: '))
    c += 1
    if esc > pc:
        print('MENOS\033[1;31m\033[m')
    elif esc < pc:
        print('MAIS ')
    else:
        print('')

print('ACERTOU EM {} TENTATIVAS, \033[1;31mA MAQUINA TIROU NUMERO {} {}\033[m'.format(c, pc,emoji.emojize(':thumbs_up:')))
