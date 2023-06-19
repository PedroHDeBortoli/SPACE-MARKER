import pygame
from tkinter import simpledialog
from estrelas import adicionar_estrelas, desenhar_estrelas, desenhar_linhas

pygame.init()
tamanho = (800, 600)
branco = (255, 255, 255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("bg.jpg")
pygame.display.set_caption("SPACE MARKER")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
estrelas = {}
fonte = pygame.font.Font(None, 22)
deslocamentox = 15
running = True

def salvar_pontos():
    with open('pontos.txt', 'w') as file:
        for nome, posicao in estrelas.items():
            file.write(nome + ',' + str(posicao[0]) + ',' + str(posicao[1]) + '\n')
    print('Pontos salvos')

def carregar_pontos():
    estrelas.clear()
    try:
        with open('pontos.txt', 'r') as file:
            for line in file:
                nome, x, y = line.rstrip('\n').split(',')
                estrelas[nome] = (int(x), int(y))
        print('Pontos carregados')
    except FileNotFoundError:
        print('Nenhum arquivo de pontos enmcontrado')

def excluir_pontos():
    estrelas.clear()
    print('Todas as marcações foram excluidas')

comandos = [
    'Pressione F10 para Salvar os Pontos',
    'Pressione F11 para Carregar os Pontos',
    'Pressione F12 para Excluir Todas as Marcações'
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space', 'Nome da Estrela:')
            print(item)
            if item is None or item.strip() == "":
                item = "desconhecido"
            estrelas[item] = pos

    tela.fill(branco)
    tela.blit(fundo, (0, 0))

    desenhar_estrelas(tela, estrelas, fonte, deslocamentox)
    desenhar_linhas(tela, estrelas, fonte)

    for i in range(len(comandos)):
        comando = comandos[i]
        tela.blit(fonte.render(comando, True, branco), (10, 10 + i * 30))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_F10]:
            salvar_pontos()
        
        if keys [pygame.K_F11]:
            carregar_pontos()

        if keys[pygame.K_F12]:
            excluir_pontos()

    pygame.display.update()
    clock.tick(40)

pygame.quit()