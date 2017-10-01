import random
import pprint
import numpy as np
from itertools import *



class kakuroMaker:
    game = False
    gameSize = 0
    def __init__(self,size):
        self.game = True
        self.gameSize = size

    def getSumForNumer(self, number):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
        numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #numberList += np.arange(1, 10).tolist()  # Creo lista del 1 al 9
        suma = 0
        for i in range(0, number):
            indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
            numObt = numberList[indice]  # obtiene el numero de la lista
            suma += numObt
            # print(numObt)
            numberList.remove(numObt)  #
        # pprint.pprint(numberList)
        return suma

    def getArrayForNumer(self, number):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
        numberList = [1,2,3,4,5,6,7,8,9]
        suma = []
        for i in range(0, number):
            indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
            numObt = numberList[indice]  # obtiene el numero de la lista
            suma.append(numObt)
            # print(numObt)
            numberList.remove(numObt)  #
        #pprint.pprint(numberList)
        return suma

    def getArrayForArray(self, array):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
        numberList = [1,2,3,4,5,6,7,8,9]
        listReturn = []
        for i in array:
            if (type(i) is list) and len(i) == 1:
                numberList.remove(i[0])
        for i in array:
            if (type(i) is list) and len(i) == 1:
                listReturn.append(i)
            else:
                indice = 0
                if len(numberList) > 1:
                    indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
                else:
                    indice = 0
                numObt = numberList[indice]  # obtiene el numero de la lista
                listReturn.append([numObt])
                numberList.remove(numObt)  #
        return listReturn

    def repeatsOnArray(self, array): #Busca repeticiones en una lista
        compArray = [] #lista de comparacion
        if array:
            for i in array:
                if (type(i) is list) and len(i) == 1:
                    if compArray.count(i[0]) > 0:
                        return True
                    compArray.append(i[0])
        return False

    def repeatsOnArray2(self, array): #Busca repeticiones en una lista
        compArray = [] #lista de comparacion
        if array:
            for i in array:
                if compArray.count(i) > 0:
                    return True
                compArray.append(i)
        return False




    def getNewGame(self):
        size = self.gameSize
        gameList = []
        for i in range(0, size):
            raw = []
            for j in range(0, size):
                if random.randrange(0, 2) == 0:
                    raw.append(0)
                else:
                    if i == 0:
                        if j == 0:
                            typeCell = 0
                            raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
                        else:
                            typeCell = random.randrange(0, 2) * 2  # 0 o 1
                            raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
                    elif j == 0 or i == (size - 1):
                        typeCell = random.randrange(0, 2)   # 0 o 1
                        raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
                    elif j == (size - 1):
                        if i == (size - 1):
                            raw.append(0)  # En la esquina de abajo siempre va un 0
                        else:
                            typeCell = random.randrange(0, 2) * 2  # 0 o 2
                            raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
                    else:
                        typeCell = random.randrange(0, 2) *3  # 0 o 1
                        raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
            gameList.append(raw)
            raw = []

        for i in range(0, size):
            for j in range(0, size):
                if gameList[i][j] == 0:
                    gameList[i][j] = []
                elif gameList[i][j] == 1: #construye columnas
                    if i == 0:
                        if (size - j) > 10:
                            numberOfCells = random.randrange(2, 10)
                            newRowArray = self.getArrayForNumer(numberOfCells) #Lista de numeros
                            newRowVal = np.sum(newRowArray) #Suma de esos numeros
                            gameList[i][j] = [0, newRowVal] #Coloca el valor de los numeros
                            indice = 0
                            j += 1
                            actual = j
                            while j < (actual + numberOfCells):
                                gameList[i][j] = [newRowArray[indice]] #Coloca el valor del indice
                                indice += 1
                                j += 1
                            gameList[i][j] = [] #Final de la lista
                        elif (size - j) > 2:
                            numberOfCells = random.randrange(2, size - j)
                            newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                            newRowVal = np.sum(newRowArray)  # Suma de esos numeros
                            gameList[i][j] = [0, newRowVal]  # Coloca el valor de la suma de los numeros
                            indice = 0
                            j += 1
                            actual = j
                            while j < (actual + numberOfCells):
                                gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
                                indice += 1
                                j += 1
                            if j < size:
                                gameList[i][j] = []
                        else:
                            for k in range(j, size):
                                gameList[i][k] = []
                            j = size

                    else:  # Evita adyacencia con columnas
                        if (size - j) >= 2:
                            thisRow = gameList[i]  # fila actual
                            notRepeatFlag = True  # Indica que no hay repeticiones de numeros en la lista
                            trys = 0
                            valuesList = []
                            posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
                            while notRepeatFlag:
                                position = j + 1  # pociacion de la siguiente celda
                                posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
                                valuesList = []
                                while (trys < (size - j)) and (position < (size - trys)) and (thisRow[position] != []):
                                    valuesList.append(thisRow[position])
                                    position += 1
                                    posibLenght += 1
                                notRepeatFlag = self.repeatsOnArray(valuesList)
                                trys += 1
                                if ((j + posibLenght + 1) < size) and (type(thisRow[j + posibLenght + 1]) is list):
                                    notRepeatFlag = True
                                if trys > 10 or len(valuesList) == 0 or len(valuesList) >= 10:
                                    notRepeatFlag = False
                                    posibLenght = 0
                            if posibLenght != 0:
                                newRowArray = self.getArrayForArray(valuesList)
                                newRowVal = np.sum(newRowArray)
                                gameList[i][j] = [0, newRowVal]
                                indice = 0
                                j += 1
                                actual = j
                                while j < (actual + posibLenght):
                                    gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
                                    indice += 1
                                    j += 1
                                if j < size:
                                    gameList[i][j] = []
                            else:
                                gameList[i][j] = []

                        else:
                            for k in range(j, size):
                                if type(gameList[i][k]) is not list:
                                    gameList[i][k] = []
                            j = len(gameList)

                elif gameList[i][j] == 2: #Construye columnas
                    if (size - i) > 10:
                        numberOfCells = random.randrange(2, 10)
                        newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                        newColVal = np.sum(newColArray) # Suma de la lista
                        gameList[i][j] = [newColVal, 0]
                        indice = 0
                        for k in range(i + 1, i + numberOfCells + 1):
                            gameList[k][j] = [newColArray[indice]]
                            indice += 1
                        gameList[i + numberOfCells + 1][j] = []
                    elif (size - i) > 2:
                        numberOfCells = random.randrange(2, size - i)
                        newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                        newColVal = np.sum(newColArray)  # Suma de la lista
                        gameList[i][j] = [newColVal, 0]
                        indice = 0
                        for k in range(i + 1, i + numberOfCells + 1):
                            gameList[k][j] = [newColArray[indice]]
                            indice += 1
                        if (i+numberOfCells+1) < size:
                            gameList[i+numberOfCells+1][j] = []
                    else:
                        for k in range(i, size):
                            gameList[k][j] = []

                elif gameList[i][j] == 3: #Filas y columnas
                    newCRVal = [0, 0]
                    # inicio por la columna por que no requiere desplazamiento
                    if (size - i) > 10:
                        numberOfCells = random.randrange(2, 10)
                        newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                        newColVal = np.sum(newColArray) # Suma de la lista
                        newCRVal[0] = newColVal
                        indice = 0
                        for k in range(i + 1, i + numberOfCells + 1):
                            gameList[k][j] = [newColArray[indice]]
                            indice += 1
                        gameList[i + numberOfCells + 1][j] = []
                    elif (len(gameList) - i) >= 2:
                        numberOfCells = random.randrange(1, size - i)
                        newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                        newColVal = np.sum(newColArray)  # Suma de la lista
                        newCRVal[0] = newColVal
                        indice = 0
                        for k in range(i + 1, i + numberOfCells + 1):
                            gameList[k][j] = [newColArray[indice]]
                            indice += 1
                        if (i+numberOfCells+1) < size:
                            gameList[i+numberOfCells+1][j] = []

                    if i == 0:
                        if (size - j) > 10:
                            numberOfCells = random.randrange(2, 10)
                            newRowArray = self.getArrayForNumer(numberOfCells) #Lista de numeros
                            newRowVal = np.sum(newRowArray) #Suma de esos numeros
                            newCRVal[1] = newRowVal
                            gameList[i][j] = newCRVal #Coloca el valor de los numeros
                            indice = 0
                            j += 1
                            actual = j
                            while j < (actual + numberOfCells):
                                gameList[i][j] = [newRowArray[indice]] #Coloca el valor del indice
                                indice += 1
                                j += 1
                            gameList[i][j] = [] #Final de la lista
                        elif (size - j) >= 2:
                            numberOfCells = random.randrange(1, size - j)
                            newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
                            newRowVal = np.sum(newRowArray)  # Suma de esos numeros
                            newCRVal[1] = newRowVal
                            gameList[i][j] = newCRVal  # Coloca el valor de la suma de los numeros
                            indice = 0
                            j += 1
                            actual = j
                            while j < (actual + numberOfCells):
                                gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
                                indice += 1
                                j += 1
                            if j < size:
                                gameList[i][j] = []
                        else:
                            for k in range(j, size):
                                gameList[i][k] = []
                            j = size
                    else:  # Evita adyacencia con columnas
                        if (size - j) >= 2:
                            thisRow = gameList[i]  # fila actual
                            notRepeatFlag = True  # Indica que no hay repeticiones de numeros en la lista
                            trys = 0
                            valuesList = []
                            posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
                            while notRepeatFlag:
                                position = j + 1  # pociacion de la siguiente celda
                                posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
                                valuesList = []
                                while (trys < (size - j)) and (position < (size - trys)) and (thisRow[position] != []):
                                    valuesList.append(thisRow[position])
                                    position += 1
                                    posibLenght += 1
                                notRepeatFlag = self.repeatsOnArray(valuesList)
                                trys += 1
                                if ((j + posibLenght + 1) < size) and (type(thisRow[j + posibLenght + 1]) is list):
                                    notRepeatFlag = True
                                if trys > 10 or len(valuesList) == 0 or len(valuesList) >= 10:
                                    notRepeatFlag = False
                                    posibLenght = 0
                            if posibLenght != 0:
                                newRowArray = self.getArrayForArray(valuesList)
                                newRowVal = np.sum(newRowArray)
                                newCRVal[1] = newRowVal
                                gameList[i][j] = newCRVal
                                indice = 0
                                j += 1
                                actual = j
                                while j < (actual + posibLenght):
                                    gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
                                    indice += 1
                                    j += 1
                                if j < size:
                                    gameList[i][j] = []
                            else:
                                newCRVal[1] = 0
                                gameList[i][j] = newCRVal
                        else:
                            newCRVal[1] = 0
                            gameList[i][j] = newCRVal
        self.printLista(gameList)
        #Rescata valores de celdas perdidas y comprueba que no hayan repeticiones
        repeatsOnScan = False
        for row, col in product(range(0,size), repeat=2):
            if not gameList[row][col] and col < (size-1) and len(gameList[row][col + 1]) == 1:
                gameList[row][col] = [0, 0]
                pos = col + 1
                finishList = False
                suma = 0
                listTaked = []
                while pos < size and not finishList:
                    if not gameList[row][pos] or len(gameList[row][pos]) == 2:
                        finishList = True
                    else:
                        suma += gameList[row][pos][0]
                        listTaked.append(gameList[row][pos][0])
                    pos += 1
                gameList[row][col][1] = suma
                print("col:", suma)
                print(listTaked)
                repeatsOnScan = self.repeatsOnArray2(listTaked)
                if repeatsOnScan:  # Si encuentra repeticiones repite el proceso desde el inicio
                    print("Repeticiones hayadas, generando de nuevo")
                    return self.getNewGame()
                if row < (size-1) and len(gameList[row + 1][col]) == 1:
                    pos = row + 1
                    finishList = False
                    suma = 0
                    listTaked = []
                    while pos < size and not finishList:
                        if not gameList[pos][col] or len(gameList[pos][col]) == 2:
                            finishList = True
                        else:
                            suma += gameList[pos][col][0]
                            listTaked.append(gameList[pos][col][0])
                        pos += 1
                    gameList[row][col][0] = suma
                    print("Row: ",suma)
                    print(listTaked)
                    repeatsOnScan = self.repeatsOnArray2(listTaked)
                    if repeatsOnScan:  # Si encuentra repeticiones repite el proceso desde el inicio
                        print("Repeticiones hayadas, generando de nuevo")
                        return self.getNewGame()
            elif not gameList[row][col] and row < (size - 1) and len(gameList[row + 1][col]) == 1:
                gameList[row][col] = [0, 0]
                pos = row + 1
                finishList = False
                suma = 0
                listTaked = []
                while pos < size and not finishList:
                    if not gameList[pos][col] or len(gameList[pos][col]) == 2:
                        finishList = True
                    else:
                        suma += gameList[pos][col][0]
                        listTaked.append(gameList[pos][col][0])
                    pos += 1
                gameList[row][col][0] = suma
                print("Row: ", suma)
                print(listTaked)
                repeatsOnScan = self.repeatsOnArray2(listTaked)
                if repeatsOnScan:  # Si encuentra repeticiones repite el proceso desde el inicio
                    print("Repeticiones hayadas, generando de nuevo")
                    return self.getNewGame()
                if col < (size-1) and len(gameList[row][col + 1]) == 1:
                    pos = col + 1
                    finishList = False
                    suma = 0
                    listTaked = []
                    while pos < size and not finishList:
                        if not gameList[row][pos] or len(gameList[row][pos]) == 2:
                            finishList = True
                        else:
                            suma += gameList[row][pos][0]
                            listTaked.append(gameList[row][pos][0])
                        pos += 1
                    gameList[row][col][1] = suma
                    print("col:",suma)
                    print(listTaked)
                    repeatsOnScan = self.repeatsOnArray2(listTaked)
                    if repeatsOnScan: #Si encuentra repeticiones repite el proceso desde el inicio
                        print("Repeticiones hayadas, generando de nuevo")
                        return self.getNewGame()
            elif len(gameList[row][col]) == 2:
                if gameList[row][col][0] == 0 and row < (size-1) and len(gameList[row + 1][col]) == 1:
                    pos = row + 1
                    finishList = False
                    suma = 0
                    listTaked = []
                    while pos < size and not finishList:
                        if not gameList[pos][col] or len(gameList[pos][col]) == 2:
                            finishList = True
                        else:
                            suma += gameList[pos][col][0]
                            listTaked.append(gameList[pos][col][0])
                        pos += 1
                    gameList[row][col][0] = suma
                    print("Row: ", suma)
                    print(listTaked)
                    repeatsOnScan = self.repeatsOnArray2(listTaked)
                    if repeatsOnScan:  # Si encuentra repeticiones repite el proceso desde el inicio
                        print("Repeticiones hayadas, generando de nuevo")
                        return self.getNewGame()
                if gameList[row][col][1] == 0 and (col < (size-1)) and len(gameList[row][col + 1]) == 1:
                    pos = col + 1
                    finishList = False
                    suma = 0
                    listTaked = []
                    while pos < size and not finishList:
                        if not gameList[row][pos] or len(gameList[row][pos]) == 2:
                            finishList = True
                        else:
                            suma += gameList[row][pos][0]
                            listTaked.append(gameList[row][pos][0])
                        pos += 1
                    gameList[row][col][1] = suma
                    print("col:", suma)
                    print(listTaked)
                    repeatsOnScan = self.repeatsOnArray2(listTaked)
                    if repeatsOnScan:  # Si encuentra repeticiones repite el proceso desde el inicio
                        print("Repeticiones hayadas, generando de nuevo")
                        return self.getNewGame()


        return gameList

    def printLista(self,lista):
        for i in range(0, len(lista)):
            print(lista[i])
        print("\n")
# lista = kakuroMaker(12).getNewGame()
# for i in range(0, len(lista)):
#     print(lista[i])
