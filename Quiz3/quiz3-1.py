import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = a ** b
sums = []
digits = []
while c > 9:
    x = [int(i) for i in str(c)]
    digits.append(x)
    c = sum(x)
    sums.append(c)
print(str(a)+"ˆ"+str(b)+" = "+str(a**b)+" = ", end="")
for number in range(len(digits)):
    digits[number] = map(str, digits[number])
    digits[number] = list(digits[number])
    digits[number] = " + ".join(digits[number])
    print(digits[number], "=", sums[number], end="")
    if number < len(digits)-1:
        print(" = ", end="")
# End Of The File
