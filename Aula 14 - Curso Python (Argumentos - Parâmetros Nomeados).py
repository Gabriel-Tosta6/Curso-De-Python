a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={nome3:.2f}'

# a,b -> argumentos | nome3 = c -> parâmetro nomeado

formato = string.format(a,b, nome3 = c)

print(formato)