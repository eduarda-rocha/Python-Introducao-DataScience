# Trabalhando com arrays Numpy


import numpy as np                                  #importação da biblioteca

km = np.loadtxt('carros-km.txt')                    #receberá um array numpy e carrega o arquivo TXT passado
km                                                  #visualizar o conteúdo da variável

anos = np.loadtxt('carros-anos.txt', dtype = int)   #também possível definir o tipo de dado da variável
anos

km_media = km / (2022 - anos)                       #calculo da quilometragem anual média
km_media
type(km_media)                                      #retornará um numpy.ndarray

