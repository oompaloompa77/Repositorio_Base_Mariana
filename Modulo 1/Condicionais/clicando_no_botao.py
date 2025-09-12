import pygame # Importa a biblioteca Pygame

pygame.init() # Inicializa o Pygame
tela = pygame.display.set_mode((400, 300)) # Define o tamanho da tela
fonte = pygame.font.SysFont(None, 36) # Fonte padrão do sistema 

def desenhar_botao(texto,posicao,cor):
    texto_render = fonte.render(texto, True, (0, 0, 0))
    retangulo = texto_render.get_rect(center = posicao)
    pygame.draw.rect(tela, cor, retangulo.inflate(20, 20))  # Botão com margem
    tela.blit(texto_render, retangulo)
    return retangulo

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(evento.pos):
                print("Botão clicado!")

    tela.fill((220,220,220))  # Preenche a tela com branco
    botao = desenhar_botao("Clique Aqui", (200, 150), (100, 200, 100))  # Botão verde
    pygame.display.update()

pygame.quit()  # Encerra a tela
