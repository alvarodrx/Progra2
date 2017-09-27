import random
import numpy as np
import pprint

gameList = []
size = 14

# array = np.arange(random.randrange(1, 5),random.randrange(5,10))
# pprint.pprint(array)
# sal = np.sum(array)
# salList = array.tolist()
# print(salList)
# print(len(array))
#
# gameList.append(1)
# gameList.append(sal)
#
# pprint.pprint(gameList)


def getSumForNumer(number): #Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
    numberList = []
    numberList += np.arange(1, 10).tolist() #Creo lista del 1 al 9
    suma = 0
    for i in range(0,number):
        indice = random.randrange(0, len(numberList)) #Obtiene un indice de la lista
        numObt = numberList[indice] #obtiene el numero de la lista
        suma += numObt
        #print(numObt)
        numberList.remove(numObt) #
    #pprint.pprint(numberList)
    return suma

####################################################################
### Cambiar a 0 y 1 y delegar decicion al de relleno
for i in range(0, size):
    raw = []
    for j in range(0, size):
        if j == (size-1):
            if i == (size-1):
                raw.append(0) # En la esquina de abajo siempre va un 0
            else:
                typeCell = random.randrange(0, 2)*2 # 0 o 2
                raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
        elif i == (size-1):
            typeCell = random.randrange(0, 2)   # 0 o 1
            raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
        else:
            typeCell = random.randrange(0, 4)  # 0 o 1
            raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
    gameList.append(raw)
    raw = []

pprint.pprint(gameList)


for i in range(0, size):
    for j in range(0, size):
        if gameList[i][j] == 0:
            gameList[i][j] = []
        elif gameList[i][j] == 1:
            if i == 0:
                if (len(gameList) - j) > 10:
                    numberOfCells = random.randrange(1, 10)
                    newRowVal = getSumForNumer(numberOfCells)
                    gameList[i][j] = [0,newRowVal]
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j+1, j+numberOfCells+1):
                        #print("ka: ",k)
                        gameList[i][k] = [0]
                    j = j+numberOfCells+1
                    gameList[i][j] = []
                elif (len(gameList) - j) >= 2:
                    numberOfCells = random.randrange(1, len(gameList) - j)
                    newRowVal = getSumForNumer(numberOfCells)
                    gameList[i][j] = [0,newRowVal]
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j + 1, j + numberOfCells + 1):
                        #print("ka: ", k)
                        gameList[i][k] = [0]
                    j = j + numberOfCells + 1
                    #gameList[i][j] = []
                else:
                    for k in range(j, len(gameList)):
                        gameList[i][k] = [0]
                    j = size
            else: #Evita adyacencia con columnas
                if (len(gameList) - j) > 10:
                    numberOfCells = random.randrange(1, 10)
                    while type(gameList[i][j+numberOfCells+1]) is list: ## Evita que coloque una fila adyacente a una columna
                        print("Adyacencia f-c")
                        numberOfCells = random.randrange(1, 10)
                    newRowVal = getSumForNumer(numberOfCells)
                    gameList[i][j] = [0,newRowVal]
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j+1, j+numberOfCells+1):
                        #print("ka: ",k)
                        gameList[i][k] = [0]
                    j = j+numberOfCells+1
                    gameList[i][j] = []
                elif (len(gameList) - j) >= 2:
                    numberOfCells = random.randrange(1, len(gameList) - j)
                    if (j + numberOfCells) > len(gameList):
                        while type(gameList[i][j + numberOfCells + 1]) is list:  ## Evita que coloque una fila adyacente a una columna
                            print("Adyacencia f-c")
                            numberOfCells = random.randrange(1, len(gameList) - j)
                    newRowVal = getSumForNumer(numberOfCells)
                    gameList[i][j] = [0,newRowVal]
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j + 1, j + numberOfCells + 1):
                        #print("ka: ", k)
                        gameList[i][k] = [0]
                    j = j + numberOfCells + 1
                    #gameList[i][j] = []
                else:
                    for k in range(j, len(gameList)):
                        gameList[i][k] = []
                    j = len(gameList)


        elif gameList[i][j] == 2:
            if (len(gameList) - i) > 10:
                numberOfCells = random.randrange(1, 10)
                newColVal = getSumForNumer(numberOfCells)
                gameList[i][j] = [newColVal, 0]
                print("new val cell: ", newColVal)
                print("new col cells: ", numberOfCells)
                for k in range(i+1, i+numberOfCells+1):
                    #print("ka: ",k)
                    gameList[k][j] = [0]
                gameList[i+numberOfCells+1][j] = []
            elif (len(gameList) - i) >= 2:
                numberOfCells = random.randrange(1, len(gameList) - i)
                newColVal = getSumForNumer(numberOfCells)
                gameList[i][j] = [newColVal, 0]
                print("new val cell: ", newColVal)
                print("new col cells: ", numberOfCells)
                for k in range(i+1, i+numberOfCells+1):
                    #print("ka: ",k)
                    gameList[k][j] = [0]
                #gameList[i+numberOfCells+1][j] = []
            else:
                for k in range(i, len(gameList)):
                    gameList[k][j] = []

        elif gameList[i][j] == 3:
            newCRVal = [0, 0]
            #inicio por la columna por que no requiere desplazamiento
            if (len(gameList) - i) > 10:
                numberOfCells = random.randrange(1, 10)
                newColVal = getSumForNumer(numberOfCells)
                newCRVal[0] = newColVal
                print("new val cell: ", newColVal)
                print("new col cells: ", numberOfCells)
                for k in range(i+1, i+numberOfCells+1):
                    #print("ka: ",k)
                    gameList[k][j] = [0]
                gameList[i+numberOfCells+1][j] = []
            elif (len(gameList) - i) >= 2:
                numberOfCells = random.randrange(1, len(gameList) - i)
                newColVal = getSumForNumer(numberOfCells)
                newCRVal[0] = newColVal
                print("new val cell: ", newColVal)
                print("new col cells: ", numberOfCells)
                for k in range(i+1, i+numberOfCells+1):
                    #print("ka: ",k)
                    gameList[k][j] = [0]
                #gameList[i+numberOfCells+1][j] = []
            else:
                for k in range(i, len(gameList)):
                    gameList[k][j] = []

            #Ahora hago la fila..
            if i == 0:
                if (len(gameList) - j) > 10:
                    numberOfCells = random.randrange(1, 10)
                    newRowVal = getSumForNumer(numberOfCells)
                    newCRVal[1] = newRowVal
                    gameList[i][j] = newCRVal
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j+1, j+numberOfCells+1):
                        #print("ka: ",k)
                        gameList[i][k] = [0]
                    j = j+numberOfCells+1
                    gameList[i][j] = []
                elif (len(gameList) - j) >= 2:
                    numberOfCells = random.randrange(1, len(gameList) - j)
                    newRowVal = getSumForNumer(numberOfCells)
                    newCRVal[1] = newRowVal
                    gameList[i][j] = newCRVal
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j + 1, j + numberOfCells + 1):
                        #print("ka: ", k)
                        gameList[i][k] = [0]
                    j = j + numberOfCells + 1
                    #gameList[i][j] = []
                else:
                    for k in range(j, len(gameList)):
                        gameList[i][k] = [0]
                    j = size
            else: #Evita adyacencia con columnas
                if (len(gameList) - j) > 10:
                    numberOfCells = random.randrange(1, 10)
                    while type(gameList[i][j+numberOfCells+1]) is list: ## Evita que coloque una fila adyacente a una columna
                        print("Adyacencia f-c")
                        numberOfCells = random.randrange(1, 10)
                    newRowVal = getSumForNumer(numberOfCells)
                    newCRVal[1] = newRowVal
                    gameList[i][j] = newCRVal
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j+1, j+numberOfCells+1):
                        #print("ka: ",k)
                        gameList[i][k] = [0]
                    j = j+numberOfCells+1
                    gameList[i][j] = []
                elif (len(gameList) - j) >= 2:
                    numberOfCells = random.randrange(1, len(gameList) - j)
                    if (j + numberOfCells) > len(gameList):
                        while type(gameList[i][j + numberOfCells + 1]) is list:  ## Evita que coloque una fila adyacente a una columna
                            print("Adyacencia f-c")
                            numberOfCells = random.randrange(1, len(gameList) - j)
                    newRowVal = getSumForNumer(numberOfCells)
                    newCRVal[1] = newRowVal
                    gameList[i][j] = newCRVal
                    print("new val cell: ", newRowVal)
                    print("new row cells: ", numberOfCells)
                    for k in range(j + 1, j + numberOfCells + 1):
                        #print("ka: ", k)
                        gameList[i][k] = [0]
                    j = j + numberOfCells + 1
                    #gameList[i][j] = []
                else:
                    for k in range(j, len(gameList)):
                        gameList[i][k] = []
                    j = len(gameList)

for i in range(0, len(gameList)):
    print(gameList[i])
