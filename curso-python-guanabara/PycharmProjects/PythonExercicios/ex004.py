a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

# o "a" significa objeto;
#tod objeto tem caracteristicas e realiza funcionalidade - atributos e métodos;
#como a gente tem parenteses depois de cada um deles a gente está trabalhando métodos;
#e string tem esses métodos;
# a função input retorna sempre uma# string;