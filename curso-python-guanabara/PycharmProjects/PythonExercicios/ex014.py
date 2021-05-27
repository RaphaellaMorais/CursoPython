c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
#não vou precisar de parenteses aqui;
#porq a ordem de precendência da expressão é exatamente na ordem que os operadores aparecem;
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
