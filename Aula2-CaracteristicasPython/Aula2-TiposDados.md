# Testes simples para alguns tipos de dados

```
ano_atual = 2022
type(ano_atual)         #retornará int

km_total = 44410.0
type(km_total)          #retornará float

zero_km = True
type(zero_km)           #retornará bool

nome = 'Jetta Variant'  #tipo string pode ser declarado com aspas simples
type(nome)              #retornará str, ou seja, string

nome = "Jetta Variant"  #tipo string pode ser declarado com aspas duplas
type(nome)              #retornará str, ou seja, string

carro = '''             #Armazenar strings com mais de uma linha, utilizando três aspas simples ou duplas.
  Nome
  Quilometragem
  Ano
''' 
type(carro)             #retornará str

quilometragem = None
type(quilometragem)     #retornará NoneType
```