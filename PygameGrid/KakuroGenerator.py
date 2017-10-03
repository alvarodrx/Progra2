import random
import pprint
import numpy as np
from itertools import *

class generator:
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
        for i in range(0,size):
            gameList[0][i] = 10
            gameList[i][0] = 10
        return gameList

    def nextAddend(self):
        nextN = random.randrange(3,10)
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
        i = col + 1
        while (i < self.size) and inBounds:
            if len(self.kakuro[i][col]) == 1:
                sum += self.kakuro[i][col][0]
            else:
                inBounds = False
            i += 1
        return sum

    def generate(self):
        kakuro = self.kakuro
        kakuro[5][5] = 5

        size = self.size
        for i in range(1,size):
            hSet = set()
            for j in range(1, size):
                nextN = self.nextAddend()
                esta = nextN not in hSet
                hSet.add(nextN)
                if not esta:
                    kakuro[i][j] = 10
                    hSet.clear()
                elif not self.isDuplicated(i, j, nextN):
                    hSet.add(nextN)
                    kakuro[i][j] = nextN
                else:
                    print(nextN)
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
                        pass
                    else:
                        kakuro[i][j] += [bottom, top]
        return kakuro


# lista = generator(20).generate()
#
#
# for i in range(0, len(lista)):
#     print(lista[i])









