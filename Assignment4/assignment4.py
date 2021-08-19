import sys
import itertools
starter=[]
myList=[]
rightWay=[]
path=[]
turnout=[]
def reader(n):
    file = open(sys.argv[n], "r", encoding="utf-8")
    counter = 0
    for i in file:
        i=i.strip("\n")
        myList.append([item for item in i])
        if "S" in i :
            global startColumn
            startColumn=myList[counter].index("S")
            global startRow
            startRow=counter
        if "F" in i :
            global stopColumn
            stopColumn=myList[counter].index("F")
            global stopRow
            stopRow=counter
        counter += 1
    file.close()
def writer(q):
    if [stopRow,stopColumn] in rightWay:
        for m,n in rightWay[1:-1]:
            myList[m][n]="1"
    else:
        for m,n in rightWay[1:]:
            myList[m][n]="1"
    for a in myList:
        for g in range(len(a)):
            if a[g]=="W" or a[g]=="P" or a[g]=="H":
                a[g]="0"
    file = open(sys.argv[4], q, encoding="utf-8")
    for y in myList:
        y=", ".join(y)
        file.write(y+"\n")
    file.write("\n")
    file.close()
reader(1)
def myFun(x,y):
    if [stopRow, stopColumn] in path:
        return
    number=0
    path.append([x, y])
    rightWay.append([x,y])
    if x < len(myList)-1:
        if myList[x+1][y]!="W" :
            number+=1
    if y < len(myList[0]) - 1:
        if myList[x][y+1]!="W" :
            number += 1
    if x > 0:
        if myList[x-1][y]!="W" :
            number += 1
    if y > 0:
        if myList[x][y-1]!="W" :
            number+=1
    if number > 1 and x == startRow and y == startColumn:
        if number == 2:
            starter.append(1)
        if number == 3:
            starter.append(2)
        if number == 4:
            starter.append(3)
    if number>2 and [x,y] not in turnout:
        turnout.append([x,y])
    if x < len(myList)-1:
        if myList[x+1][y]!="W" and [x+1,y] not in path:
            return myFun(x+1,y)
    if y < len(myList[0]) - 1:
        if myList[x][y+1]!="W" and [x,y+1] not in path:
            return myFun(x,y+1)
    if x > 0:
        if myList[x-1][y]!="W" and [x-1,y] not in path :
            return myFun(x-1,y)
    if y > 0:
        if myList[x][y-1]!="W" and [x,y-1] not in path :
            return myFun(x,y-1)
    i = 1
    if len(turnout) > 0:
        if turnout[-i] == rightWay[-1]:
            turnout.remove(turnout[-i])
            if len(turnout) == 0:
                return
        if [stopRow, stopColumn] not in path:
            rightWay[rightWay.index(turnout[-i]):] = []
        myFun(int(str(turnout[-i][0])), int(str(turnout[-i][1])))
myFun(startRow,startColumn)
if len(starter) > 0:
    if [stopRow, stopColumn] not in path:
        rightWay=[]
        now=[]
        for l in range(starter[0]):
            myFun(startRow, startColumn)
            if [stopRow, stopColumn] in path:
                break
writer("w")
myList=[]
reader(2)
def health(x,y,z):
    now.append(z)
    if [stopRow, stopColumn] in path and z >= 0:
        now.pop()
        return
    elif z<0:
        i=1
        if turnout[-i] == rightWay[-1]:
            turnout.remove(turnout[-i])
        if len(turnout) == 0:
            return
        now[rightWay.index(turnout[-i]):] = []
        rightWay[rightWay.index(turnout[-i]):] = []
        health(int(str(turnout[-i][0])), int(str(turnout[-i][1])), now[-1] - 1)
    else:
        number = 0
        path.append([x, y])
        rightWay.append([x, y])
        if x < len(myList) - 1:
            if myList[x + 1][y] != "W":
                number += 1
        if y < len(myList[0]) - 1:
            if myList[x][y + 1] != "W":
                number += 1
        if x > 0:
            if myList[x - 1][y] != "W":
                number += 1
        if y > 0:
            if myList[x][y - 1] != "W":
                number += 1
        if number > 1 and x==startRow and y==startColumn:
            if number == 2:
                starter.append(1)
            if number == 3:
                starter.append(2)
            if number==4:
                starter.append(3)
        if number > 2 and [x, y] not in turnout:
            turnout.append([x, y])
        for g in direction:
            g(x,y,z)
        i = 1
        if len(turnout) > 0:
            if [stopRow, stopColumn] in path and now[-1] >= 0:
                return
            else:
                if turnout[-i] == rightWay[-1]:
                    turnout.remove(turnout[-i])
                if len(turnout) == 0:
                    return
                now[rightWay.index(turnout[-i]):] = []
                rightWay[rightWay.index(turnout[-i]):] = []
                health(int(str(turnout[-i][0])), int(str(turnout[-i][1])), now[-1] - 1)
def direction1(x,y,z):
    if x < len(myList) - 1:
        if myList[x + 1][y] != "W" and [x + 1, y] not in path:
            if myList[x + 1][y] == "H":
                if z>0:
                    z=int(sys.argv[3])+1
            return health(x + 1, y,z-1)
def direction2(x,y,z):
    if y < len(myList[0]) - 1:
        if myList[x][y + 1] != "W" and [x, y + 1] not in path:
            if myList[x][y+1] == "H":
                if z>0:
                    z=int(sys.argv[3])+1
            return health(x, y+1 ,z-1)
def direction3(x,y,z):
    if x > 0:
        if myList[x - 1][y] != "W" and [x - 1, y] not in path:
            if myList[x-1][y] == "H":
                if z>0:
                    z=int(sys.argv[3])+1
            return health(x - 1, y,z-1)
def direction4(x,y,z):
    if y > 0:
        if myList[x][y - 1] != "W" and [x, y - 1] not in path:
            if myList[x][y-1] == "H":
                if z>0:
                    z=int(sys.argv[3])+1
            return health(x, y - 1,z-1)
direction=[direction1,direction2,direction3,direction4]
allDirection=list(itertools.permutations(direction))
shortest=[]
lenght=[]
for i in allDirection:
    direction=i
    starter = []
    now = []
    rightWay = []
    path = []
    turnout = []
    health(startRow, startColumn, int(sys.argv[3]))
    if len(starter)>0:
        if [stopRow, stopColumn] not in path:
            rightWay=[]
            now=[]
            for l in range(starter[0]):
                health(startRow, startColumn, int(sys.argv[3]))
                if [stopRow, stopColumn] in path:
                    break
    shortest.append(rightWay)
for i in shortest:
    lenght.append(len(i))
    rightWay=shortest[lenght.index(min(lenght))]
writer("a")
