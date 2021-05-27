#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer, {:=^20}!'.format(nome))
n1 = int(input('Um valor :'))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
#para quebrar linha \n, para não quebrar (,end='')

#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2))
#aqui não foi preciso usar mais uma variável p soma;
#normalmente eu uso com variável se eu for precisar desse resultado depois;
#no caso eu teria acrescentando s = n1 + n2

