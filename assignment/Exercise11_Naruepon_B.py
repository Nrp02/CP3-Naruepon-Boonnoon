i = int(input())
a = " "
b = "*"
c = 0
for x in range(i):
    print(a * (i - x - 1) + b * (x + c + 1))
    c += 1
 
    