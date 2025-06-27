'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

No VS Code não existem variáveis constantes, que não mudam, então por boas práticas sempre que for escrever algo constante que não irá mudar, escrever em LETRAS MAIÚSCULAS !!!
'''
velocidade = 65 # velocidade atual do véiculo
local_carro = 99 # local em que o veículo está na estrada 

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RANGE_RADAR = 1 # a distância onde o radar pega


if velocidade > RADAR_1:
    print('O carro ultrapassou o limite de velocidade')
if local_carro >= (LOCAL_1 - RANGE_RADAR) and \
    local_carro <= (LOCAL_1 + RANGE_RADAR) and velocidade > RADAR_1:
    print('Carro multado no radar 1')




