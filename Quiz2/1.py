import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if b ** 2 - 4 * a * c < 0:
    print("There isn't real solution(s)")
elif b ** 2 - 4 * a * c == 0:
    print("There is one solution")
    root = ((-b + (b ** 2-4 * a * c) ** (1 / 2))/(2 * a))
    print("Solution(s):", "{:.2f}".format(root))
else:
    print("There are two solutions")
    root1 = ((-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a))
    root2 = ((-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a))
    print("Solution(s):", "{:.2f}".format(root1), "{:.2f}".format(root2))
# End Of The File
