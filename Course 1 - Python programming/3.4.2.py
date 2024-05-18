'''
Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) 
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''

with open('dataset_3363_3.txt', 'r') as file:
    matches = {}
    for line in file:
        line = line.split()
        for element in line:
            if element.lower() in matches:
                matches[element.lower()] += 1
            else:
                matches[element.lower()] = 1
    print(matches)
    max_key, max_value = '', 0
    for key, value in matches.items():
        if value > max_value:
            max_value = value
            max_key = key
    print(max_key, max_value)


with open('response_task2.txt', 'w') as file:
    print(max_key, max_value)
    