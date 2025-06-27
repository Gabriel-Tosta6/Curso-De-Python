velocidade = 65 # velocidade atual do véiculo
local_carro = 99 # local em que o veículo está na estrada 

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RANGE_RADAR = 1 # a distância onde o radar pega

velocidade_carro_passou_limite = velocidade > RADAR_1

carro_passou_radar1 = local_carro >= (LOCAL_1 - RANGE_RADAR) and local_carro <= (LOCAL_1 + RANGE_RADAR)

carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_limite

if velocidade_carro_passou_limite:
    print('O carro ultrapassou o limite de velocidade')

if carro_passou_radar1:
    print('O carro passou no radar 1')

if carro_multado_radar1:
    print('O carro foi multado no radar 1')

# Simples é melhor que complexo, para que eu possa entender no futuro, ou para que outros programadores possam entender com mais facilidade! 