'''from math import trunc
num = float(input('Digite um valor : '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''
#eu poderia usar o import math apenas, mas como eu só quero utilizar o trunc eu posso fazer da maneira acima;

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#nesse outro exemplo podemos ver que nem sempre será necessário importar modulos;