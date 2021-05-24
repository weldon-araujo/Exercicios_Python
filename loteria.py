
def megasena():
    import random
    li = list(range(1, 61))
    print(f'Escolha entre 6 e 15 números para ser sorteado dentre os números abaixo: {li}')
    qtd = int(input('Quantos números você vai jogar ? '))
    if qtd < 6:
        print('Você precisa escolher entre 6 e 15 números, tente novamente')
        megasena()
    elif qtd > 15:
        print('Você precisa escolher entre 15 e 18 números, tente novamente')
        megasena()
    else:
        print(f'Seus números são: {sorted(random.sample(li, qtd))}\nBoa sorte !')


def lotofacil():
    import random
    l = list(range(1, 26))
    print(f'Escolha entre 15 e 18 números para ser sorteado dentre os números abaixo: {l}')
    qtd = int(input('Quantos números você vai selecionar ? '))
    if qtd < 15:
        print('Você precisa escolher entre 15 e 18 números, tente novamente')
        lotofacil()
    elif qtd > 18:
        print('Você precisa escolher entre 15 e 18 números, tente novamente')
        lotofacil()
    else:
        print(f'Seus números são: {sorted(random.sample(l, qtd))}\nBoa sorte! ')

resp = input('Escolha: uma das opções\nMega senha\nLotofácil\n')
if resp == 'mega sena' or resp == 'Mega sena':
    megasena()
elif resp == 'lotofacil' or resp == 'Lotofacil':
    lotofacil()
