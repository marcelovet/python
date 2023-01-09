"""
CONSTANTE = "Variáveis" que não vão mudar (nome em uppercase)
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim), quanto mais blocos dentro de blocos, mais complexo e pior
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local do radar 1
RADAR_RANGE = 1 # a distância onde o radar pega

"""
if velocidade > RADAR_1:
    print('Velocidade superior ao limite do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro multado em radar 1')
"""
velocidade_superior_ao_radar1 = velocidade > RADAR_1
carro_no_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_no_radar and velocidade_superior_ao_radar1

if velocidade_superior_ao_radar1:
    print('Velocidade superior ao limite do radar 1')

if  carro_multado:
    print('Carro multado em radar 1')