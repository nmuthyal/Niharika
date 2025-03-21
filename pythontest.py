def diamond(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1,n+1):
        for j in range(n-i):
            print('',end=' ')
        for k in range(i):
            print(alphabet[k],end=' ')
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print('',end=' ')
        for k in range(i):
            print(alphabet[k],end=' ')
        print()

n = int(input('Enter the size '))
diamond(n)