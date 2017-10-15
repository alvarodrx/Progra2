# # import random
# # import pprint
# # import numpy as np
# #
# #
# #
# # class kakuroMaker:
# #     game = False
# #     gameSize = 0
# #     def __init__(self,size):
# #         self.game = True
# #         self.gameSize = size
# #
# #     def getSumForNumer(self, number):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
# #         numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #         #numberList += np.arange(1, 10).tolist()  # Creo lista del 1 al 9
# #         suma = 0
# #         for i in range(0, number):
# #             indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
# #             numObt = numberList[indice]  # obtiene el numero de la lista
# #             suma += numObt
# #             # print(numObt)
# #             numberList.remove(numObt)  #
# #         # pprint.pprint(numberList)
# #         return suma
# #
# #     def getArrayForNumer(self, number):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
# #         numberList = [1,2,3,4,5,6,7,8,9]
# #         suma = []
# #         for i in range(0, number):
# #             indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
# #             numObt = numberList[indice]  # obtiene el numero de la lista
# #             suma.append(numObt)
# #             # print(numObt)
# #             numberList.remove(numObt)  #
# #         #pprint.pprint(numberList)
# #         return suma
# #
# #     def getArrayForArray(self, array):  # Obtiene un numero random probeniente de la suma de la cantidad de posiciones dada
# #         numberList = [1,2,3,4,5,6,7,8,9]
# #         listReturn = []
# #         for i in array:
# #             print("i: ",i)
# #             if (type(i) is list) and len(i) == 1:
# #                 numberList.remove(i[0])
# #                 print("numberlist: ",numberList)
# #         for i in array:
# #             if (type(i) is list) and len(i) == 1:
# #                 listReturn.append(i)
# #
# #             else:
# #                 indice = 0
# #                 if len(numberList) > 1:
# #                     indice = random.randrange(0, len(numberList))  # Obtiene un indice de la lista
# #                 else:
# #                     indice = 0
# #                 numObt = numberList[indice]  # obtiene el numero de la lista
# #                 listReturn.append([numObt])
# #                 numberList.remove(numObt)  #
# #         return listReturn
# #
# #     def repeatsOnArray(self, array): #Busca repeticiones en una lista
# #         compArray = [] #lista de comparacion
# #         for i in array:
# #             if (type(i) is list) and len(i) == 1:
# #                 if compArray.count(i[0]) > 0:
# #                     return True
# #                 compArray.append(i[0])
# #         return False
# #
# #
# #
# #
# #     def getNewGame(self):
# #         size = self.gameSize
# #         gameList = []
# #         for i in range(0, size):
# #             raw = []
# #             for j in range(0, size):
# #                 if random.randrange(0, 2) == 0:
# #                     raw.append(0)
# #                 else:
# #                     if j == (size - 1):
# #                         if i == (size - 1):
# #                             raw.append(0)  # En la esquina de abajo siempre va un 0
# #                         else:
# #                             typeCell = random.randrange(0, 2) * 2  # 0 o 2
# #                             raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
# #                     elif i == (size - 1):
# #                         typeCell = random.randrange(0, 2)  # 0 o 1
# #                         raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
# #                     else:
# #                         typeCell = random.randrange(0, 4)  # 0 o 1
# #                         raw.append(typeCell)  # 0 es negro, 1 es de fila , 2 es de columna, 3 es de fila y columna
# #             gameList.append(raw)
# #             raw = []
# #
# #         for i in range(0, size):
# #             for j in range(0, size):
# #                 if gameList[i][j] == 0:
# #                     gameList[i][j] = []
# #
# #                 elif gameList[i][j] == 1: #construye columnas
# #                     if i == 0:
# #                         if (size - j) > 10:
# #                             numberOfCells = random.randrange(1, 10)
# #                             newRowArray = self.getArrayForNumer(numberOfCells) #Lista de numeros
# #                             newRowVal = np.sum(newRowArray) #Suma de esos numeros
# #                             gameList[i][j] = [0, newRowVal] #Coloca el valor de los numeros
# #                             indice = 0
# #                             j += 1
# #                             actual = j
# #                             while j < (actual + numberOfCells):
# #                                 gameList[i][j] = [newRowArray[indice]] #Coloca el valor del indice
# #                                 indice += 1
# #                                 j += 1
# #                             gameList[i][j] = [] #Final de la lista
# #                         elif (size - j) >= 2:
# #                             numberOfCells = random.randrange(1, size - j)
# #                             newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                             newRowVal = np.sum(newRowArray)  # Suma de esos numeros
# #                             gameList[i][j] = [0, newRowVal]  # Coloca el valor de la suma de los numeros
# #                             indice = 0
# #                             j += 1
# #                             actual = j
# #                             while j < (actual + numberOfCells):
# #                                 gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
# #                                 indice += 1
# #                                 j += 1
# #                             if j < size:
# #                                 gameList[i][j] = []
# #                         else:
# #                             for k in range(j, size):
# #                                 gameList[i][k] = []
# #                             j = size
# #                     else:  # Evita adyacencia con columnas
# #                         if (size - j) > 10:
# #                             thisRow = gameList[i] #fila actual
# #                             notRepeatFlag = False  # Indica que no hay repeticiones de numeros en la lista
# #                             trys = 0
# #                             valuesList = []
# #                             posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                             while notRepeatFlag:
# #                                 position = j + 1  # pociacion de la siguiente celda
# #                                 posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                                 valuesList = []
# #                                 while (trys < 10) and (position < (j+10-trys)) and (thisRow[position] != []):
# #                                     valuesList.append(thisRow[position])
# #                                     position += 1
# #                                     posibLenght += 1
# #                                 notRepeatFlag = self.repeatsOnArray(valuesList)
# #                                 trys += 1
# #                                 if (thisRow[j+posibLenght+1] < size) and (type(thisRow[j+posibLenght+1]) is list):
# #                                     notRepeatFlag = True
# #                             if posibLenght != 0:
# #                                 newRowArray = self.getArrayForArray(valuesList)
# #                                 print("Array: ",newRowArray)
# #                                 newRowVal = np.sum(newRowArray)
# #                                 gameList[i][j] = [0, newRowVal]
# #                                 j += 1
# #                                 actual = j
# #                                 while j < (actual + numberOfCells):
# #                                     gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
# #                                     indice += 1
# #                                     j += 1
# #                                 if j < size:
# #                                     gameList[i][j] = []
# #                             else:
# #                                 gameList[i][j] = []
# #
# #                         elif (size - j) >= 2:
# #                             print("Entra")
# #                             thisRow = gameList[i]  # fila actual
# #                             notRepeatFlag = True  # Indica que no hay repeticiones de numeros en la lista
# #                             trys = 0
# #                             valuesList = []
# #                             posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                             while notRepeatFlag:
# #                                 print("Entra al for")
# #                                 position = j + 1  # pociacion de la siguiente celda
# #                                 posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                                 valuesList = []
# #                                 while (trys < (size - j)) and (position < (size - trys)) and (thisRow[position] != []):
# #                                     valuesList.append(thisRow[position])
# #                                     position += 1
# #                                     posibLenght += 1
# #                                 notRepeatFlag = self.repeatsOnArray(valuesList)
# #                                 trys += 1
# #                                 if ((j + posibLenght + 1) < size) and (type(thisRow[j + posibLenght + 1]) is list):
# #                                     notRepeatFlag = True
# #                                 if trys > 10 or len(valuesList) == 0:
# #                                     notRepeatFlag = False
# #                                     posibLenght = 0
# #                             if posibLenght != 0:
# #                                 print("- List: ", valuesList)
# #                                 newRowArray = self.getArrayForArray(valuesList)
# #                                 newRowVal = np.sum(newRowArray)
# #                                 print("- Array: ", newRowArray)
# #                                 gameList[i][j] = [0, newRowVal]
# #                                 indice = 0
# #                                 j += 1
# #                                 actual = j
# #                                 while j < (actual + posibLenght):
# #                                     gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
# #                                     indice += 1
# #                                     j += 1
# #                                 if j < size:
# #                                     gameList[i][j] = []
# #                             else:
# #                                 gameList[i][j] = []
# #
# #                         else:
# #                             for k in range(j, size):
# #                                 if type(gameList[i][k]) is not list:
# #                                     gameList[i][k] = []
# #                             j = len(gameList)
# #
# #                 elif gameList[i][j] == 2: #Construye columnas
# #                     if (size - i) > 10:
# #                         numberOfCells = random.randrange(1, 10)
# #                         newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                         newColVal = np.sum(newColArray) # Suma de la lista
# #                         gameList[i][j] = [newColVal, 0]
# #                         indice = 0
# #                         for k in range(i + 1, i + numberOfCells + 1):
# #                             gameList[k][j] = [newColArray[indice]]
# #                             indice += 1
# #                         gameList[i + numberOfCells + 1][j] = []
# #                     elif (size - i) >= 2:
# #                         numberOfCells = random.randrange(1, size - i)
# #                         newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                         newColVal = np.sum(newColArray)  # Suma de la lista
# #                         gameList[i][j] = [newColVal, 0]
# #                         indice = 0
# #                         for k in range(i + 1, i + numberOfCells + 1):
# #                             gameList[k][j] = [newColArray[indice]]
# #                             indice += 1
# #                         if (i+numberOfCells+1) < size:
# #                             gameList[i+numberOfCells+1][j] = []
# #                     else:
# #                         for k in range(i, size):
# #                             gameList[k][j] = []
# #
# #                 elif gameList[i][j] == 3: #Filas y columnas
# #                     newCRVal = [0, 0]
# #                     # inicio por la columna por que no requiere desplazamiento
# #                     if (size - i) > 10:
# #                         numberOfCells = random.randrange(1, 10)
# #                         newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                         newColVal = np.sum(newColArray) # Suma de la lista
# #                         newCRVal[0] = newColVal
# #                         indice = 0
# #                         for k in range(i + 1, i + numberOfCells + 1):
# #                             gameList[k][j] = [newColArray[indice]]
# #                             indice += 1
# #                         gameList[i + numberOfCells + 1][j] = []
# #                     elif (len(gameList) - i) >= 2:
# #                         numberOfCells = random.randrange(1, size - i)
# #                         newColArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                         newColVal = np.sum(newColArray)  # Suma de la lista
# #                         newCRVal[0] = newColVal
# #                         indice = 0
# #                         for k in range(i + 1, i + numberOfCells + 1):
# #                             gameList[k][j] = [newColArray[indice]]
# #                             indice += 1
# #                         if (i+numberOfCells+1) < size:
# #                             gameList[i+numberOfCells+1][j] = []
# #                     else:
# #                         for k in range(i, size):
# #                             gameList[k][j] = []
# #
# #                     # Ahora hago la fila..
# #
# #                     if i == 0:
# #                         if (size - j) > 10:
# #                             numberOfCells = random.randrange(1, 10)
# #                             newRowArray = self.getArrayForNumer(numberOfCells) #Lista de numeros
# #                             newRowVal = np.sum(newRowArray) #Suma de esos numeros
# #                             newCRVal[1] = newRowVal
# #                             gameList[i][j] = newCRVal #Coloca el valor de los numeros
# #                             indice = 0
# #                             j += 1
# #                             actual = j
# #                             while j < (actual + numberOfCells):
# #                                 gameList[i][j] = [newRowArray[indice]] #Coloca el valor del indice
# #                                 indice += 1
# #                                 j += 1
# #                             gameList[i][j] = [] #Final de la lista
# #                         elif (size - j) >= 2:
# #                             numberOfCells = random.randrange(1, size - j)
# #                             newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                             newRowVal = np.sum(newRowArray)  # Suma de esos numeros
# #                             newCRVal[1] = newRowVal
# #                             gameList[i][j] = newCRVal  # Coloca el valor de la suma de los numeros
# #                             indice = 0
# #                             j += 1
# #                             actual = j
# #                             while j < (actual + numberOfCells):
# #                                 gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
# #                                 indice += 1
# #                                 j += 1
# #                             if j < size:
# #                                 gameList[i][j] = []
# #                         else:
# #                             for k in range(j, size):
# #                                 gameList[i][k] = []
# #                             j = size
# #                     else:  # Evita adyacencia con columnas
# #                         if (size - j) > 10:
# #                             thisRow = gameList[i] #fila actual
# #                             notRepeatFlag = False  # Indica que no hay repeticiones de numeros en la lista
# #                             trys = 0
# #                             valuesList = []
# #                             posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                             while notRepeatFlag:
# #                                 position = j + 1  # pociacion de la siguiente celda
# #                                 posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                                 valuesList = []
# #                                 while (trys < 10) and (position < (j+10-trys)) and (thisRow[position] != []):
# #                                     valuesList.append(thisRow[position])
# #                                     position += 1
# #                                     posibLenght += 1
# #                                 notRepeatFlag = self.repeatsOnArray(valuesList)
# #                                 trys += 1
# #                                 if (thisRow[j+posibLenght+1] < size) and (type(thisRow[j+posibLenght+1]) is list):
# #                                     notRepeatFlag = True
# #                             if posibLenght != 0:
# #                                 newRowArray = self.getArrayForArray(valuesList)
# #                                 print("Array: ",newRowArray)
# #                                 newRowVal = np.sum(newRowArray)
# #                                 newCRVal[1] = newRowVal
# #                                 gameList[i][j] = newCRVal
# #                                 j += 1
# #                                 actual = j
# #                                 while j < (actual + numberOfCells):
# #                                     gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
# #                                     indice += 1
# #                                     j += 1
# #                                 if j < size:
# #                                     gameList[i][j] = []
# #                             else:
# #                                 gameList[i][j] = []
# #
# #                         elif (size - j) >= 2:
# #                             print("Entra")
# #                             thisRow = gameList[i]  # fila actual
# #                             notRepeatFlag = True  # Indica que no hay repeticiones de numeros en la lista
# #                             trys = 0
# #                             valuesList = []
# #                             posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                             while notRepeatFlag:
# #                                 print("Entra al for")
# #                                 position = j + 1  # pociacion de la siguiente celda
# #                                 posibLenght = 0  # tamaño maximo antes de tocar con adyacencia o con repeticiones
# #                                 valuesList = []
# #                                 while (trys < (size - j)) and (position < (size - trys)) and (thisRow[position] != []):
# #                                     valuesList.append(thisRow[position])
# #                                     position += 1
# #                                     posibLenght += 1
# #                                 notRepeatFlag = self.repeatsOnArray(valuesList)
# #                                 trys += 1
# #                                 if ((j + posibLenght + 1) < size) and (type(thisRow[j + posibLenght + 1]) is list):
# #                                     notRepeatFlag = True
# #                                 if trys > 10 or len(valuesList) == 0:
# #                                     notRepeatFlag = False
# #                                     posibLenght = 0
# #                             if posibLenght != 0:
# #                                 print("- List: ", valuesList)
# #                                 newRowArray = self.getArrayForArray(valuesList)
# #                                 newRowVal = np.sum(newRowArray)
# #                                 print("- Array: ", newRowArray)
# #                                 newCRVal[1] = newRowVal
# #                                 gameList[i][j] = newCRVal
# #                                 indice = 0
# #                                 j += 1
# #                                 actual = j
# #                                 while j < (actual + posibLenght):
# #                                     gameList[i][j] = newRowArray[indice]  # Coloca el valor del indice
# #                                     indice += 1
# #                                     j += 1
# #                                 if j < size:
# #                                     gameList[i][j] = []
# #                             else:
# #                                 gameList[i][j] = []
# #
# #                         else:
# #                             for k in range(j, size):
# #                                 if type(gameList[i][k]) is not list:
# #                                     gameList[i][k] = []
# #                             j = len(gameList)
# #
# #
# #         return gameList
# #
# #
# # lista = kakuroMaker(12).getNewGame()
# # for i in range(0, len(lista)):
# #     print(lista[i])
# '''
# import multiprocessing
# import time
#
# class Test:
#     muestra = 0
#     def __init__(self):
#         self.pool = multiprocessing.Pool(1)
#         m = multiprocessing.Manager()
#         self.queue = m.Queue()
#
#     def subprocess(self):
#         for i in range(10):
#             print("Running",self.muestra)
#             self.muestra += 1
#             time.sleep(1)
#         print("Subprocess Completed")
#
#     def subprocess2(self):
#         for i in range(10):
#             print("Running2",self.muestra)
#             self.muestra += 1
#             time.sleep(1)
#         print("Subprocess Completed")
#
#     def start(self):
#         self.pool.apply_async(func=self.subprocess)
#         self.pool.apply_async(func=self.subprocess2)
#         self.pool.apply_async(func=self.subprocess2)
#         print("Subprocess has been started")
#         self.pool.close()
#         self.pool.join()
#
#     def __getstate__(self):
#         self_dict = self.__dict__.copy()
#         del self_dict['pool']
#         return self_dict
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#
# if __name__ == '__main__':
#     test = Test()
#     test.start()
#
# ##################################################################################
#
# import kakuroMaker
# from itertools import *
# from copy import copy
#
# def uCellSolver(game): #Resuelve todos los valores de una celda
#     size = len(game)
#     for row, col in product(range(size), repeat=2):
#         if game[row][col] and len(game[row][col]) == 2:
#             rowVal = game[row][col][0]
#             colVal = game[row][col][1]
#             #Columnas
#             if (rowVal > 0) and (rowVal < 10):
#                 cellQ = 0
#                 nonBlank = True
#                 pos = row + 1
#                 while nonBlank and pos < size:
#                     if game[pos][col] == []:
#                         nonBlank = False
#                     elif len(game[pos][col]) == 1:
#                         cellQ += 1
#                     else:
#                         nonBlank = False
#                     pos += 1
#                 if cellQ == 1:
#                     game[row + 1][col][0] = rowVal
#             #Filas
#             if (colVal > 0) and (colVal < 10):
#                 cellQ = 0
#                 nonBlank = True
#                 pos = col + 1
#                 while nonBlank and pos < size:
#                     if game[row][pos] == []:
#                         nonBlank = False
#                     elif len(game[row][pos]) == 1:
#                         cellQ += 1
#                     else:
#                         nonBlank = False
#                     pos += 1
#                 if cellQ == 1:
#                     game[row ][col + 1][0] = colVal
#
# def printLista(lista):
#     for i in range(0, len(lista)):
#         print(lista[i])
#     print("\n")
#
# lista = kakuroMaker.kakuroMaker(20).getNewGame()
# printLista(lista)
#
# for row, col in product(range(len(lista)), repeat=2):
#     actual = lista[row][col]
#     if len(actual) == 1:
#         lista[row][col] = [0]
#
# printLista(lista)
#
# uCellSolver(lista)
#
# printLista(lista)
# '''
#
#
#
#
# #
# # for i in range(0, size):
# #     for j in range(0, size):
# #         if gameList[i][j] == 0:
# #             gameList[i][j] = []
# #         elif gameList[i][j] == 1:  # construye filas
# #             if i < 2:
# #                 if (size - j) > 10:
# #                     numberOfCells = random.randrange(3, 10)
# #                     newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                     newRowVal = np.sum(newRowArray)  # Suma de esos numeros
# #                     gameList[i][j] = [0, newRowVal]  # Coloca el valor de los numeros
# #                     indice = 0
# #                     j += 1
# #                     actual = j
# #                     while j < (actual + numberOfCells):
# #                         gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
# #                         indice += 1
# #                         j += 1
# #                     gameList[i][j] = []  # Final de la lista
# #                 elif (size - j) > 2:
# #                     numberOfCells = random.randrange(2, size - j)
# #                     newRowArray = self.getArrayForNumer(numberOfCells)  # Lista de numeros
# #                     newRowVal = np.sum(newRowArray)  # Suma de esos numeros
# #                     gameList[i][j] = [0,
# #                                       newRowVal]  # Coloca el valor de la suma de los numeros
# #                     indice = 0
# #                     j += 1
# #                     actual = j
# #                     while j < (actual + numberOfCells):
# #                         gameList[i][j] = [newRowArray[indice]]  # Coloca el valor del indice
# #                         indice += 1
# #                         j += 1
# #                     if j < size:
# #                         gameList[i][j] = []
# #                 else:
# #                     for k in range(j, size):
# #                         gameList[i][k] = []
# #                     j = size
# #
# # import matplotlib.pyplot as plt
# # from functools import partial
# # import multiprocessing
# #
# #
# # def mandelbrotCalcRow(yPos, h, w, max_iteration=1000):
# #     y0 = yPos * (2 / float(h)) - 1  # rescale to -1 to 1
# #     row = []
# #     for xPos in range(w):
# #         x0 = xPos * (3.5 / float(w)) - 2.5  # rescale to -2.5 to 1
# #         iteration, z = 0, 0 + 0j
# #         c = complex(x0, y0)
# #         while abs(z) < 2 and iteration < max_iteration:
# #             z = z ** 2 + c
# #             iteration += 1
# #         row.append(iteration)
# #     return row
# #
# #
# # def mandelbrotCalcSet(h, w, max_iteration=1000):
# #     # make a helper function that better supports pool.map by using only 1 var
# #     # This is necessary since the version
# #     partialCalcRow = partial(mandelbrotCalcRow, h=h, w=w, max_iteration=max_iteration)
# #
# #     pool = multiprocessing.Pool()  # creates a pool of process, controls worksers
# #     # the pool.map only accepts one iterable, so use the partial function
# #     # so that we only need to deal with one variable.
# #     mandelImg = pool.map(partialCalcRow, range(h))  # make our results with a map call
# #     pool.close()  # we are not adding any more processes
# #     pool.join()  # tell it to wait until all threads are done before going on
# #
# #     return mandelImg
# #
# # ''' Algoritmo normal
# # def mandelbrotCalcSet(h, w, max_iteration = 1000):
# #     partialCalcRow = partial(mandelbrotCalcRow, h=h, w=w, max_iteration = max_iteration)
# #     mandelImg = map(partialCalcRow, xrange(h))
# #     return mandelImg'''
# #
# #
# # if __name__=='__main__':
# #     mandelImg = mandelbrotCalcSet(1000, 1000, 500)
# #     plt.imshow(mandelImg)
# #     plt.savefig('mandelimg0.png')
#
# #!/usr/bin/env python
# """This library provides functionality to represent and solve Kakuro boards.
#
# A board is represented by a two dimensional array of KakuroEntry objects,
# either Brick or Blank:
#
# * Brick(v=None, h=None):
# A greyed out brick, possibly specifying a vertical (v) and / or horizontal
# (h) sum.
#
# * Blank(value=None):
# An entry to be filled in, possibly with a value already specified.
#
# The two dimensional array is passed to the constructor of a KakuroBoard:
#
# * KakuroBoard(array)
# Uses the two dimensional array to represent internal data structures
# necessary to solve the Kakuro board. Provides the solve() method to solve a
# board, which functions as a generator in the case of no or multiple solutions.
#
# The board is solved using an iterative refinement process by eliminating
# possible values from entries and candidate values for semirows or semicolumns
# used in sums. When pure refinement yields no more improvement, the algorithm
# uses backtracking, branching on an entry of fewest possible values.
#
# Here is an example of the use of this class to solve a Kokuro board:
#
# board = [[Brick(), Brick(v=14), Brick(v=5), Brick(v=28), Brick(v=3), Brick(), Brick(), Brick(v=26), Brick(v=5), Brick(v=22)],
#          [Brick(h=12), Blank(), Blank(), Blank(), Blank(), Brick(v=12,h=24), Blank(), Blank(), Blank(), Blank()],
#          [Brick(h=23), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(v=32,h=21), Blank(), Blank(), Blank()],
#          [Brick(), Brick(v=7), Brick(v=39), Blank(), Brick(h=6), Blank(), Blank(), Blank(), Brick(v=24), Blank()],
#          [Brick(h=20), Blank(), Blank(), Blank(), Brick(v=19,h=27), Blank(), Blank(), Blank(), Blank(), Brick(v=34)],
#          [Brick(h=6), Blank(), Blank(), Brick(v=22,h=23), Blank(), Blank(), Blank(), Brick(v=13,h=15), Blank(), Blank()],
#          [Brick(h=14), Blank(), Blank(), Blank(), Blank(), Brick(h=14), Blank(), Blank(), Blank(), Blank()],
#          [Brick(), Brick(v=6,h=22), Blank(), Blank(), Blank(), Brick(v=4,h=16), Blank(), Blank(), Brick(v=17), Blank()],
#          [Brick(h=21), Blank(), Blank(), Blank(), Brick(h=24), Blank(), Blank(), Blank(), Blank(), Blank()],
#          [Brick(h=15), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(h=20), Blank(), Blank(), Blank()]]
#
# k = KakuroBoard(board)
#
# for entries in k.solve():
#     print '*** SOLUTION ***'
#     str = ''
#     for row in board:
#         for col in row:
#             if isinstance(col, Brick):
#                 str += '_ '
#             else:
#                 str += '%s ' % entries[col.myID].possibleValues[0]
#         str += '\n'
#     print str
# """
#
# import operator
# from functools import reduce
#
#
# def _findAssignments(val, blankList, exclude=[]):
#     """_findAssignments(val, blankList, exclude=[])
#
#     Given a value and a list of blanks, find all possible assignments of values
#     to entries that satisfies this value. Exclude can be used to exclude certain
#     possible values. In this case, it is used recursively to make sure that each
#     possible number appears at most once in each sum."""
#
#     # If we have a full sum, yield it.
#     if val == 0 and len(blankList) == 0:
#         yield []
#
#     # If we are out of blanks to fill and val was not achieved, we failed.
#     if len(blankList) == 0:
#         return
#
#     # If we have no possible value left for any remaining position, we failed.
#     if not reduce(lambda x, y: x and y,
#                   [filter(lambda x: x not in exclude, blank.possibleValues) for blank in blankList],
#                   True):
#         return
#
#     # If we cannot even use the biggest guys to complete, stop.
#     if sum([max([i for i in blank.possibleValues if i not in exclude]) for blank in blankList]) < val:
#         return
#
#     # If we cannot even use the smallest guys to complete, stop.
#     if sum([min([i for i in blank.possibleValues if i not in exclude]) for blank in blankList]) > val:
#         return
#
#     # Otherwise, try to fill in the next position and reiterate.
#     for candidate in [i for i in blankList[0].possibleValues if i not in exclude]:
#         for s in _findAssignments(val - candidate, blankList[1:], exclude + [candidate]):
#             yield [candidate] + s
#
#
# class Sum:
#     """Represents a sum in the board, i.e. the value of the sum and the iist of
#     Blank objects contributing to that sum."""
#
#     def __init__(self, value, blankList, isCopy=False):
#         self.value = value
#         self.blankList = blankList
#
#         # If this is not a copying operation, we calculate all possible
#         # assignments.
#         if not (isCopy):
#             self.configurations = list(_findAssignments(self.value, self.blankList))
#
#         # Record each entry as appearing in this sum.
#         for blank in blankList:
#             blank._recordSum(self)
#
#         # Flag indicating that the sum is not yet fully determined.
#         self.flag = False
#
#     def isComplete(self):
#         """Return True if this sum is completely defined and has been processed.
#         and False otherwise."""
#         return self.flag
#
#     def _copy(self, entries):
#         """Make a copy of this sum, using the entries in entries instead of the
#         original entries. (The entries in entries should be copies.)"""
#
#         # Make a copy, using the isCopy flag to avoid recalculating all possible
#         # configurations.
#         s = Sum(self.value, [entries[i.myID] for i in self.blankList], isCopy=True)
#
#         # Now copy over the configurations. We do not need to do a deep copy
#         # since the configurations themselves do not change, only the list of
#         # them changes.
#         s.configurations = self.configurations[:]
#
#         return s
#
#     def _filterBasedOnEntry(self, entry):
#         """For a given entry, filter out all configurations that are not valid
#         based on the possible values for the entry."""
#
#         # If this sum is complete, we ignore this operation.
#         if self.flag:
#             return False
#
#         # Get the index in configurations for entry.
#         idx = self.blankList.index(entry)
#
#         # Filter, allowing only possible entries for entry.
#         newConfigurations = [config for config in self.configurations if config[idx] in entry.possibleValues]
#         changed = (newConfigurations != self.configurations)
#         self.configurations = newConfigurations
#
#         # Report if anything changed.
#         return changed
#
#     def _banExistingConfiguration(self, config):
#         """We only allow each sum to appear once in the table, e.g. if we have
#         twos sum of value 10 over three entries and one of them is 1, 3, 6, then
#         the other one cannot be any permutation of 1, 3, 6.
#
#         This method accepts a configuration (a list of values) that has already
#         been used, and filters all permutations of it out of the configuration
#         for this row."""
#
#         # If this sum is complete, we ignore this operation.
#         if self.flag:
#             return False
#
#         newConfigurations = [c for c in self.configurations if set(c) != set(config)]
#         changed = (newConfigurations != self.configurations)
#         self.configurations = newConfigurations
#
#         # Report if anything changed.
#         return changed
#
#     def _getValuesForEntry(self, entry):
#         """Given an entry appearing in the sum, determine all the possible
#         values it can have in the sum."""
#
#         # Get the index in the configurations for the entry.
#         idx = self.blankList.index(entry)
#
#         # Find all possible values for entry over the configurations.
#         return [config[idx] for config in self.configurations]
#
#     def _checkCompleteAndProcess(self):
#         """Check if this sum is defined, i.e. if only one configuration remains.
#         If this is the case, mark it as such and set all of the entries to their
#         value in the configuration."""
#
#         if self.flag:
#             return False
#
#         changed = False
#         if len(self.configurations) == 1:
#             # We only do this once, and then ignore the sum as it has been fully
#             # processed, so mark the flag as true to indicate this.
#             self.flag = True
#
#             # Now for every entry in this sum, set it to its value.
#             for entry, value in zip(self.blankList, self.configurations[0]):
#                 changed |= entry._setValue(value)
#
#         # Report if anything changed.
#         return changed
#
#
# class KakuroEntry:
#     """The superclass for entries in a Kakuro board."""
#     pass
#
#
# class Blank(KakuroEntry):
#     """A blank square to be filled in."""
#     id = 0
#
#     def __init__(self, value=None, specificID=None):
#         self.possibleValues = [value] if value else range(1, 10)
#
#         # Give every blank an index for easy identification and to determine
#         # if one blank is a copy of another.
#         if specificID == None:
#             self.myID = Blank.id
#             Blank.id += 1
#         else:
#             self.myID = specificID
#
#         # Keep track of the sums containing this blank.
#         self.sums = []
#
#     def _copy(self):
#         """Create a copy of this entry.
#
#         NOTE: We do not populate sums, as this will be done when the sums are
#         duplicated."""
#
#         # We want the same ID for comparison purposes.
#         blank = Blank(specificID=self.myID)
#
#         # Make a copy of the possible values so that we can change the possible
#         # values of the copy without affecting the original.
#         blank.possibleValues = self.possibleValues[:]
#
#         return blank
#
#     def __str__(self):
#         """Return a string identifying this blank."""
#         return 'E%2s' % self.myID
#
#     def _recordSum(self, s):
#         """Record this entry as appearing in the specified Sum object."""
#         if s not in self.sums:
#             self.sums.append(s)
#
#     def _filterSumConfigurations(self):
#         """Iterate over all the sums containing this blank, and filter out
#         all of the configurations over those sums that contain an invalid
#         entry for this blank."""
#
#         changed = False
#         for s in self.sums:
#             changed |= s._filterBasedOnEntry(self)
#
#         # Report if anything changed.
#         return changed
#
#     def _filterValuesFromSums(self):
#         """This entry can only have certain values in each sum it appears in.
#         The possible values that it can have overall is the intersection of
#         its current possible values with the possible values in each of the
#         sums in which it appears."""
#         newPossibleValues = reduce(lambda x, y: [i for i in x if i in y],
#                                    [set(s._getValuesForEntry(self)) for s in self.sums],
#                                    self.possibleValues)
#         changed = (newPossibleValues != self.possibleValues)
#         self.possibleValues = newPossibleValues
#
#         # Report if anything changed.
#         return changed
#
#     def _setValue(self, value):
#         """Set the value for this entry. This triggers a reaction where we then
#         iterate over the sums containing this entry and modify them
#         accordingly."""
#
#         # This value is now set in stone.
#         self.flag = True
#         self.possibleValues = [value]
#
#         # Filter out all configurations from sums that don't have value for this
#         # entry.
#         return self._filterSumConfigurations()
#
#
# class Brick(KakuroEntry):
#     """A brick, i.e. solid space."""
#
#     def __init__(self, v=None, h=None):
#         self.verticalSum = v
#         self.horizontalSum = h
#
#     def __str__(self):
#         return '_'
#
#
# class KakuroBoard:
#     """A Kakuro board is represented by a two dimensional array with entries of
#     type KakuroEntry representing the data at position x,y."""
#
#     def __init__(self, board):
#         self.board = board
#         self.entries = []
#         print(type(board[0][0]))
#         # Convert to internal data structure, namely a list of sums represented
#         # in the following way:
#         # sum, [Blanks in the sum]
#         sums = []
#         for x, row in enumerate(board):
#             for y, entry in enumerate(row):
#                 # If the entry is a sum, process the sum.
#                 if isinstance(entry, Brick):
#                     brkVal = "Brick: "
#                     if entry.verticalSum:
#                         blocks = []
#                         posx = x + 1
#                         col = [board[i][y] for i in range(len(board))]
#                         while posx < len(col) and isinstance(col[posx], Blank):
#                             blocks.append(col[posx])
#                             posx += 1
#                         sums.append(Sum(entry.verticalSum, blocks))
#                         brkVal += "v=" + str(entry.verticalSum)
#                     if entry.horizontalSum:
#                         blocks = []
#                         posy = y + 1
#                         while posy < len(row) and isinstance(row[posy], Blank):
#                             blocks.append(row[posy])
#                             posy += 1
#                         sums.append(Sum(entry.horizontalSum, blocks))
#                         brkVal += "h=" + str(entry.horizontalSum)
#                     #print(brkVal)
#                 elif isinstance(entry, Blank):
#                     self.entries.append(entry)
#                     #print("Blank")
#
#         # We have the structure.
#         self.sums = sums
#
#     def _copyBoard(self, entries, sums):
#         """Given a board, make a copy of it. This is used in backtracking.
#
#         NOTE: We are not making a full copy of this object so much as we are
#         simply copying the entries and sums lists."""
#
#         # The entries are specifically going to be what changes, so begin by
#         # copying them.
#         cEntries = [entry._copy() for entry in entries]
#
#         # Now copy the sums. Note that doing so automatically will register each
#         # of the entries with the appropriate sums as required.
#         cSums = [s._copy(cEntries) for s in sums]
#
#         return cEntries, cSums
#
#     def solve(self):
#         """Solve the board."""
#
#         # We start by making a copy, since we don't want to change the actual
#         # Blank entries themselves through computation. Thus, they are preserved
#         # and this class represents a fresh, clean sheet of paper with no
#         # writing on it at all times.
#         cEntries, cSums = self._copyBoard(self.entries, self.sums)
#
#         # Now we use the auxiliary method on the data structure copy until all
#         # the entries are solved.
#         return self._solve(cEntries, cSums)
#
#     def _solve(self, entries, sums):
#         """Solve the board on the data structures given.
#
#         Go as far as we can computationally, and then branch on the entry of
#         fewest choices."""
#
#         # print "\n\n*** BOARD BEFORE ***"
#         # for s in sums:
#         #    print 'Sum: v=%s, e=%s' % (s.value, [(e.myID,e.possibleValues) for e in s.blankList])
#
#         # We process the board as far as we can.
#         changed = True
#         while changed:
#             changed = False
#
#             # First we check to see if any sums are now complete.
#             for s in filter(lambda x: not (x.isComplete()), sums):
#                 # Process it.
#                 changed |= s._checkCompleteAndProcess()
#
#                 # Now if it is complete, we make sure that the configuration is
#                 # not repeated anywhere else in the puzzle.
#                 if s.isComplete():
#                     for s2 in filter(lambda s2: s2.value == s.value and len(s2.blankList) == len(s.blankList), sums):
#                         changed |= s2._banExistingConfiguration(s.configurations[0])
#
#             # Now we iterate over entries and process them.
#             for e in entries:
#                 # First filter the values from sums, meaning reduce the
#                 # possible values for this entry based on what is allowed
#                 # through the sums.
#                 changed |= e._filterValuesFromSums()
#
#             # Iterate over the entries again now, and process further.
#             for e in entries:
#                 # Second filter the values from configs, meaning reduce the
#                 # configurations over the sums so that only those accommodating
#                 # the possible values for this entry are considered.
#                 changed |= e._filterSumConfigurations()
#
#         # print "\n\n*** BOARD AFTER ***"
#         # for s in sums:
#         #    print 'Sum: v=%s, e=%s' % (s.value, [(e.myID,e.possibleValues) for e in s.blankList])
#
#         # If any entries are empty, we must backtrack.
#         if reduce(operator.or_, map(lambda x: len(x.possibleValues) == 0, entries), False):
#             return
#
#         # If the board is complete, we are done.
#         if reduce(operator.and_, [len(i.possibleValues) == 1 for i in entries], True):
#             yield entries
#         else:
#             # Things are now stable, so we must branch on a possible value.
#             # Pick the entry with the fewest choices to minimize branching.
#             branchingEntries = sorted([(len(entry.possibleValues), entry.myID)
#                                        for entry in entries if len(entry.possibleValues) > 1])
#             entryID = branchingEntries[0][1]
#
#             # Try all possible values for this entry.
#             for value in entries[entryID].possibleValues:
#                 # Create a copy of the board.
#                 cEntries, cSums = self._copyBoard(entries, sums)
#
#                 # Set the value.
#                 cEntries[entryID]._setValue(value)
#
#                 # Iteratively solve.
#                 for solution in self._solve(cEntries, cSums):
#                     yield solution
#     def getBoard(self):
#         return self.board
#
# def traslate(kakuro):
#     board = []
#     for i in range(len(kakuro)):
#         newRow = []
#         for j in range(len(kakuro[0])):
#             if len(kakuro[i][j]) == 0:
#                 valor = Brick()
#             elif len(kakuro[i][j]) == 1:
#                 valor = Blank()
#             else:
#                 if kakuro[i][j][1] == 0:
#                     valor = Brick(v= kakuro[i][j][0])
#                 elif kakuro[i][j][0] == 0:
#                     valor = Brick(h= kakuro[i][j][1])
#                 else:
#                     valor = Brick(v= kakuro[i][j][0], h= kakuro[i][j][1])
#             newRow.append(valor)
#         board.append(newRow)
#     return board
#
#
#
#
# board1 = [[[],[14,0],[5,0],[28,0],[3,0],[],[],[26,0],[5,0],[22,0]],
#          [[0,12],[0],[0],[0],[0],[12,24],[0],[0],[0],[0]],
#          [[0,23],[0],[0],[0],[0],[0],[32,21],[0],[0],[0]],
#          [[],[7,0],[39,0],[0],[0,6],[0],[0],[0],[24,5],[0]],
#          [[0,20],[0],[0],[0],[19,27],[0],[0],[0],[0],[34,0]],
#          [[0,6],[0],[0],[22,23],[0],[0],[0],[13,15],[0],[0]],
#          [[0,14],[0],[0],[0],[0],[0,14],[0],[0],[0],[0]],
#          [[],[6,22],[0],[0],[0],[4,16],[0],[0],[17,8],[0]],
#          [[0,21],[0],[0],[0],[2,24],[0],[0],[0],[0],[0]],
#          [[0,15],[0],[0],[0],[0],[0],[0,20],[0],[0],[0]]]
#
# board = traslate(board1)
#
# k = KakuroBoard(board)
# print(k)
#
# for entries in k.solve():
#     print('*** SOLUTION ***')
#     # for entry in entries:
#     #    print '%2s: %s' % (entry.myID, entry.possibleValues)
#     str = ''
#     for row in k.getBoard():
#         for col in row:
#             if isinstance(col, Brick):
#                 str += '_ '
#             else:
#                 str += '%s ' % entries[col.myID].possibleValues[0]
#         str += '\n'
#     print(str)
#
# # board = [[Brick(), Brick(v=14), Brick(v=5), Brick(v=28), Brick(v=3), Brick(), Brick(), Brick(v=26), Brick(v=5), Brick(v=22)],
# #          [Brick(h=12), Blank(), Blank(), Blank(), Blank(), Brick(v=12,h=24), Blank(), Blank(), Blank(), Blank()],
# #          [Brick(h=23), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(v=32,h=21), Blank(), Blank(), Blank()],
# #          [Brick(), Brick(v=7), Brick(v=39), Blank(), Brick(h=6), Blank(), Blank(), Blank(), Brick(v=24), Blank()],
# #          [Brick(h=20), Blank(), Blank(), Blank(), Brick(v=19,h=27), Blank(), Blank(), Blank(), Blank(), Brick(v=34)],
# #          [Brick(h=6), Blank(), Blank(), Brick(v=22,h=23), Blank(), Blank(), Blank(), Brick(v=13,h=15), Blank(), Blank()],
# #          [Brick(h=14), Blank(), Blank(), Blank(), Blank(), Brick(h=14), Blank(), Blank(), Blank(), Blank()],
# #          [Brick(), Brick(v=6,h=22), Blank(), Blank(), Blank(), Brick(v=4,h=16), Blank(), Blank(), Brick(v=17), Blank()],
# #          [Brick(h=21), Blank(), Blank(), Blank(), Brick(h=24), Blank(), Blank(), Blank(), Blank(), Blank()],
# #          [Brick(h=15), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(h=20), Blank(), Blank(), Blank()]]
# #
# # k = KakuroBoard(board)
# #
# # for entries in k.solve():
# #     print ('*** SOLUTION ***')
# #     str = ''
# #     for row in board:
# #         for col in row:
# #             if isinstance(col, Brick):
# #                 str += '_ '
# #             else:
# #                 str += '%s ' % entries[col.myID].possibleValues[0]
# #         str += '\n'
# #     print (str)
#*****************************************************************************************************************

#
# def getCellsLen(board, row, col):
#     sizeBoard = len(board)
#     colLen = 0
#     rowLen = 0
#     nextRow = row + 1
#     while len(board[nextRow][col]) == 1 and nextRow < sizeBoard:
#         colLen += 1
#         nextRow += 1
#
#     nextCol = col + 1
#     while len(board[row][nextCol]) == 1 and nextCol < sizeBoard:
#         rowLen += 1
#         nextCol += 1
#
#     return rowLen, colLen
#
# board1 = [[[],[14,0],[5,0],[28,0],[3,0],[],[],[26,0],[5,0],[22,0]],
#          [[0,12],[0],[0],[0],[0],[12,24],[0],[0],[0],[0]],
#          [[0,23],[0],[0],[0],[0],[0],[32,21],[0],[0],[0]],
#          [[],[7,0],[39,0],[0],[0,6],[0],[0],[0],[24,5],[0]],
#          [[0,20],[0],[0],[0],[19,27],[0],[0],[0],[0],[34,0]],
#          [[0,6],[0],[0],[22,23],[0],[0],[0],[13,15],[0],[0]],
#          [[0,14],[0],[0],[0],[0],[0,14],[0],[0],[0],[0]],
#          [[],[6,22],[0],[0],[0],[4,16],[0],[0],[17,8],[0]],
#          [[0,21],[0],[0],[0],[2,24],[0],[0],[0],[0],[0]],
#          [[0,15],[0],[0],[0],[0],[0],[0,20],[0],[0],[0]]]
#
# y, x = getCellsLen(board1, 0, 3)

# print("Vals:",x,y)
# from copy import copy
# def getValuesForLen(listLen, sumTotal, actList):
#     if len(actList) == listLen:
#         if sumTotal == sum(actList):
#             yield actList
#         return
#     valueList = 0
#     if actList:
#         valueList = range(actList[len(actList) - 1]+1, 10)
#     else:
#         valueList = range(1, 10)
#     for i in valueList:
#         copyList = copy(actList)
#         copyList.append(i)
#         if sum(copyList) == sumTotal and len(copyList) == listLen:
#             yield copyList
#         if sum(copyList) >= sumTotal:
#             return
#         yield from getValuesForLen(listLen, sumTotal, copyList)
#
#
# x = getValuesForLen(0, 24, [])
# for i in x:
#     print("asd:",i)


# def getPromissingList(vhList):
#     vList = vhList[0]
#     hList = vhList[1]
#     hSet = set()
#     vSet = set()
#     result = set()
#     for i in vList:
#         for n in i:
#             vSet.add(n)
#     for i in hList:
#         for n in i:
#             hSet.add(n)
#     for i in hSet:
#         if i in vSet:
#              result.add(i)
#
#     return list(result)
#
#
# a = [[[5, 9], [6, 8]], [[1, 2, 3, 6], [1, 2, 4, 5]]]
#
# print(getPromissingList(a))

# from copy import copy
# from itertools import *
#
# class KakuroSolver:
#     def __init__(self, board):
#         self.board = board
#         self.size = len(board)
#
#     def getCellsLen(self, board, row, col):
#         """Obtiene la cantidad de celdas para una
#         suma tanto para columna como para fila"""
#         sizeBoard = len(board)
#         colLen = 0
#         rowLen = 0
#         nextRow = row + 1
#         while nextRow < sizeBoard and len(board[nextRow][col]) == 1:
#             colLen += 1
#             nextRow += 1
#         nextCol = col + 1
#         while nextCol < sizeBoard and len(board[row][nextCol]) == 1:
#             rowLen += 1
#             nextCol += 1
#
#         return colLen, rowLen
#
#     def getValForLen(self, listLen, sumTotal, actList):
#         """Obtiene las permutaciones del conjunto de valores
#         posibles para la suma y cantidad de celdas dadas """
#         if len(actList) == listLen:
#             if sumTotal == sum(actList):
#                 yield actList
#             return
#         valueList = 0
#         if actList:
#             valueList = range(actList[len(actList) - 1] + 1, 10)
#         else:
#             valueList = range(1, 10)
#         for i in valueList:
#             copyList = copy(actList)
#             copyList.append(i)
#             if sum(copyList) == sumTotal and len(copyList) == listLen:
#                 yield copyList
#             if sum(copyList) >= sumTotal:
#                 return
#             # Baktracking aplicado
#             yield from self.getValForLen(listLen, sumTotal, copyList)
#
#     def getValuesForLen(self, listLen, sumTotal, actList):
#         result = self.getValForLen(listLen, sumTotal, actList)
#         newList = []
#         for solution in result:
#             newList.append(solution)
#         return newList
#
#     def setPosibleValues(self, board):
#         for y, row in enumerate(board):
#             for x, col in enumerate(row):
#                 if len(col) == 2:
#                     rowLen, colLen = self.getCellsLen(board, y, x)
#                     sumsForRow = self.getValuesForLen(rowLen, col[0], [])
#                     sumsForCol = self.getValuesForLen(colLen, col[1], [])
#                     # print(col)
#                     # print("rowlen",rowLen)
#                     # print("colLen",colLen)
#                     # print(sumsForRow)
#                     # print(sumsForCol)
#
#                     posy = y+1
#                     for i in range(rowLen):
#                         if type(board[posy][x][0]) != list:
#                             board[posy][x][0] = [sumsForRow,0]
#                         else:
#                             board[posy][x][0][0] = sumsForRow
#                         posy += 1
#                     posx = x + 1
#                     for i in range(colLen):
#                         if type(board[y][posx][0]) != list:
#                             board[y][posx][0] = [0,sumsForCol]
#                         else:
#                             board[y][posx][0][1] = sumsForCol
#                         posx += 1
#         return board
#
#     def getPromissingList(self, vhList):
#         vList = vhList[0]
#         hList = vhList[1]
#         hSet = set()
#         vSet = set()
#         result = set()
#         for i in vList:
#             for n in i:
#                 vSet.add(n)
#         for i in hList:
#             for n in i:
#                 hSet.add(n)
#         for i in hSet:
#             if i in vSet:
#                 result.add(i)
#
#         return list(result)
#
#     def recalculateValues(self, board, row, col, value):
#         board
#
#     def nextBlank(self, row, col):
#         size = self.size
#         for i, j in product(range(size), repeat=2):
#             if ((i == row and j > col) or (i > row)) and (len(self.board[i][j]) == 1):
#                 return i, j
#         return 0, 0
#
#     def solve(self):
#         boardCopy = self.setPosibleValues(self.board)
#         # col =_1
#         # row = 1
#         # for i in range(self.size):
#         #     for j in range(self.size):
#         #         if len(self.board[i][j] == 1):
#         #             col = j
#         #             row = i
#         #             break
#         row, col = self.nextBlank(1,0)
#         print("r:",row)
#         print("c:", col)
#         return self.solver(boardCopy, row, col, 0)
#
#     def solver(self, board, row, col, prom):
#         print(row)
#         print(col)
#         print(board)
#         print("prom:", prom)
#         if prom == 0:
#             promList = self.getPromissingList(board[row][col][0])
#             print(promList)
#             for i in promList:
#                 yield from self.solver(board, row, col, i)
#         else:
#             board[row][col]
#
#
#
#
#
#
# def printLista(lista):
#     for i in range(0, len(lista)):
#         print(lista[i])
#     print("\n")
#
#
# board = [
#     [[],[5,0],[12,0]],
#     [[0,6],[1],[5]],
#     [[0,11],[4],[7]]
# ]
#
# board1 = [[[],[14,0],[5,0],[28,0],[3,0],[],[],[26,0],[5,0],[22,0]],
#          [[0,12],[0],[0],[0],[0],[12,24],[0],[0],[0],[0]],
#          [[0,23],[0],[0],[0],[0],[0],[32,21],[0],[0],[0]],
#          [[],[7,0],[39,0],[0],[0,6],[0],[0],[0],[24,5],[0]],
#          [[0,20],[0],[0],[0],[19,27],[0],[0],[0],[0],[34,0]],
#          [[0,6],[0],[0],[22,23],[0],[0],[0],[13,15],[0],[0]],
#          [[0,14],[0],[0],[0],[0],[0,14],[0],[0],[0],[0]],
#          [[],[6,22],[0],[0],[0],[4,16],[0],[0],[17,8],[0]],
#          [[0,21],[0],[0],[0],[2,24],[0],[0],[0],[0],[0]],
#          [[0,15],[0],[0],[0],[0],[0],[0,20],[0],[0],[0]]]
# x = KakuroSolver(board)
# lista = x.solve()
# print(lista)
#
# # [   [[],    [5, 0],                                     [12, 0]],
# #  [[0, 6], [[[[1, 4], [2, 3]], [[1, 5], [2, 4]]]],   [[[[3, 9], [4, 8], [5, 7]], [[1, 5], [2, 4]]]]],
# #  [[0, 11], [[[[1, 4], [2, 3]], [[2, 9], [3, 8],     [4, 7], [5, 6]]]], [[[[3, 9], [4, 8], [5, 7]], [[2, 9], [3, 8], [4, 7], [5, 6]]]]]]
