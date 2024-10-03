"""
n = int(input())
sum = 0
if n>100:
    print("Error! Input the correct numbers!")
else:
    for i in range(n+1):
        sum += i*i*i
    print(f'The sum of cubes of all natural nubers up to {n} is {sum}')
    print()

print('The table of multiplication')
for i in range(1, 10):
    for k in range(1, 10):
        if (k*i)/10>=1:
            print(k*i, end=' ')
        else:
            print(k*i, end='  ')
    print()
"""
print('The uncommon table of multiplication')
for i in range(1, 10):
    for k in range(1, 10):
        print((10-k)*i, end=' ')
    else:
        print((10-k)*i, end='  ')
print()