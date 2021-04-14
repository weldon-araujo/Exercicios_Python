
pre = float(input('Entre com o preço do produto: '))
d = pre / 100
desc = 5 * d
pf = pre - desc
print('O valor {} R$ sai por {} com desconto de 5%'.format(pre, pf))
