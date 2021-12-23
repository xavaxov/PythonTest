import random

n = 15 # количество строк
m = 15 # количество столбцов

a = [[random.choice([0,0,0,0,0,'■']) for j in range(m)] for i in range(n)]
b = [['.'] * m for i in range(n)]
for i in range(n): 
    for j in range(m):
        if a[i][j] == '■':
            b[i][j] = '■'
# a = [[0] * m for i in range(n)]
# b = [['.'] * m for i in range(n)]
start = [random.randint(0,n-1), random.randint(0,m-1)] 
finish = [random.randint(0,n-1), random.randint(0,m-1)]
# rocks = [[1, 2],[1, 4],[1, 5],[2, 1],[3,3]]
path = []


def PrintArr(arr): # функция вывода массива
    for i in range(len(arr)): 
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ') if len(str(arr[i][j])) == 2 else print(' ' + str(arr[i][j]), end=' ')
        print()

d = 1
flag = 0
a[start[0]][start[1]] = d # помечаем стартоввую ячейку
a[finish[0]][finish[1]] = 0

# def RocksArr(a, rocks):
#    for i in range(len(rocks)):
#        a[rocks[i][0]][rocks[i][1]] = '@'
# RocksArr(a, rocks)
# RocksArr(b, rocks)

b[start[0]][start[1]] = 'S'
b[finish[0]][finish[1]] = 'F'
# PrintArr(b)
# print('------')

while a[finish[0]][finish[1]] == 0 and flag == 0:
    flag = 1
    for i in range(n): 
        for j in range(m):
            if a[i][j] == d:
                if i+1<n and i+1>-1:
                    if a[i+1][j] == 0:
                        a[i+1][j] = d + 1 
                        flag = 0
                if i-1<n and i-1>-1:
                    if a[i-1][j] == 0:
                        a[i-1][j] = d + 1
                        flag = 0
                if j+1<m and j+1>-1:
                    if a[i][j+1] == 0:
                        a[i][j+1] = d + 1 
                        flag = 0
                if j-1<m and j-1>-1:
                    if a[i][j-1] == 0:
                        a[i][j-1] = d + 1
                        flag = 0
    d = d + 1


# PrintArr(a)
# print('------')

if flag == 0:
    cur = finish
    start
    while cur != start:
        x = cur[0]
        y = cur[1]
        path.append(cur)
        if x+1<n and x+1>-1 and a[x+1][y] == a[x][y] - 1:
            b[x][y] = '↓'
            x = x + 1
        elif x-1<n and x-1>-1 and a[x-1][y] == a[x][y] - 1:
            b[x][y] = '↑'
            x = x - 1
        elif y+1<m and y+1>-1 and a[x][y+1] == a[x][y] - 1:
            b[x][y] = '→'
            y = y + 1
        elif y-1<m and y-1>-1 and a[x][y-1] == a[x][y] - 1:
            b[x][y] = '←'
            y = y - 1
        cur = [x, y]    
    b[start[0]][start[1]] = 'F'
    b[finish[0]][finish[1]] = 'S'
    PrintArr(b)
    print('------')
    print(path)
else:
    PrintArr(b)
    print('------')
    print('no path') 

