lines = 5
for j in range(1,lines+1):
    for i in range(1,lines+1):
        if (i<(lines+1) - j) or (i > lines+j-1):
            print(' ', end='')
        else:
            print('*', end=' ')
    print()
