# Estrutura de repetição FOR

```
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

for item in Acessorios: 
  print(item)

for i in range(10):
    print(i ** 2)

quadrado = []
for i in range(10):
    quadrado.append(i ** 2)

quadrado

[i ** 2 for i in range(10)]             #Mesmo código porém escrito em uma linha

```