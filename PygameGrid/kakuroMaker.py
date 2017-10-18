import random
import pprint
import numpy as np
from itertools import *
import KakuroGenerator
from kakuroStruc import *



class kakuroMaker:
    kakuro = []
    size = 0

    def __init__(self, size):
        self.size = size
        self.kakuro = self.blankBoard()

    def blankBoard(self):
        size = self.size
        gameList = []
        for col in range(size):
            rw = []
            for r in range(size):
                rw.append(0)
            gameList.append(rw)
        gameList[0][0] = 10
        for i in range(0, size):
            gameList[0][i] = 10
            gameList[i][0] = 10
        # i = size//10
        # mitad = size// 2
        # gameList[1][mitad] = 10
        # gameList[size-1][mitad] = 10
        # gameList[mitad][1] = 10
        # gameList[mitad][size-1] = 10
        # gameList[mitad][mitad] = 10
        # while i > 0:
        #     gameList[1][mitad + i] = 10
        #     gameList[1][mitad - i] = 10
        #     gameList[size - i][mitad + i] = 10
        #     gameList[size - i][mitad - i] = 10
        #     gameList[mitad + i][1] = 10
        #     gameList[mitad - i][1] = 10
        #     gameList[mitad + i][size - 1] = 10
        #     gameList[mitad - i][size - 1] = 10
        #     gameList[1 + i][mitad] = 10
        #     gameList[size - 1 - i][mitad] = 10
        #     gameList[mitad][1 + i] = 10
        #     gameList[mitad][size - 1 - i] = 10
        #     gameList[mitad + i][mitad] = 10
        #     gameList[mitad][mitad - i] = 10
        #     gameList[mitad - i][mitad] = 10
        #     gameList[mitad][mitad + i] = 10
        #     i -= 1

        #print(gameList)
        #gameList= [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10,  0,  0, 10, 10,  0,  0, 10, 10], [10, 10,  0,  0, 10, 10,  0,  0, 10, 10], [10,  0,  0, 10, 10,  0,  0,  0, 10, 10], [10,  0,  0, 10,  0,  0, 10,  0,  0, 10], [10,  0,  0, 10,  0,  0, 10,  0,  0, 10], [10, 10,  0,  0,  0, 10, 10,  0,  0, 10], [10, 10,  0,  0, 10, 10,  0,  0, 10, 10], [10, 10,  0,  0, 10, 10,  0,  0, 10, 10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
        return gameList

    def nextAddend(self, added):
        setLen = len(added)
        nextN = random.randrange(1, 10)
        return nextN

    def isDuplicated(self, row, col, num):
        kakuro = self.kakuro
        duplicates = set()
        duplicates.add(num)
        i = row
        while i > 0 and kakuro[i][col] < 10:
            esta = kakuro[i][col] not in duplicates
            duplicates.add(kakuro[i][col])
            if esta:
                pass
            else:
                return True
            i -= 1
        return False

    def isMaxLen(self, row, col):
        kakuro = self.kakuro
        duplicates = set()
        i = row
        while i > 0 and kakuro[i][col] < 10:
            duplicates.add(kakuro[i][col])
            i -= 1
        if len(duplicates) == 9:
            return True
        return False

    def topRow(self, row, col):
        kakuro = self.kakuro
        resultRow = set()
        i = row-1
        while i > 0 and kakuro[i][col] < 10:
            resultRow.add(kakuro[i][col])
            i -= 1
        return resultRow

    def addendForNonRepits(self, row, col, hSet):
        kakuro = self.kakuro
        topRow = self.topRow(row,col)
        fullSet = [1,2,3,4,5,6,7,8,9]

        for i in hSet:
            fullSet.remove(i)

        for i in topRow:
            if i in fullSet:
                fullSet.remove(i)
        fLen = len(fullSet)
        if fLen == 1:
            return fullSet[0]
        if fLen > 1:
            ind = random.randrange(0,fLen)
            return fullSet[ind]
        return 10




    def hAdd(self, row, col):
        sum = 0
        inBounds = True
        j = col + 1
        while (j < self.size) and inBounds:
            if len(self.kakuro[row][j]) == 1:
                sum += self.kakuro[row][j][0]
            else:
                inBounds = False
            j += 1
        return sum

    def vAdd(self, row, col):
        sum = 0
        inBounds = True
        i = row + 1
        while (i < self.size) and inBounds:
            if len(self.kakuro[i][col]) == 1:
                sum += self.kakuro[i][col][0]
            else:
                inBounds = False
            i += 1
        return sum

    def generate(self):
        kakuro = self.kakuro
        size = self.size
        for i in range(1, size):
            hSet = set()
            for j in range(1, size):
                nextN = 0
                if kakuro[i][j] == 10 or (len(hSet) == 0 and j == (size-1)):
                    kakuro[i][j] = 10
                    hSet.clear()
                elif (len(hSet) == 1) or (len(self.topRow(i,j)) == 1) or (random.randrange(0, 5) >= 3):
                    nextN = self.addendForNonRepits(i, j, hSet)
                    estaEn = nextN in hSet
                    #hSet.add(nextN)
                    if nextN == 10:
                        print("Es 10", i, j)
                        kakuro[i][j] = 10
                        if len(hSet) == 1:
                            kakuro[i][j-1] = 10
                        hSet.clear()
                    elif estaEn:
                        kakuro[i][j] = 10
                        hSet.clear()
                    elif not self.isDuplicated(i, j, nextN):
                        hSet.add(nextN)
                        kakuro[i][j] = nextN
                    else:
                        kakuro[i][j] = 10
                        hSet.clear()
                else:
                    kakuro[i][j] = 10
                    hSet.clear()

        for row, col in product(range(size), repeat=2):
            if kakuro[row][col] == 10:
                kakuro[row][col] = []
            else:
                kakuro[row][col] = [kakuro[row][col]]

        for i in range(0, size):
            for j in range(0, size):
                if kakuro[i][j] == []:
                    top = self.hAdd(i, j)
                    bottom = self.vAdd(i, j)
                    if top == 0 and bottom == 0:
                        kakuro[i][j] += []
                    else:
                        kakuro[i][j] += [bottom, top]

        return kakuro

    def getNewBoard(self):
        kakuro = self.generate()
        for row, col in product(range(self.size), repeat=2):
            if len(kakuro[row][col]) == 1:
                kakuro[row][col] = [0]
        self.kakuro = kakuro
        return kakuro

    def getStrucForSolver(self):
        if self.kakuro == []:
            return []
        kakuro = self.kakuro
        newBoard = self.blankBoard()
        strs = ''
        for i in range(self.size):
            strs += '['
            for j in range(self.size):
                strs += '['
                if len(kakuro[i][j]) == 0:
                    strs += 'Brick()'
                    newBoard[i][j] = Brick()
                elif len(kakuro[i][j]) == 1:
                    strs += 'Blank()'
                    newBoard[i][j] = Blank()
                else:
                    if kakuro[i][j][1] == 0:
                        strs += "Brick(v=" + str(kakuro[i][j][0]) + ")"
                        newBoard[i][j] = Brick(v=kakuro[i][j][0])
                    elif kakuro[i][j][0] == 0:
                        strs += 'Brick(h=' + str(kakuro[i][j][1]) + ')'
                        newBoard[i][j] = Brick(h=kakuro[i][j][1])
                    else:
                        strs += 'Brick(v=' + str(kakuro[i][j][0])  + ', h=' +  str(kakuro[i][j][1]) + ')'
                        newBoard[i][j] = Brick(v=kakuro[i][j][0], h=kakuro[i][j][1])
                strs += '],'
            strs += ']\n'
        #print(strs)
        return newBoard

def printLista(lista):
    for i in range(0, len(lista)):
        print(lista[i])
    print("\n")

"""
mak = kakuroMaker(11).generate()
print(mak)
"""

# solucionado = False
# while not solucionado:
#
#     mak = kakuroMaker(10)
#     lista = mak.generate()
#     print(lista)
#
#     board = traslate(lista)
#     k = KakuroBoard(board)
#
#     for entries in k.solve():
#         solucionado = True
#         print('*** SOLUTION ***')
#         # for entry in entries:
#         #    print '%2s: %s' % (entry.myID, entry.possibleValues)
#         str = ''
#         for row in board:
#             for col in row:
#                 if isinstance(col, Brick):
#                     str += '_ '
#                 else:
#                     str += '%s ' % entries[col.myID].possibleValues[0]
#             str += '\n'
#         print(str)
#         break




