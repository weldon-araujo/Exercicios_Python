# faça um progrma que jogue par ou impar com o computador o programa so vai parar quando o jogador perder

import random
import emoji
import time

def trap():
    print('=' * 50, '=' * 50)

while True:
    pc = random.randint(1, 11)
    lp = ['I','P']
    espc = random.choice(lp)
    nd = int(input('Quantos dedos: '))
    escp = input('Par ou Impar [P/I]: ').upper()[0]
    print('...')
    time.sleep(1)
    print('')
    if escp == 'P' and espc == 'I' and (nd + pc) % 2 == 0:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, a maquina escolheu {espc} e apostou {pc} dedos, deu PAR voce \033[1;34mGANHOU\033[1;m')
        print(emoji.emojize(':person_tipping_hand_medium-dark_skin_tone:'))
        trap()
    elif escp == 'P' and espc == 'P' and (nd + pc) % 2 == 0:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, a maquina escolheu {espc} e apostou {pc} dedos, deu PAR entao \033[1;32mEMPATOU\033[1;m')
        print(emoji.emojize(':eyes:'))
        trap()
    elif escp == 'I' and espc == 'P' and (nd + pc) % 2 == 0:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu PAR voce \033[1;31mPERDEU\033[1;m')
        print(emoji.emojize(':woman_juggling_medium_skin_tone:'))
        trap()
    elif escp == 'I' and espc == 'I' and (nd + pc) % 2 == 0:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu PAR os dois \033[1;31mPERDERAM\033[1;m')
        print(emoji.emojize(':yawning_face:'))
        trap()
    elif escp == 'I' and espc == 'P' and (nd + pc) % 2 == 1:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu IMPAR voce \033[1;34mGANHOU\033[1;m')
        print(emoji.emojize(':person_tipping_hand_medium-dark_skin_tone:'))
        trap()
    elif escp == 'I' and espc == 'I' and (nd + pc) % 2 == 1:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu IMPAR entao \033[1;32mEMPATOU\033[1;m')
        print(emoji.emojize(':eyes:'))
        trap()
    elif escp == 'P' and espc == 'I' and (nd + pc) % 2 == 1:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu PAR voce \033[1;31mPERDEU\033[1;m')
        print(emoji.emojize(':woman_juggling_medium_skin_tone:'))
        trap()
    elif escp == 'P' and espc == 'P' and (nd + pc) % 2 == 1:
        trap()
        print(f'voce escolheu {escp} e apostou {nd} dedos, maquina escolheu {espc} e apostou {pc} dedos, deu IMPAR os dois \033[1;31mPERDERAM\033[1;m')
        print(emoji.emojize(':yawning_face:'))
        trap()
    else:
        print('Opção inválida')


