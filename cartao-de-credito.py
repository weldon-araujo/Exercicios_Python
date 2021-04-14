# faça um programa que calcule um valor a ser pago por um produto considerando o seu preço normal
# e condiçao de pagamento a vista dinheiro ou cheque 10%, a vista no cartão 5%, em até 2% no cartao preço normal
# 3 vezes no cartão 20% a mais

def traco():
    print('=-=' * 30)

traco()
print('LOJAS ZELDIM')
traco()
v = float(input('Valor do produto: '))
esc = int(input('''Formas de pagamanto:\n[1] pagamento a vista 10% de desconto: \n[2] a vista no cartaõ 5% de desconto: \n[3] 2x no cartão preço normal: \n[4] 3x ou mais no cartão 20% de juros: '''))
if esc == 1:
    print('Sua compra fica em \033[31m{:.2f} R$\033[m com 10% de desconto'.format(v / 100 * v - 10))
elif esc == 2:
    print('Sua compra a vista no cartão de crédito fica em {:.2f} R$'.format(v / 100 * v - 5))
elif esc == 3:
    print('Sua compra em 2x no cartão de crédito fica em \033[31m{:.2f} R$\033[m'.format(v))
elif esc == 4:
    vc = int(input('Quantas vezes vai querer dividir: '))
    if vc > 2 and vc < 12:
        print('Sua compra fica no total de \033[31m{:.2f} R$\033[m divido em {} parcelas de \033[31m{:.2f} R$\033[m'.format(v / 100 * 20 + v, vc, (v / 100 * 20 + v) / vc))
    else:
        print('\033[31mOpção inválida !')
else:
    print('\033[31mOpção inválida !')

