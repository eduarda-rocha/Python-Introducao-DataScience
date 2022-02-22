# Instrução If

```
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados

for lista in dados:     #Varredura de cada uma das sublistas
    print(lista) 

for lista in dados:      #Verifica se o carro é zero km e imprime
  if (lista[2] == True):
    print(lista)      

zero_km_Y = []             #População do vetor caso a condição de zero km seja True
for lista in dados:
  if (lista[2] == True):
    zero_km_Y.append(lista)
zero_km_Y

zero_km_N = []            #População do vetor caso a condição de zero km seja False
for lista in dados:
  if (lista[2] == False):
    zero_km_N.append(lista)
zero_km_N

[lista for lista in dados if lista[2] == True]  #List Comprehensions de zero km True

```