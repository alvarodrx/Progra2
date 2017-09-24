import pygame
import random
import pygbutton
from tkinter import filedialog
import time
import os

blueP = (30,30,30)#(20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
whiteP = (255,255,255)
BLACK = (0, 0, 0)

Fuente = pygame.font.Font(None, 16)

gameList = "NoIniciada"

#px = int(eval(input("Coordenada en X: ")))
#py = int(eval(input("Coordenada en Y: ")))
px = 0
py = 0

x = 0
y = 0

tamaño = int(eval(input("Tamaño del X x X: ")))

sizeSquare = 650//tamaño
tamPlantilla = tamaño * sizeSquare

size = (tamPlantilla, tamPlantilla+50)
screen = ""
gameOver = False

colVar = [0,0,0]

buttonObj = pygbutton.PygButton((tamPlantilla/2-100,tamPlantilla + 5, 200, 40), 'Button Caption',whiteP,blueP,Fuente)

def loadFile():
    game = []
    try:
        load = filedialog.askopenfilename(filetypes=[("Archivos sav", "*.sav")])
        if load == "":
            return []
        saved = open(load, "r")
        game = saved.readline()
        game = eval(game)
        saved.close()
        return game
    except:
        return game

def saveFile(game):
    archivo = asksaveasfilename(defaultextension=".sav")
    try:
        save = open(archivo, "a")
        save.write(str(game))
        save.close()
        return
    except:
        return

def drawGrid():
    colVar[random.randrange(0, 3)] = random.randrange(100, 255)
    colScreen = (colVar[0],colVar[1],colVar[2])#(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    screen.fill(colScreen)
    Fuente = pygame.font.Font(None, 16)
    Tx = 0
    Ty = 0
    for i in range(1, size[0], sizeSquare):
        for j in range(1, size[1]-sizeSquare, sizeSquare):
            pygame.draw.rect(screen, BLACK, [i, j, sizeSquare-1, sizeSquare-1], 0)#(screen, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)), [i, j, sizeSquare-1, sizeSquare-1], 0)
            if py == 0:
                y = 1
            elif py == Ty:
                y = j
            Ty += 1
        if px == 0:
            x = 1
        elif px == Tx:
            x = i
        Texto = Fuente.render(str(Tx), True, whiteP)
        screen.blit(Texto, [i+2, 2])
        if Tx != 0:
            screen.blit(Texto, [2, i+2])
        Tx += 1
        Ty = 0
    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

    #pygame.draw.rect(screen, colAl, [x, y, sizeSquare-1, sizeSquare-1], 0)
    #start_button = pygame.draw.rect(screen, (200, 200, 200), (tamPlantilla, tamPlantilla-sizeSquare, 100, 50));
    buttonObj.draw(screen)
    pygame.display.flip()

def inicio():
    global gameList,gameOver, screen
    print(gameList)
    gameList = loadFile()
    print(gameList)
    pygame.init()
    pygame.display.set_caption("Grid on PYGAME")
    screen = pygame.display.set_mode(size)
    # pygame.display.set_caption("Grid on PYGAME")
    clock = pygame.time.Clock()
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if 'click' in buttonObj.handleEvent(event):
                print("responde el boton")
        drawGrid()
        clock.tick(10)

inicio()
pygame.quit()