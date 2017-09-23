import pygame
import random
import pygbutton

blueP = (30,30,30)#(20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
whiteP = (255,255,255)
BLACK = (0, 0, 0)

Fuente = pygame.font.Font(None, 16)


#px = int(eval(input("Coordenada en X: ")))
#py = int(eval(input("Coordenada en Y: ")))
px = 0
py = 0

x = 0
y = 0
pygame.init()
tamaño = int(eval(input("Tamaño del X x X: "))) +1
sizeSquare = 650//tamaño
tamPlantilla = tamaño * sizeSquare

size = (tamPlantilla, tamPlantilla+sizeSquare)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

colVar = [0,0,0]

buttonObj = pygbutton.PygButton((tamPlantilla/2-100,tamPlantilla + 3, 200, sizeSquare), 'Button Caption',whiteP,blueP,Fuente)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if 'click' in buttonObj.handleEvent(event):
            print("responde el boton")

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
    clock.tick(10)
pygame.quit()