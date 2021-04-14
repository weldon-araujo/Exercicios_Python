# Programa que peça notas e faça a media

def notas():
    n1 = float(input('Digite primeira nota: '))
    n2 = float(input('Digite segunda nota: '))
    n3 = float(input('Digite terceira nota: '))
    n4 = float(input('Digite quarta nota: '))
    s = (n1 + n2 + n3 + n4) / 4
    return s

n = notas()
if n >= 7:
    print('Passou com media {:.f} parabens'.format(n))
else:
    print('Não passou, sua média {:.2f} não atingiu 7'.format(n))
