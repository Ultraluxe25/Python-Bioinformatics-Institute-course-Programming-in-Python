'''
Напишите программу, которая считывает с клавиатуры два числа a и b,
 считает и выводит на консоль среднее арифметическое всех чисел из отрезка 
[a;b], которые кратны числу 3

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3
Sample Input:
-5
12

Sample Output:
4.5
'''

a, b = int(input()), int(input())
total = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        total += i
        counter += 1
    
print(total / counter)