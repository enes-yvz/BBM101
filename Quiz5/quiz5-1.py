import sys
x=int(sys.argv[1])
def upPart(n,counter):
    if n==2*x-1:
        return downPart(2*x-1,2*x-1)
    else:
        item=n*"*"
        print(item.rjust(counter, " "))
        return upPart(n+2,counter+1)
def downPart(n,counter):
    if n<0:
        return
    else:
        item = n*"*"
        if n==1 :
            print(item.rjust(counter, " "),end="")
        else:
            print(item.rjust(counter, " "))
        return downPart(n-2,counter-1)
upPart(1,x)