import sys
temporary = map(int, (sys.argv[1]).split(","))
evenNumber = []
summationEven = 0
summationAll = 0
for i in temporary:
    if i < 0:
        pass
    else:
        summationAll += i
        if i % 2 == 0:
            evenNumber.append(i)
            summationEven += i
evenNumber = map(str, evenNumber)
evenNumber = list(evenNumber)
evenNumber = ",".join(evenNumber)
print("Even Numbers:", '"'+evenNumber+'"')
print("Sum of Even Numbers:", summationEven)
print("Even Number Rate:", "{:.3f}".format(summationEven/summationAll))
# End Of The File
