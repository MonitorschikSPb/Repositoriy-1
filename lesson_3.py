n = int(input())
sum = 0
if n>100:
    print("Error! Input the correct numbers!")
else:
    for i in range(n+1):
        sum += i*i*i
    print('Summary of cubes ever numbers is from', n, 'to', sum)
    