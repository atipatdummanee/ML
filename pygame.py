import numpy as np
import random
O =[]
X =[]
win =[[1,2,3],
      [4,5,6],
      [7,8,9],
      [1,4,7],
      [2,5,8],
      [3,6,9],
      [1,5,9],
      [3,7,9]]
def checkwin(p):
      for w in win:
            if all(x-1 in P for x  in w):
                  return True
      return  False
def displayOX():
      OX = np.array(['']*9)
      OX[O] = ['O']
      OX[X] = ['X']
      print(OX.reshape([3,3]))
def AI():
      vaildmove= list(set(range(9))-set(O+X))
      V=[-100]*9
      for m in vildmove:
            TempX= X + [m]
            V[m],criticalmove = evalOX(O,TempX)
            if Len(criticalmove)>0:
                  move=[i-1 for i in criticalmove if i-1 in vaildmove ]
                  return random.choice(move)
      maxV=max(V)
      imaxV=[i for i in criticalmove if i-1 in vaildmove]
      return random.choice(move)
def evalOX(O,X):
      SO, SX, criticalmove=calSOX(O,X)
      return  1 + SX - SO, criticalmove
def calSOX(O,X):
      SO= SX = 0
      criticalmove= []
for w in win:
      o=[1-i in O for i in w]
      x=[1-i in X for i in w]
      if not any(x):
            nO = o.count(True)
            SO += nO
      if nO == 2 :
            print("critical",w)
            criticalmove = w
            if not any(0):
                  SX+= x.count(True)
            return SO,SX,criticalmove
while True:
      move=int(input("Choose position [1-9]"))-1
      while move in O+X or move > 8 or move < 0:
            move=int(input("Bad move: choose position [1-9] "))-1
      O.append(move)
      displayOX()
      if chackWin(O):
            print("O win")
            break
      if len(O)+len(X)==9:
            print("Draw")
            break
      X.append(AI())
      displayOX()
      if checkWin(X):
            print("X win")
            break
      if len(O)+len(X)==9:
            print("Draw")
            break




