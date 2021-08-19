import sys
x=int(sys.argv[1])
upList=["".join(["*" for item in range(1,i+1)]) for i in range(1,2*x-1,2)]
upList=[i*" "+upList[-i] for i in range(len(upList),0,-1)]
print(*upList,sep="\n")
downList = ["".join(["*" for item in range(1,i+1)])for i in range(2*x-1,0,-2)]
downList = [i*" "+downList[i] for i in range(0,len(downList))]
print(*downList,sep="\n",end="")