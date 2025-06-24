valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ')

if valor_1 > valor_2:
    print(f'valor_1 = "{valor_1}" é maior do que o valor_2 = "{valor_2}"')
elif valor_1 == valor_2:
    print(f'valor_1 = "{valor_1}" é igual ao valor_2 = "{valor_2}"')
else:
    print(f'valor_2 = "{valor_2}" é maior do que o valor_1 = "{valor_1}"')