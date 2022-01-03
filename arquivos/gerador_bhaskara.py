import os

def verificar_raiz(delta):

    if delta > 0:
        return verificar_dizima(delta**0.5)


def verificar_dizima(num):

    if num == round(num, config['AposVirgResult']):
        return num


add, nums, contN, ok = [], [], 0, True

config = {'MenorValor': 9, 'MaiorValor': 5, 'AposVirgValor': 0, 'AposVirgResult': 3}

for k, v in config.items():
    if type(v) in (str, float):
        if ok:
            print('Os valores da configuração devem ser números inteiros!')
        print(f'Confira o valor "{v}" no item "{k}"')
        ok = False

if ok is False:
    exit()

if config['MenorValor'] > config['MaiorValor']:
    config['MenorValor'], config['MaiorValor'] = config['MaiorValor'], config['MenorValor']

FimDecimal = 10 ** config['AposVirgValor']
Soma = 10 ** -config['AposVirgValor']

for c in range(config['MenorValor'], config['MaiorValor']):

    cont = c
    nums.append(cont)

    for c2 in range(1, FimDecimal):

        cont += Soma
        nums.append(round(cont, config['AposVirgValor']))

nums.append(config['MaiorValor'])

numsA = nums[:]

if 0 in nums:
    zero = nums.index(0)
    numsA.pop(zero)

for a in numsA:
    for b in nums:
        for c in nums:
            print(a, b, c)
            contN += 1

            v = {'a': a, 'b': b, 'c': c, 'd': None, 'x1': 0, 'x2': 0}

            v['d'] = (v['b'])**2 -4 * v['a'] * v['c']

            raiz = verificar_raiz(v['d'])

            v['d'] = round(v['d'], config['AposVirgResult'])

            if raiz != None:

                for c in range(1, 3):

                    if c == 1:

                        part1 = - v['b'] + raiz

                    elif c == 2:

                        part1 = - v['b'] - raiz

                    part2 = 2 * v['a']

                    if 0 not in (part1, part2):

                        v[f'x{c}'] = verificar_dizima(part1/part2)

                if None not in (v['x1'], v['x2']):

                    add.append(v)

local = f'arquivos/QeR/Menor {config["MenorValor"]}_Maior {config["MaiorValor"]}_AposVirgValor {config["AposVirgValor"]}_AposVirgResult {config["AposVirgResult"]}_Tot {len(add)}'

os.makedirs(local, exist_ok=True)

perg = open(f'{local}/Questões Bhaskara.txt', 'w')
resp = open(f'{local}/Respostas Bhaskara.txt', 'w')

for c in range(len(add)):

    perg.write(f'{c+1}) a = {add[c]["a"]} | b = {add[c]["b"]} | c = {add[c]["c"]}\n\n')
    resp.write(f'{c+1}) d = {add[c]["d"]} | x1 = {add[c]["x1"]} | x2 = {add[c]["x2"]}\n\n')
