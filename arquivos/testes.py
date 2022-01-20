import os
import time

inicio = time.time()

def verificar_raiz(delta):

    if delta > 0:
        return verificar_dizima(delta**0.5)


def verificar_dizima(num):

    if num == round(num, config['AposVirgResult']):
        return num


add, nums, contN, ok = [], [], 0, True # Criando variaveis

config = {'MenorValor': -9, 'MaiorValor': 20, 'AposVirgValor': 0, 'AposVirgResult': 3} # Dicionario com as configurações

for k, v in config.items():

    if type(v) != int: # Verificando se o valor e inteiro"

        if ok: # Significa que é a primeira vez que houve um valor diferente de "int"

            print('Os valores da configuração devem ser números inteiros!')

        print(f'Confira o valor "{v}" no item "{k}"')

        ok = False # Pois agora sabemos que há um valor inadequado nas configurações

        # OBS: Não cancelei de imediato para que o programa termine de analisar o resto das configurações, se houver mais algum problema irá mostrar ao usuario

if ok is False: # Facha o programa se houver um valor invalido nas configurações
    exit()

if config['MenorValor'] > config['MaiorValor']: # Verfica se o menor valor e realmente o menor
    config['MenorValor'], config['MaiorValor'] = config['MaiorValor'], config['MenorValor'] # Irá inverter (Menor =  Maior; Maior = Menor)

# Nessa parte e para adicionar os valores decimais 
# config['AposVirgValor'] = 1 (Exemplo)

FimDecimal = 10 ** config['AposVirgValor'] # 10 ** 1 = 1*10 = 10 (10 Fim dos valores decimais)
Soma = 10 ** -config['AposVirgValor']      # 10 ** -1 = 1/10 = 0.1 (0.1 Soma para chegar)

# Com esses valores (10, 0.1) faço 10 * 0.1 e recebo 1

for c in range(config['MenorValor'], config['MaiorValor']):

    cont = c # cont = -9 (Exemplo)
    nums.append(cont) # nums = [-9]

    for c2 in range(1, FimDecimal):

        cont += Soma # cont = -8.9 (-9 + 0.1 = -8.9)
        nums.append(round(cont, config['AposVirgValor'])) # -8.9 e adicionado na lista arredonda para 1 numero decimal eliminar dizimas)

nums.append(config['MaiorValor']) # Adiciona o maior valor, pois acaba ficando de fora da lista

numsA = nums[:]

if 0 in nums: # Elimina o valor 0 da lista dos valores "a", pois se houver 0 todos x1, x2 tambem serão 0
    zero = nums.index(0)
    numsA.pop(zero)

for a in numsA:
    for b in nums:
        for c in nums:
            print(a, b, c)

print(time.time())