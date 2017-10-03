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
        return gameList

    def nextAddend(self, added):
        setLen = 5
        nextN = random.randrange(1, 10)
        while setLen > 0:
            if nextN in added:
                nextN = random.randrange(1, 10)
                setLen -= 1
            break

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
                if random.randrange(0, 15) > 0:
                    nextN = self.nextAddend(hSet)
                    esta = nextN not in hSet
                    hSet.add(nextN)
                    if not esta:
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
        for i in range(self.size):
            for j in range(self.size):
                if len(kakuro[i][j]) == 0:
                    newBoard[i][j] = Brick()
                elif len(kakuro[i][j]) == 1:
                    newBoard[i][j] = Blank()
                else:
                    if kakuro[i][j][1] == 0:
                        newBoard[i][j] = Brick(v=kakuro[i][j][0])
                    elif kakuro[i][j][0] == 0:
                        newBoard[i][j] = Brick(h=kakuro[i][j][1])
                    else:
                        newBoard[i][j] = Brick(v=kakuro[i][j][0], h=kakuro[i][j][1])
        return newBoard

def printLista(lista):
    for i in range(0, len(lista)):
        print(lista[i])
    print("\n")

mak = kakuroMaker(10)
lista = mak.generate()

board1 = mak.getStrucForSolver()


board = [[Brick(), Brick(v=14), Brick(v=5), Brick(v=28), Brick(v=3), Brick(), Brick(), Brick(v=26), Brick(v=5),
              Brick(v=22)],
             [Brick(h=12), Blank(), Blank(), Blank(), Blank(), Brick(v=12, h=24), Blank(), Blank(), Blank(), Blank()],
             [Brick(h=23), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(v=32, h=21), Blank(), Blank(), Blank()],
             [Brick(), Brick(v=7), Brick(v=39), Blank(), Brick(h=6), Blank(), Blank(), Blank(), Brick(v=24), Blank()],
             [Brick(h=20), Blank(), Blank(), Blank(), Brick(v=19, h=27), Blank(), Blank(), Blank(), Blank(),
              Brick(v=34)],
             [Brick(h=6), Blank(), Blank(), Brick(v=22, h=23), Blank(), Blank(), Blank(), Brick(v=13, h=15), Blank(),
              Blank()],
             [Brick(h=14), Blank(), Blank(), Blank(), Blank(), Brick(h=14), Blank(), Blank(), Blank(), Blank()],
             [Brick(), Brick(v=6, h=22), Blank(), Blank(), Blank(), Brick(v=4, h=16), Blank(), Blank(), Brick(v=17),
              Blank()],
             [Brick(h=21), Blank(), Blank(), Blank(), Brick(h=24), Blank(), Blank(), Blank(), Blank(), Blank()],
             [Brick(h=15), Blank(), Blank(), Blank(), Blank(), Blank(), Brick(h=20), Blank(), Blank(), Blank()]]

print(board1)
print(board)

# k = KakuroBoard(board)
# for entries in k.solve():
#     print('*** SOLUTION ***')
#     # for entry in entries:
#     #    print '%2s: %s' % (entry.myID, entry.possibleValues)
#     str = ''
#     for row in board:
#         for col in row:
#             if isinstance(col, Brick):
#                 str += '_ '
#             else:
#                 str += '%s ' % entries[col.myID].possibleValues[0]
#         str += '\n'
#     print(str)




