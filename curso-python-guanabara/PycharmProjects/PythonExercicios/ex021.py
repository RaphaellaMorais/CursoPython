import pygame
pygame.init() #iniciando o pygame
pygame.mixer.music.load('ex21.mp3')  #arquivo mp3 que eu colei no projeto
pygame.mixer.music.play()  #iniciar música
pygame.event.wait()  #finalizar

#tem que ter o arquivo também em mp3 e depois copiar + botão direito colar em Paste;
#evitar que o nome do arquivo tenha acentuações e espaçoes, nome simples com letras minuscilas;

#pygame não vai estar inslado, tem que instalar - clica la lampada + install package pygame;
