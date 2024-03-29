'''
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа x программа должна на отдельной строке вывести значение f(x). 
Функция f(x) уже реализована и доступна для вызова. 

Функция вычисляется достаточно долго и зависит только от переданного аргумента x. 
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12

Sample Output:
11
41
47
61
41
'''

output = dict()
arg = int(input())
for i in range(arg):
    x = int(input())
# если такого ключа не было, то добавим
    if x not in output.keys():
        output[x] = f(x)
# если был, то и значение уже известно
    print(output[x])
    