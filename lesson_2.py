"""
a = int(input())
b=int(input())
if b!=0 and a!=0:
    c=a/b
    print(c)
else:
    print('Error!')

a=int(input())
if a>20:
    b=(a/10)*3.5
    print(a)
    print(round(b, 2))
else:
    print('No discount')
    """
a=int(input())
if a==1:
    print('January', 'Winter')
elif a==2:
    print('February', 'Winter')
elif a==3:
    print('March', 'Spring')
elif a==4:
    print('April', 'Spring')
elif a==5:
    print('May', 'Spring')
elif a==6:
    print('June', 'Summer')
elif a==7:
    print('Jule', 'Summer')
elif a==8:
    print('August', 'Summer')
else:
    print('Error! This number is incorrect!')