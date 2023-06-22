import pygame
from tkinter import simpledialog

def adicionar_estrelas():
    posicao = pygame.mouse.get_pos()
    nome = simpledialog.askinteger('Space','Noma da Estrela:')
    return nome

def desenhar_estrelas(tela, estrelas, fonte, deslocamentox):
    cor = (255, 255, 255)
    for nome, posicao in estrelas.items():
        nome = str(nome)
        pygame.draw.circle(tela, cor, posicao, 10)
        texto = fonte.render(nome, True, cor)
        textoX = posicao[0] + deslocamentox
        textoY = posicao[1]
        tela.blit(texto, (textoX, textoY))
        coordenada = fonte.render('(' + str(posicao[0]) + ',' + str(posicao[1]) + ')', True, cor)
        tela.blit(coordenada, (posicao[0] + deslocamentox, posicao[1] + 20))

def desenhar_linhas(tela, estrelas, fonte):
    cor = (255, 255, 255)
    estrelasLista = list(estrelas.values())
    if len(estrelasLista) >= 2:
        for i in range(1, len(estrelasLista)):
            anterior = estrelasLista[i-1]
            atual = estrelasLista[i]
            distanciaX = atual[0] - anterior[0]
            distanciaY = atual[1] - anterior[1]
            total = ((distanciaX ** 2) + (distanciaY ** 2)) ** 0.5
            if total > 20:
                pygame.draw.line(tela, cor, atual, anterior)
                
            soma = abs(distanciaX) + abs(distanciaY)
            distancias = fonte.render(str(int(soma)), True, cor)
            centroX = (atual[0] + anterior[0]) // 2 + 10
            centroY = (atual[1] + anterior[1]) // 2 + 10
            tela.blit(distancias, (centroX, centroY))   