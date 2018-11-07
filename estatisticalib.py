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

def getQuartil1(dados):
    tamanho = len(dados)
    dadosOrdenado = sorted(dados)
    
    if tamanho % 2:
        index = int(tamanho/2)
        return getMediana(dadosOrdenado[:index+1])
    else:
        index = int(tamanho/2)
        return getMediana(dadosOrdenado[:index])
    
def getQuartil2(dados):
    return getMediana(dados)

def getQuartil3(dados):
    tamanho = len(dados)
    dadosOrdenado = sorted(dados)
    index = int(tamanho/2)
    return getMediana(dadosOrdenado[index:])

def getDistanciaInterquartil(dados):
    return getQuartil3(dados) - getQuartil1(dados)

##########
#
# IDENTIFICAÇÃO DE DISCREPÂNCIA - OUTLIERS
#
###################
    
def getIntervaloOutliersPoucoResistente(dados):
    """Indentificação de outliers baseado em medidas pouco resistente. Os\
    outliers estão fora do (valorInferior, valorSuperior)"""
    media = getMedia(dados)
    desvioPadrao = getDesvioPadrao(dados)
    valorInferior = media - 3 * desvioPadrao
    valorSuperior = media + 3 * desvioPadrao
    return (valorInferior, valorSuperior)

def getIntervaloOutliersMaisResistente(dados):
    """Indentificação de outliers baseado em medidas mais resistente. Os\
    outliers estão fora do (valorInferior, valorSuperior)"""
    quartil1 = getQuartil1(dados)
    quartil3 = getQuartil3(dados)
    distanciaInterquartil = getDistanciaInterquartil(dados)
    valorInferior = quartil1 - 3/2 * distanciaInterquartil
    valorSuperior = quartil3 + 3/2 * distanciaInterquartil
    return (valorInferior, valorSuperior)

##########
#
# CORRELAÇÃO
#
###################

def getCoefDeCorrelacao(dadosX, dadosY):
    tamanho = len(dadosX)
    somatorioXmultY = sum([dadosX[i] * dadosY[i] for i in range(tamanho)])
    mediaX = getMedia(dadosX)
    mediaY = getMedia(dadosY)
    
    somatorioXpow2 = sum([pow(x,2) for x in dadosX])
    somatorioYpow2 = sum([pow(y,2) for y in dadosY])
    
    rxy = (somatorioXmultY-tamanho*mediaX*mediaY)/ \
    pow((somatorioXpow2-tamanho*pow(mediaX,2))*(somatorioYpow2-tamanho*pow(mediaY,2)),1/2)
    
    return rxy

def getCovariancia(dadosX, dadosY):
    coefCorrelacao = getCoefDeCorrelacao(dadosX, dadosY)
    desvioPadraoX = getDesvioPadrao(dadosX)
    desvioPadraoY = getDesvioPadrao(dadosY)
    sxy = coefCorrelacao * desvioPadraoX *  desvioPadraoY
    return sxy
