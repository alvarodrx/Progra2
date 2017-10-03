import pygame
import random
import pygbutton
from tkinter.filedialog import *
import kakuroMaker
import pprint #Se debe instalar a traves de pycharm
import numpy as np
import time
import os

blueP = (20,10,255)#(20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
whiteP = (255,255,255)
BLACK = (0, 0, 0)
grayP = (15, 15, 15)
colScreen = (0, 0, 0)
colVar = [0,0,0]


Fuente = pygame.font.Font(None, 20)
FuenteG = pygame.font.Font(None, 20)
fontSize = 10

gameList = "NoIniciada"

px = 0
py = 0

x = 0
y = 0

tamaño = 0
sizeSquare = 0
tamPlantilla = 0
size = 0
screen = ""

gameOver = False

newGameButton = ""
saveGameButton = ""
solveGameButton = ""

def loadFile():
    game = []
    try:
        load = askopenfilename(filetypes=[("Archivos sav", "*.sav")])
        if load == "":
            return []
        saved = open(load, "r")
        game = eval(saved.readline())
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
    global colScreen
    colVar[random.randrange(0, 3)] = random.randrange(10, 70)
    colScreen = (colVar[0],colVar[1],colVar[2])#(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    screen.fill(colScreen)
    halfSquareSize = sizeSquare // 2
    Ti = 0
    for i in range(1, size[0], sizeSquare):
        Tj = 0
        for j in range(1, size[0], sizeSquare):
            if gameList[Tj][Ti] == [] :
                pygame.draw.rect(screen, BLACK, [i, j, sizeSquare - 1, sizeSquare - 1], 0)  # (screen, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)), [i, j, sizeSquare-1, sizeSquare-1], 0)
            elif len(gameList[Tj][Ti]) == 1 :
                pygame.draw.rect(screen, whiteP, [i, j, sizeSquare-1, sizeSquare-1], 0)#(screen, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)), [i, j, sizeSquare-1, sizeSquare-1], 0)
                actVal = gameList[Tj][Ti][0]
                if actVal != 0:
                    valCell = Fuente.render(str(actVal), True, BLACK)
                    screen.blit(valCell, [i + halfSquareSize, j + halfSquareSize])
            elif len(gameList[Tj][Ti]) == 2 :
                valRC = gameList[Tj][Ti]
                pygame.draw.rect(screen, grayP, [i, j, sizeSquare-1, sizeSquare-1], 0)#(screen, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)), [i, j, sizeSquare-1, sizeSquare-1], 0)
                if valRC[0] != 0:
                    valRow = Fuente.render(str(valRC[0]), True, whiteP)
                    screen.blit(valRow, [i + halfSquareSize - fontSize, j + (sizeSquare*0.7//1)])
                if valRC[1] != 0:
                    valCol = Fuente.render(str(valRC[1]), True, whiteP)
                    screen.blit(valCol, [i + (sizeSquare*0.7//1), j + halfSquareSize - fontSize])
                pygame.draw.line(screen, whiteP, [i+1, j+1], [i + sizeSquare - 1, j + sizeSquare - 1], 1)

            Tj += 1
        Ti += 1
    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

    newGameButton.draw(screen)
    saveGameButton.draw(screen)
    solveGameButton.draw(screen)
    pygame.display.flip()

def inicio():
    global gameList,gameOver, screen, tamaño, sizeSquare, tamPlantilla, size, newGameButton, saveGameButton, solveGameButton, Fuente, FuenteG, colScreen

    #Rutina de inicializacion
    print("Desea cargar un tablero guardado? S/N ")
    cargar = input("- ")
    if cargar == "S":
        gameList = loadFile()
        print(str(type(gameList)))
        pprint.pprint(gameList)
        if type(gameList) == list:
            print("Tablero cargado con exito")
        tamaño = len(gameList)
    else:
        tamaño = int(eval(input("Tamaño del tablero: ")))
        gameList = kakuroMaker.kakuroMaker(tamaño).getNewBoard() #generate()
        print("Desea guardar el tablero nuevo? S/N ")
        guardar = input("- ")
        if guardar == "S":
            saveFile(gameList)
        pprint.pprint(gameList)
    #Configuracion de pantalla
    sizeSquare = 650 // tamaño
    tamPlantilla = tamaño * sizeSquare
    size = (tamPlantilla, tamPlantilla + 50)
    newGameButton = pygbutton.PygButton((10, tamPlantilla + 5, 200, 40), 'Generar nuevo', redP, colScreen, Fuente)
    saveGameButton = pygbutton.PygButton((tamPlantilla / 2 - 100, tamPlantilla + 5, 200, 40), 'Guardar juego', greenP, colScreen, Fuente)
    solveGameButton = pygbutton.PygButton((tamPlantilla / 2 + 110, tamPlantilla + 5, 200, 40), 'Resolver juego', blueP, colScreen, Fuente)
    fontSize = sizeSquare // 3
    Fuente = pygame.font.Font(None, fontSize)
    FuenteG = pygame.font.Font(None, fontSize)
    screen = pygame.display.set_mode(size)
    pygame.init()
    pygame.display.set_caption("KA-KUR-OH!")
    # pygame.display.set_caption("Grid on PYGAME")
    clock = pygame.time.Clock()

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if 'click' in newGameButton.handleEvent(event):
                gameList = kakuroMaker.kakuroMaker(tamaño).getNewBoard() #generate()
            if 'click' in saveGameButton.handleEvent(event):
                saveFile(gameList)
            if 'click' in solveGameButton.handleEvent(event):
                print("T LA KREISTE WE!")
        drawGrid()
        clock.tick(10)

sys.setrecursionlimit(10000)
inicio()
pygame.quit()