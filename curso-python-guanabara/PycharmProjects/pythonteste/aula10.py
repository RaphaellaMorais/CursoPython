'''nome = str(input('Qual é o seu nome? '))
if nome == 'Raphaella':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))'''
#comando colado no lado esquerdo sempre vai acontecer
#os que estiverem dentro são os blocos de comando, como os print
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#poderia tabém coolocar da seguinte forma: print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!') aqui seria uma condição simplificada.