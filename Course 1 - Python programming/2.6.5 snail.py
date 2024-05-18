'''
Выведите таблицу размером n×n, заполненную числами от 1 до n в квадрате по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке.

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

dimension = int(input())
table = [[0] * dimension for line in range(dimension)]

# build first line
for i in range(dimension):
    table[0][i] = i + 1

start = dimension + 1
end = int(dimension ** 2)
index = 0

# print(start)
# print(end)

# create borders
x, y = 0, dimension - 1

# fulfill lines in four directions
while start <= end:
    # to the down
    for i in range(x + 1, y + 1):
        if start > end:
            break
        else:
            table[i][y] = start
            start += 1

    # to the left
    for i in range(y - 1, x - 1, -1):
        if start > end:
            break
        else:
            table[y][i] = start
            start += 1

    # to the up
    for i in range(y - 1, x, -1):
        if start > end:
            break
        else:
            table[i][x] = start
            start += 1

    # to the right
    for i in range(x + 1, y):
        if start > end:
            break
        else:
            table[x + 1][i] = start
            start += 1

    x += 1
    y -= 1
    
# output answer in correct form
for line in table:
    print(*line)
