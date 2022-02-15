# Métodos de Listas

```
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

Acessorios.sort()                         #Ordena a lista sendo ordem alfabética ou numérica
Acessorios                                #Saída:['Ar condicionado', 'Bancos de couro', 'Piloto automático', 'Rodas de liga', 'Sensor crepuscular', 'Sensor de chuva', 'Sensor de estacionamento', 'Travas elétricas']

Acessorios.append('4 x 4')                #Adiciona um elemento passado como parâmetro ao final da lista
Acessorios                                #Saída:['Ar condicionado', 'Bancos de couro', 'Piloto automático', 'Rodas de liga', 'Sensor crepuscular', 'Sensor de chuva', 'Sensor de estacionamento', 'Travas elétricas', '4 x 4']

Acessorios.pop()                           #Se não passarmos nenhum parâmetro, ele removerá o último elemento da lista

Acessorios_2 = Acessorios.copy()           #Fazer uma cópia de uma lista
Acessorios_2

Acessorios_2 = Acessorios[:]               #Equivalente a Acessorios.copy()  
```