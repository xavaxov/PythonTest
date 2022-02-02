import random

n = 15 # количество строк
m = 15 # количество столбцов

# n - no wall
# r - right wall
# d - down wall
# c - corner wall

a = [[random.choice(['n','r','d','c']) for j in range(m)] for i in range(n)]
b = [[0] * m for i in range(n)]
c = [[''] * m for i in range(n)]
path = []

start = [random.randint(0,n-1), random.randint(0,m-1)] 
finish = [random.randint(0,n-1), random.randint(0,m-1)]

c[start[0]][start[1]] = 'S'
c[finish[0]][finish[1]] = 'F'

def PrintArr(a, c):
    for i in range(len(a)): 
        for j in range(len(a[i])):
            if a[i][j] == 'n':
                print('   ', end='') if c[i][j] == '' else  print(' ' + c[i][j] +' ', end='')
            elif a[i][j] == 'r':
                print('  |', end='') if c[i][j] == '' else  print(' ' + c[i][j] +'|', end='')
            elif a[i][j] == 'd':
                print('___', end='') if c[i][j] == '' else  print('_' + c[i][j] +'_', end='')
            elif a[i][j] == 'c':
                print('__|', end='') if c[i][j] == '' else  print('_' + c[i][j] +'|', end='')
        print()

PrintArr(a, c)
print('-----')

d = 1
flag = 0
b[start[0]][start[1]] = d # помечаем стартовую ячейку

while b[finish[0]][finish[1]] == 0 and flag == 0:
    flag = 1
    for i in range(n): 
        for j in range(m):
            if b[i][j] == d:
                if i+1<n and a[i][j] != 'd' and a[i][j] != 'c' and b[i+1][j] == 0:
                        b[i+1][j] = d + 1 
                        flag = 0
                if i-1>-1 and a[i-1][j] != 'd' and a[i-1][j] != 'c' and b[i-1][j] == 0:
                        b[i-1][j] = d + 1
                        flag = 0
                if j+1<m and a[i][j] != 'r' and a[i][j] != 'c' and b[i][j+1] == 0:
                        b[i][j+1] = d + 1 
                        flag = 0
                if j-1>-1 and a[i][j-1] != 'r' and a[i][j-1] != 'c' and b[i][j-1] == 0:
                        b[i][j-1] = d + 1
                        flag = 0
    d = d + 1

for i in range(len(b)): 
        for j in range(len(b[i])):
            print(b[i][j], end=' ') if len(str(b[i][j])) == 2 else print(' ' + str(b[i][j]), end=' ')
        print()
print('-----')

if flag == 0:
    cur = finish
    while cur != start:
        x = cur[0]
        y = cur[1]
        path.append(cur)
        if x+1<n and x+1>-1 and b[x+1][y] == b[x][y] - 1:
            c[x][y] = '↓'
            x = x + 1
        elif x-1<n and x-1>-1 and b[x-1][y] == b[x][y] - 1:
            c[x][y] = '↑'
            x = x - 1
        elif y+1<m and y+1>-1 and b[x][y+1] == b[x][y] - 1:
            c[x][y] = '→'
            y = y + 1
        elif y-1<m and y-1>-1 and b[x][y-1] == b[x][y] - 1:
            c[x][y] = '←'
            y = y - 1
        cur = [x, y]   
    c[start[0]][start[1]] = 'F'
    c[finish[0]][finish[1]] = 'S'
    PrintArr(a, c)
else:
    print('no path') 