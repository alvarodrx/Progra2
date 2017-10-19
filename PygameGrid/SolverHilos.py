from copy import deepcopy
from itertools import *
import threading
from queue import Queue
import time

class beanKakuro:
    def __init__(self, boardCopy, row, col, prom):
        self. board = boardCopy
        self.row = row
        self.col = col
        self.prom = prom

class KakuroSolver:
    def __init__(self, board):
        self.MaxHilos = 100
        self.board = board
        self.size = len(board)
        self.mutex = threading.Lock()  # esta variable se encarga de mantener una sincronia entre los hilos
        self.cola = Queue()
        self.flag = 0
        self.boardResult = []
        self.BeanInfo = False


    def getCellsLen(self, board, row, col):
        """Obtiene la cantidad de celdas para una
        suma tanto para columna como para fila"""
        sizeBoard = len(board)
        colLen = 0
        rowLen = 0
        nextRow = row + 1
        while nextRow < sizeBoard and len(board[nextRow][col]) == 1:
            colLen += 1
            nextRow += 1
        nextCol = col + 1
        while nextCol < sizeBoard and len(board[row][nextCol]) == 1:
            rowLen += 1
            nextCol += 1

        return colLen, rowLen

    def getValForLen(self, listLen, sumTotal, actList):
        """Obtiene las permutaciones del conjunto de valores
        posibles para la suma y cantidad de celdas dadas """
        if len(actList) == listLen:
            if sumTotal == sum(actList):
                yield actList
            return
        valueList = 0
        if actList:
            valueList = range(actList[len(actList) - 1] + 1, 10)
        else:
            valueList = range(1, 10)
        for i in valueList:
            copyList = deepcopy(actList)
            copyList.append(i)
            if sum(copyList) == sumTotal and len(copyList) == listLen:
                yield copyList
            if sum(copyList) >= sumTotal:
                return
            # Baktracking aplicado
            yield from self.getValForLen(listLen, sumTotal, copyList)

    def getValuesForLen(self, listLen, sumTotal, actList):
        result = self.getValForLen(listLen, sumTotal, actList)
        newList = []
        for solution in result:
            newList.append(solution)
        return newList

    def setPosibleValues(self, boardM):
        board = deepcopy(boardM)
        size = self.size
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if len(col) == 2:
                    rowLen, colLen = self.getCellsLen(board, y, x)
                    sumsForRow = self.getValuesForLen(rowLen, col[0], [])
                    sumsForCol = self.getValuesForLen(colLen, col[1], [])
                    # print(col)
                    # print("rowlen",rowLen)
                    # print("colLen",colLen)
                    # print(sumsForRow)
                    # print(sumsForCol)

                    posy = y+1
                    for i in range(rowLen):
                        if type(board[posy][x][0]) != list:
                            board[posy][x][0] = [deepcopy(sumsForRow),[]]
                        else:
                            board[posy][x][0][0] = deepcopy(sumsForRow)
                        posy += 1
                    posx = x + 1
                    for i in range(colLen):
                        if type(board[y][posx][0]) != list:
                            board[y][posx][0] = [[],deepcopy(sumsForCol)]
                        else:
                            board[y][posx][0][1] = deepcopy(sumsForCol)
                        posx += 1
        # for i, j in product(range(size), repeat=2):
        #     if len(board[i][j]) == 1:
        #         board[i][j][0] = self.getPromissingList(board[i][j][0])
        return board

    def getPromissingList(self, vhList):
        vList = vhList[0]
        hList = vhList[1]
        hSet = set()
        vSet = set()
        result = set()
        for i in vList:
            for n in i:
                vSet.add(n)
        for i in hList:
            for n in i:
                hSet.add(n)
        for i in hSet:
            if i in vSet:
                result.add(i)

        return result

    def recalculateLists(self, vLists, value):
        #print(vLists)
        nvList = []
        for i in vLists:
            if value in i:
                i.remove(value)
                nvList.append(i)
        return nvList

    def recalculateValues(self, boardM, row, col, value):
        board = deepcopy(boardM)
        size = self.size
        board[row][col][0] = value
        rowM = 1 + row
        while rowM < size and len(board[rowM][col]) == 1:
            #print(rowM, col)
            board[rowM][col][0][0] = self.recalculateLists(board[rowM][col][0][0], value)
            rowM += 1
        colM = 1 + col
        while colM < size and len(board[row][colM]) == 1:
            #print(row,colM)
            board[row][colM][0][1] = self.recalculateLists(board[row][colM][0][1], value)
            colM += 1
        return board

    def nextBlank(self, row, col):
        size = self.size
        for i, j in product(range(size), repeat=2):
            if ((i == row and j > col) or (i > row)) and (len(self.board[i][j]) == 1):
                return i, j
        return 0, 0


    def prueba(self):
        while True:
            print('Solucionando!')
            time.sleep(0.8)
            if(self.boardResult != []):
                print('Ya hay solucion!!!')
                break


    def threader(self, numero):
        #while self.flag != 1:
        self.BeanInfo = beanKakuro(self.BeanInfo.board,self.BeanInfo.row,self.BeanInfo.col,numero)
        self.solucionador(self.BeanInfo)
        #self.cola.task_done()

    def funcionX(self, beanObj):
        print(beanObj.board, beanObj.row, beanObj.col, beanObj.prom)

    def solucionador(self, beanObj):
        #ahora = time.time()
        solution = self.solver(beanObj.board, beanObj.row, beanObj.col, beanObj.prom)
        #print('La recursion tomo: ', time.time()-ahora, threading.current_thread().name)
        if solution:
            #print("SOLUCIOOOON")
            self.boardResult = solution
            return solution
        return



    def solve(self, board=[], row=0, col=0, promList = set()):
        if not board:
            boardCopy = self.setPosibleValues(self.board)
            row, col = self.nextBlank(1,0)
            promList = self.getPromissingList(boardCopy[row][col][0])
            print("promlist:", promList)
            #hilo = threading.Thread(target=self.prueba)
            #hilo.start()
            #self.BeanInfo = beanKakuro(boardCopy,row,col,0)
            for prometedor in promList:
                thread = threading.Thread(target=self.solucionador, args=(beanKakuro(boardCopy,row,col,prometedor),))
                thread.daemon = True
                self.MaxHilos -= 1
                thread.start()

            print("Hilos hechos")

            while not self.boardResult:
                pass

            return self.boardResult
        else:
            self.mutex.acquire()
            actuales = self.MaxHilos
            self.mutex.release()
            if actuales >= 0:
                boardCopy = deepcopy(board)
                for prometedor in promList:
                    thread = threading.Thread(target=self.solucionador, args=(beanKakuro(boardCopy,row,col,prometedor),))
                    thread.daemon = True
                    self.MaxHilos -= 1
                    thread.start()

                print("Hilos hechos", self.MaxHilos)

            else:
                #self.mutex.release()
                while promList != set():
                    j = self.solver(board, row, col, promList.pop())
                    if type(j) == list and j:
                        promList.clear()
                        return j
            while not self.boardResult:
                pass

            return self.boardResult



    def solver(self, boardM, row, col, prom):
        board = self.recalculateValues(boardM, row, col, prom)
        row, col = self.nextBlank(row, col)
        if self.boardResult != []:
            return []
        if row == 0 or col == 0: #Esta completo
            print("Listo")
            self.flag = 1
            self.boardResult = board
            return board
        else:
            promList = self.getPromissingList(board[row][col][0])
            if promList == set():
                return []
            while promList != set():
                j = self.solver(board, row, col, promList.pop())
                if type(j) == list and j:
                    promList.clear()
                    return j








def printLista(lista)::
    for i in range(0, len(lista))
        print(lista[i])
    print("\n")

board = [
    [[],[5,0],[12,0]],
    [[0,6],[1],[5]],
    [[0,11],[4],[7]]
]

board2 = [
    [[],[8,0],[12,0],[]],
    [[0,6],[1],[5],[3,0]],
    [[0,12],[4],[7],[1]],
    [[0,3],[3],[0,2],[2]]
]

board1 = [[[],[14,0],[5,0],[28,0],[3,0],[],[],[26,0],[5,0],[22,0]],
         [[0,12],[0],[0],[0],[0],[12,24],[0],[0],[0],[0]],
         [[0,23],[0],[0],[0],[0],[0],[32,21],[0],[0],[0]],
         [[],[7,0],[39,0],[0],[0,6],[0],[0],[0],[24,5],[0]],
         [[0,20],[0],[0],[0],[19,27],[0],[0],[0],[0],[34,0]],
         [[0,6],[0],[0],[22,23],[0],[0],[0],[13,15],[0],[0]],
         [[0,14],[0],[0],[0],[0],[0,14],[0],[0],[0],[0]],
         [[],[6,22],[0],[0],[0],[4,16],[0],[0],[17,8],[0]],
         [[0,21],[0],[0],[0],[2,24],[0],[0],[0],[0],[0]],
         [[0,15],[0],[0],[0],[0],[0],[0,20],[0],[0],[0]]]

boar5 = [[[], [16, 0], [18, 0], [24, 0], [22, 0]], [[0, 17], [1], [8], [6], [2]], [[0, 22], [5], [6], [7], [4]], [[0, 17], [4], [1], [3], [9]], [[0, 24], [6], [3], [8], [7]]]
board5 = [[[], [5, 0], [], [15, 0], [7, 0]], [[0, 5], [5], [20, 7], [1], [6]], [[], [1, 11], [3], [7], [1]], [[0, 11], [1], [8], [2], []], [[], [0, 14], [9], [5], []]]
board6 = [[[], [27, 0], [15, 0], [25, 0], [19, 0], [13, 0]], [[0, 23], [1], [6], [3], [9], [4]], [[0, 30], [5], [2], [8], [6], [9]], [[0, 22], [9], [7], [5], [1], [7, 0]], [[0, 8], [8], [1, 12], [2], [3], [7]], [[0, 12], [4], [1], [7], [], []]]
board7 = [[[], [27, 0], [27, 0], [], [21, 0], [], []], [[0, 7], [1], [6], [24, 5], [5], [28, 0], [29, 0]], [[0, 27], [4], [3], [7], [6], [2], [5]], [[0, 26], [5], [7], [3], [2], [8], [1]], [[0, 32], [9], [2], [4], [3], [6], [8]], [[0, 31], [2], [9], [8], [1], [5], [6]], [[0, 6], [6], [0, 22], [2], [4], [7], [9]]]
board8 = [[[], [], [9, 0], [35, 0], [], [4, 0], [16, 0], []], [[], [17, 12], [9], [3], [8, 11], [4], [7], [7, 0]], [[0, 8], [8], [7, 7], [5], [2], [0, 16], [9], [7]], [[0, 28], [9], [5], [8], [6], [11, 0], [], []], [[], [9, 11], [2], [9], [9, 8], [8], [], []], [[0, 9], [9], [6, 16], [4], [9], [3], [12, 0], [10, 0]], [[], [0, 10], [4], [6], [], [6, 11], [5], [6]], [[], [0, 2], [2], [], [0, 17], [6], [7], [4]]]
board9 = [[[], [], [22, 0], [], [], [2, 0], [20, 0], [17, 0], [23, 0]], [[], [5, 6], [6], [1, 0], [10, 19], [2], [5], [4], [8]], [[0, 21], [5], [9], [1], [6], [9, 11], [2], [3], [6]], [[], [1, 7], [7], [13, 33], [4], [9], [7], [8], [5]], [[0, 1], [1], [20, 9], [9], [25, 0], [12, 12], [6], [2], [4]], [[], [14, 22], [2], [4], [9], [7], [], [], []], [[0, 13], [5], [8], [0, 12], [7], [5], [], [], []], [[0, 15], [9], [6], [7, 3], [3], [2, 0], [8, 0], [3, 0], []], [[], [0, 30], [4], [7], [6], [2], [8], [3], []]]
board10 =[[[], [], [], [6, 0], [10, 0], [], [], [], [20, 0], []], [[], [5, 0], [19, 15], [6], [9], [], [17, 0], [1, 8], [8], [10, 0]], [[0, 6], [5], [1], [0, 1], [1], [0, 17], [9], [1], [4], [3]], [[], [6, 7], [7], [9, 0], [], [15, 5], [5], [4, 3], [1], [2]], [[0, 18], [1], [8], [9], [10, 21], [2], [3], [4], [7], [5]], [[0, 8], [5], [3], [0, 9], [1], [8], [24, 0], [21, 0], [8, 0], []], [[], [6, 0], [], [10, 31], [9], [5], [7], [4], [6], []], [[0, 4], [4], [12, 6], [6], [3, 0], [0, 12], [3], [7], [2], []], [[0, 12], [2], [5], [4], [1], [3, 17], [8], [9], [8, 0], [9, 0]], [[], [0, 7], [7], [0, 29], [2], [3], [6], [1], [8], [9]]]
board11 = [[[], [], [40, 0], [21, 0], [], [], [], [], [19, 0], [24, 0], [13, 0]], [[], [0, 9], [3], [6], [], [], [], [0, 20], [5], [7], [8]], [[], [0, 8], [7], [1], [], [], [], [9, 19], [6], [8], [5]], [[], [11, 9], [4], [5], [], [], [23, 21], [4], [8], [9], []], [[0, 16], [5], [2], [9], [8, 0], [17, 7], [2], [5], [5, 0], [12, 0], []], [[0, 7], [6], [1], [12, 20], [5], [6], [9], [0, 6], [1], [5], [16, 0]], [[], [12, 22], [6], [1], [3], [7], [5], [0, 17], [4], [6], [7]], [[0, 21], [9], [8], [4], [0, 5], [4], [1], [16, 0], [0, 10], [1], [9]], [[0, 14], [3], [9], [2], [5, 0], [0, 8], [6], [2], [14, 0], [10, 0], []], [[], [], [0, 9], [5], [4], [4, 0], [0, 19], [6], [9], [4], []], [[], [], [], [0, 5], [1], [4], [0, 19], [8], [5], [6], []]]
board15 =[[[], [], [], [4, 0], [], [], [], [], [20, 0], [], [9, 0], [8, 0], [37, 0], [], []], [[], [5, 0], [0, 4], [4], [], [27, 0], [], [0, 1], [1], [0, 21], [9], [8], [4], [27, 0], [14, 0]], [[0, 5], [5], [4, 0], [6, 0], [7, 8], [8], [], [0, 2], [2], [1, 0], [], [5, 19], [9], [4], [6]], [[], [6, 18], [4], [6], [7], [1], [21, 0], [6, 7], [6], [1], [9, 22], [4], [3], [7], [8]], [[0, 6], [6], [25, 0], [], [0, 30], [9], [7], [6], [8], [9, 16], [7], [1], [5], [3], []], [[], [2, 6], [6], [15, 0], [0, 12], [3], [9], [0, 14], [3], [9], [2], [6, 9], [1], [8], [4, 0]], [[0, 10], [2], [3], [5], [0, 11], [6], [5], [], [6, 0], [34, 0], [0, 12], [1], [2], [5], [4]], [[], [0, 15], [7], [8], [], [16, 0], [7, 0], [16, 6], [4], [2], [14, 11], [5], [6], [], []], [[], [5, 11], [9], [2], [5, 30], [9], [7], [3], [2], [4], [5], [5, 7], [7], [18, 0], []], [[0, 5], [5], [], [15, 12], [5], [7], [0, 2], [2], [0, 15], [1], [9], [5], [4, 3], [3], [8, 0]], [[], [22, 0], [0, 8], [8], [9, 0], [], [0, 6], [6], [0, 8], [8], [4, 0], [0, 15], [4], [9], [2]], [[0, 6], [6], [0, 11], [2], [9], [4, 0], [10, 5], [5], [3, 13], [9], [4], [], [4, 7], [1], [6]], [[0, 7], [7], [0, 5], [5], [0, 5], [4], [1], [0, 10], [3], [7], [], [0, 9], [4], [5], []], [[0, 4], [4], [3, 0], [8, 0], [], [0, 3], [3], [3, 0], [9, 3], [3], [6, 0], [5, 0], [], [], []], [[0, 16], [5], [3], [8], [], [0, 18], [6], [3], [9], [0, 11], [6], [5], [], [], []]]

ahora = time.time()
x = KakuroSolver(board7)
lista = x.solve()
print(lista)
print('todo el trabajo duro: ',time.time()-ahora,' segundos')

# [   [[],    [5, 0],                                     [12, 0]],
#  [[0, 6], [[[[1, 4], [2, 3]], [[1, 5], [2, 4]]]],   [[[[3, 9], [4, 8], [5, 7]], [[1, 5], [2, 4]]]]],
#  [[0, 11], [[[[1, 4], [2, 3]], [[2, 9], [3, 8],     [4, 7], [5, 6]]]], [[[[3, 9], [4, 8], [5, 7]], [[2, 9], [3, 8], [4, 7], [5, 6]]]]]]
