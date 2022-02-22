# Loop For Aninhado

```
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados

for lista in dados:                 #Saída: imprime as três listas
    print(lista)

for lista in dados:                 #Saída: imprime todos os itens das três listas
    for item in lista: 
        print(item)

Acessorios = []                     #Adicionar à lista Acessorios os itens das três listas
for lista in dados:
  for item in lista:
        Acessorios.append(item)     
print(Acessorios)

list(set(Acessorios))               #Método set() usado para remoção de duplicatas em uma sequência

list(set([item for lista in dados for item in lista])) #list comprehensions. Mesmo código porém compacto

```