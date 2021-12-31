import os

def verificar_raiz(delta):

    if delta >= 0:
        return verificar_dizima(delta**0.5)
  

def verificar_dizima(num):

    if num == round(num, quantV):
        return num


add = []
x1 = x2 = cont = 0

menorP, maiorP, quantV = -9, 9, 2
'''
menorP = int(input('Menor número possivel: '))
maiorP = int(input('Maior número possivel: '))
quantV = int(input('Resultados com até quantos números após a virula? '))
'''
for a in range(menorP, maiorP + 1):
    for b in range(menorP, maiorP + 1):
        for c in range(menorP, maiorP + 1):

            cont += 1

            v = {'a': a, 'b': b, 'c': c, 'd': None, 'x1': 0, 'x2': 0}

            v['d'] = (v['b'])**2 -4 * v['a'] * v['c']

            raiz = verificar_raiz(v['d'])

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
while True:

    quest = input(f'Digite um valor de 0 a {len(add)}: ')

    if quest == '':
        
        break

    try:

        quest = int(quest)

    except ValueError:

        print('Digite um número!')

    else:

        if quest > len(add) or quest < 0:

            print('Valor invalido!')

        else:

            print(add[quest])

local = f'arquivos/QeR/Menor {menorP} | Maior {maiorP} | PosVirg {quantV} | Tot {len(add)}'

os.makedirs(local, exist_ok=True)

perg = open(f'{local}/Questões Bhaskara.txt', 'w')
resp = open(f'{local}/Respostas Bhaskara.txt', 'w')

print(os.getcwd())

for c in range(len(add)):

    perg.write(f'{c+1}) a = {add[c]["a"]} | b = {add[c]["b"]} | c = {add[c]["c"]}\n\n')
    resp.write(f'{c+1}) d = {add[c]["d"]} | x1 = {add[c]["x1"]} | x2 = {add[c]["x2"]}\n\n')

print('Menor -9 | Maior 9 | PosVirg 2 | Tot 1021')
