# Gerador-Questoes-Bhaskara

## Geração de valores

- Inicio e fim da conategm: 
   - if MenorValor = 1 and MaiorValor = 5: [1, 2, 3, 4, 5]
- Valores com numeros decimais: 
   - if MenorValor = 1 and MaiorValor = 5 and AposVirgValor = 1: [1, 1.1, 1.2, 1.3 ... 4.7, 4.8, 4.9, 5]
- Resultados com numeros decimais: 
   - if AposVirgResult = 2: O delta, x1 e x2 maximo serão até 2 casas decimais (1.45 = True; 1.432 = False)

Exemplo da configuração atual: config = {'MenorValor': 1, 'MaiorValor': 5, 'AposVirgValor': 1, 'AposVirgResult': 2}

## Validação

- Verifica se o delta e negativo
- Se delta ou "a" forem igual a 0, são desconsiderados, pois sempre resultará em S={0; 0}

Caso na verificação os valores forem inapropriados para a configuração do usuario ou cause um erro, esses valores não serão salvos

## Resultado

- Retorna uma lista com resultados validos
- Dentro da lista há dicionarios com os valores de: a, b, c, delta, x1 e x2
- Gera 2 arquivos .txt com as questões, um arquivo com os valores de a, b, c e outro com os valores de delta, x1, x2


