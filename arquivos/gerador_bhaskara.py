add = []
x1 = x2 = 0

def verificar_raiz(delta):

    if delta >= 0:

        raiz = verificar_dizima(delta**0.5)

        if raiz != None:

            return raiz


def verificar_dizima(num):

    if num == round(num, 2):

        return num


for a in range(-9, 10):
    for b in range(-9, 10):
        for c in range(-9, 10):

            v = {'a': a, 'b': b, 'c': c}

            delta = (v['b'])**2 -4 * v['a'] * v['c']

            v['d'] = delta

            raiz = verificar_raiz(delta)

            if raiz != None:

                try:

                    x1 = (- v['b'] + raiz) / (2 * v['a'])
                    x2 = (- v['b'] - raiz) / (2 * v['a'])

                except ZeroDivisionError:

                    pass

                if None not in (x1, x2):

                    v['x1'] = verificar_dizima(x1)

                    v['x2'] = verificar_dizima(x2)

                    if None not in (v['x1'], v['x2']):

                        add.append(v)

print(add[789])
                

    

