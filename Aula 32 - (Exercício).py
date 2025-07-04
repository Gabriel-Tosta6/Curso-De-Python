"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_string = input('Digite um número inteiro:\n')
try:
    numero_int = int(numero_string)
    if numero_int % 2 == 0:
        print(f'{numero_int} é par!')
    else:
        print(f'{numero_int} é ímpar!')
except:
    print('Não foi digitado um número inteiro!')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Olá, que horas são?:\n')
try:
    hora_float = float(hora)
    if hora_float >= 0.00 and hora_float <= 11.59:
        print('Bom dia!')
    elif hora_float >= 12.00 and hora_float <= 17.59:
        print('Boa tarde!')
    elif hora_float >= 18.00 and hora_float <= 23.59:
        print('Boa noite')
    else:
        print('Hora inválida!')
except:
    print('O formato de hora digitado está incorreto!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome:\n')
tamanho = len(nome)
try:
    if tamanho <= 4:
        print('Seu nome é curto!')
    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
except:
    print('Não foi possível ler seu nome!')