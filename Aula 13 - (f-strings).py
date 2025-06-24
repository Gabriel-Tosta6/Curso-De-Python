nome = 'Gabriel'
altura = 1.85
peso = 75
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,' #:.2f define a quantidade de casas 
#decimais após a virgula
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Gabriel tem 1.85 de altura,
# pesa 75 quilos e seu IMC é
# 21.91