# 1. (n + n) - Os parênteses sempre são executados primeiro, e de dentro pra fora
# 2. ** 
# 3. * / // % - Se os operadores tiverem a mesma precedência serão executados da 
# esquerda para a direita
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)