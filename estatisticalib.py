# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:21:18 2018

@author: elenildosantana
@link  : https://github.com/elenildosantana
"""
import math

##########
#
# MEDIDAS DE CENTRALIDADE
#
##########

def getMedia(dados):
    return sum(dados)/len(dados)

def getMediana(dados):
    tamanho = len(dados)
    dadosOrdenados = sorted(dados)
    
    if tamanho % 2:
        index = int(tamanho/2)
        return dadosOrdenados[index]
    else:
        index1 = int(tamanho/2)-1
        index2 = int(tamanho/2)
        return getMedia([dadosOrdenados[index1], dadosOrdenados[index2]])  

###########
#
# MEDIDAS DE DISPERSÃO
#
###########

def getVariancia(dados):
    media = getMedia(dados)
    tamanho = len(dados)
    somatorio = sum([pow(valor,2) for valor in dados])
    variancia = (somatorio - tamanho * pow(media,2))/(tamanho-1)
    return variancia

def getDesvioPadrao(dados):
    return math.sqrt(abs(getVariancia(dados)))

def getCoefDeVariacao(dados):
    return getDesvioPadrao(dados)/getMedia(dados)
