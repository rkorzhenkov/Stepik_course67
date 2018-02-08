"""Вывести последовательность так 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... -на вход дается длина массива"""


n = int(input())
m = []
for i in range(n):
    j = 0
    while j < i + 1:
        m.append(i + 1)
        j = j + 1
    if len(m) > n: 
        break
m = m[:n]
for i in m:
    print(i)