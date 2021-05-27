frase = 'Curso em Vídeo Python'
print(frase[::2])

print('Oi')
#uma maneira fácil de escrever na tela, quando eu executar ele vai imprimir o texto inteiro:
print('''Diversas leis foram editadas nos últimos tempos no sentido de facilitar o acesso à justiça forte na
desjudicialização de procedimentos. Ou seja, a retirada do âmbito da atuação do Poder Judiciário dos processos de
jurisdição voluntária nos quais inexiste, tecnicamente, conflito de interesses. Nessa linha, a Lei nº 8.951/1994 já
previa a possibilidade de consignação em pagamento perante instituições bancárias com base na adição dos
parágrafos 1º a 3º ao artigo 190 do CPC/1973.''')
#outros exemplos:
'''frase = '   Curso em Vídeo Python   '
print(frase.count('V'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))'''

'''frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))'''
#aqui é o único modo que tenho a possibilidade de mudar, mas aqui não vai estar salvo;
#Uma String em seus microelementos é imutável a não ser q utilize uma função de transformação de String e faça uma atribuição;
#para salvar e depois continuar imprimindo Android eu devo:
'''frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)'''
frase = 'Curso em Vídeo Python'
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
