# faça um programa que ao passa o limite de 80 km o programa mostre uma mensagem de levou multa
# e a cada km excedente pagara 7 reais

km = float(input('Quanto km: '))

ex = (km - 80) * 7
if km > 80:
    print('Voce passou com {} km e ultrapassou o lomite de 80 km/h voce vai pagar {} R$ de multa'.format(km,ex ))
