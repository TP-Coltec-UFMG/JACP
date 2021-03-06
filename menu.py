import pygame
from pygame.locals import *
import os
from main import Main

# Game Initialization
pygame.init()
pygame.mixer.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen = pygame.display.set_mode((900, 600))

# Text Renderer


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, False, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Main Menu


def main_menu():
    menu = True
    selected = "start"
    started = False

    while menu:
        if not started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            pygame.mixer.music.load('assets/sounds/item-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            started = True
                        if selected == "quit":
                            pygame.mixer.music.load('assets/sounds/item-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            pygame.quit()
        if started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected = "normal"
                    elif event.key == pygame.K_2:
                        selected = "protanopia"
                    elif event.key == pygame.K_3:
                        selected = "deuteranopia"
                    elif event.key == pygame.K_4:
                        selected = "tritanopia"
                    if event.key == pygame.K_RETURN:
                        if selected == "normal":
                            pygame.mixer.music.load('assets/sounds/gamemode-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            main = Main(selected)
                            main.__init__(selected)
                        elif selected == "protanopia":
                            pygame.mixer.music.load('assets/sounds/gamemode-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            main = Main(selected)
                            main.__init__(selected)
                        elif selected == "deuteranopia":
                            pygame.mixer.music.load('assets/sounds/gamemode-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            main = Main(selected)
                            main.__init__(selected)
                        elif selected == "tritanopia":
                            pygame.mixer.music.load('assets/sounds/gamemode-selected-menu.wav')
                            pygame.mixer.music.play(0)
                            main = Main(selected)
                            main.__init__(selected)

        # Main Menu UI
        if not started:
            screen.fill(black)
            title = text_format("Jornada por Gavendish", font, 90, yellow)
            if selected == "start":
                textStart = text_format("INICIAR", font, 75, yellow)
            else:
                textStart = text_format("INICIAR", font, 75, white)
            if selected == "quit":
                textQuit = text_format("SAIR", font, 75, yellow)
            else:
                textQuit = text_format("SAIR", font, 75, white)

            titleRect = title.get_rect()
            startRect = textStart.get_rect()
            quitRect = textQuit.get_rect()

            # Main Menu Text
            screen.blit(title, (900/2 - (titleRect[2]/2), 80))
            screen.blit(textStart, (900/2 - (startRect[2]/2), 300))
            screen.blit(textQuit, (900/2 - (quitRect[2]/2), 360))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Jornada por Gavendish")

        # Sub Menu UI
        if started:
            screen.fill(black)
            title = text_format("Selecione o modo de jogo", font, 90, yellow)
            subtitle = text_format("Aperte de 1 a 4 para selecionar", font, 40, yellow)
            if selected == "normal":
                textNormal = text_format("1. NORMAL", font, 75, yellow)
            else:
                textNormal = text_format("1. NORMAL", font, 75, white)
            if selected == "protanopia":
                textProtanopia = text_format("2. PROTANOPIA", font, 75, yellow)
            else:
                textProtanopia = text_format("2. PROTANOPIA", font, 75, white)
            if selected == "deuteranopia":
                textDeuteranopia = text_format("3. DEUTERANOPIA", font, 75, yellow)
            else:
                textDeuteranopia = text_format("3. DEUTERANOPIA", font, 75, white)
            if selected == "tritanopia":
                textTritanopia = text_format("4. TRITANOPIA", font, 75, yellow)
            else:
                textTritanopia = text_format("4. TRITANOPIA", font, 75, white)

            normalRect = textNormal.get_rect()
            protanopiaRect = textProtanopia.get_rect()
            deuteranopiaRect = textDeuteranopia.get_rect()
            tritanopiaRect = textTritanopia.get_rect()
            titleRect = title.get_rect()
            subtitleRect = subtitle.get_rect()

            # Sub Menu Text
            screen.blit(title, (900 / 2 - (titleRect[2] / 2), 80))
            screen.blit(subtitle, (900 / 2 - (subtitleRect[2] / 2), 160))
            screen.blit(textNormal, (900 / 2 - (normalRect[2] / 2), 240))
            screen.blit(textProtanopia, (900 / 2 - (protanopiaRect[2] / 2), 300))
            screen.blit(textDeuteranopia, (900 / 2 - (deuteranopiaRect[2] / 2), 360))
            screen.blit(textTritanopia, (900 / 2 - (tritanopiaRect[2] / 2), 420))

            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Jornada por Gavendish")
# Initialize the Game


main_menu()
pygame.quit()
