import sys
inputFile = open(sys.argv[1],"r")
myList=[]
messageID=[]
finalList=[]
counter=0
part=0
number=1
for line in inputFile:
    line = line.strip("\n")
    line=line.split("\t")
    line[0]=int(line[0])
    line[1]=int(line[1])
    myList.append(line)
for i in myList:
    messageID.append(i[0])
setID=set(messageID)
setID=list(setID)
setID.sort()
myList.sort(key=lambda x: x[0])
outputFile=open(sys.argv[2],"w")
while part<len(myList):
    for i in setID:
        part += messageID.count(i)
        newList=myList[counter:part]
        newList.sort(key=lambda x: x[1])
        finalList.append(newList)
        counter=part
for item in finalList:
    outputFile.write("Message"+" "+str(number)+"\n")
    number+=1
    for i in item :
        i[0] = str(i[0])
        i[1] = str(i[1])
        i="\t".join(i)
        i=str(i)
        i=i.strip("[]")
        outputFile.write(i + "\n")
inputFile.close()
outputFile.close()