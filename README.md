# Gerador-Questoes-Bhaskara

## Geração de valores

- Gera os valores para a, b, c
- Os valores gerados são entre -9 e 9
- Entre -9 e 9 há 6859 possibilidades, porém nem todas tem um resultados valido

## Validação

- Todas as possibilidades possiveis são testadas
- Elimina valores com dizima periódica extensa (Maximo 2)
- Verifica se o delta e negativo
- Verifica se há divisão por 0

Caso na verificação os valores forem inapropriados para a configuração do usuario ou cause um erro, esses valores não serão salvos

## Resultado

- Retorna uma lista com resultados validos
- Dentro da lista há dicionarios com os valores de: a, b, c, delta, x1 e x2
