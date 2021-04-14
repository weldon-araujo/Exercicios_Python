# faça um programa de joquem pô

import random

def joquei():
    l = ['pedra','papel','tesoura']
    s = random.randint(0,2)
    e = input('Escolha papel, pedra ou tesoura: ')
    a = l[s]
    if a == 'pedra' and e == 'papel':
        print('voce ganhou {} embrula {}'.format(e, a))
    elif a == 'pedra' and e == 'tesoura':
        print('vocẽ perdeu {} quebra {}'.format(a, e))
    elif a == 'pedra' and e == 'pedra':
        print('voce tirou {} e o pc tirou {} deu empate joguem novamente'.format(e, a))
    elif a == 'papel' and e == 'pedra':
        print('voce perdeu {} embrulha {}'.format(a, e))
    elif a == 'papel' and e == 'tesoura':
        print('voce ganhou {} corta {}'.format(e, a))
    elif a == 'papel' and e == 'papel':
        print('voce tirou {} e o pc tirou {} deu empate joguem novamente'.format(e, a))
    elif a == 'tesoura' and e == 'pedra':
        print('voce ganhou {} quebra {}'.format(e, a))
    elif a == 'tesoura' and e == 'papel':
        print('voce perdeu {} corta {}'.format(a, e))
    else:
        print('voce tirou {} e o pc tirou {} deu empate joguem novamente'.format(e, a))

joquei()