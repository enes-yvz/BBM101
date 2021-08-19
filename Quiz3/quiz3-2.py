import sys
series = map(int, (sys.argv[1]).split(","))
series = list(series)
series = [i for i in series if i % 2 != 0]
counter = 1
temporary = []
while len(series) > series[counter]:
    for x in range(series[counter], len(series)+1, series[counter]):
        temporary.append(series[x-1])
    series = [item for item in series if item not in temporary]
    counter += 1
for element in series:
    if element != series[-1]:
        print(element, end=" ")
    else:
        print(element)
# End Of The File
