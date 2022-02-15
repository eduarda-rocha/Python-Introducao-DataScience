# Seleções em Listas

```
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

Acessorios[0]               #Saída: 'Rodas de liga'
Acessorios[1]               #Saída: 'Travas elétricas'
Acessorios[-1]              #Acessar o ultimo item da lista. Equivale a Acessorios[7]. Saída: 'Sensor de chuva'

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', ['Rodas de liga', 'Travas elétricas'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
Carros = [Carro_1, Carro_2]
Carros

Carros[0]               #Saída:['Jetta Variant', 'Motor 4.0 Turbo', ['Rodas de liga', 'Travas elétricas'], 88078.64]
Carros[0][0]            #Acessar informações dentro desta lista. Saída: 'Jetta Variant'
Carros[0][-2]           #Saída: ['Rodas de liga', 'Travas elétricas']
Carros[0][-2][1]        #Saída: 'Travas elétricas'

Acessorios[2:5]         #Saída: ['Piloto automático', 'Bancos de couro', 'Ar condicionado']. Como o fatiamento é não-inclusivo, somente os itens de índice 2 a 4 foram listados.

Acessorios[2:]          #Saída: ['Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']. Itens a partir do índice 2 até o final.
```