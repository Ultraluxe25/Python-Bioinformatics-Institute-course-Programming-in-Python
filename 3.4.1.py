'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, 
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". 
Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. 
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, 
надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''

with open('dataset_3363_2.txt') as data_set:
    data = data_set.readline()
    message = []
# v9G4R19n11w8s11V15G14w12a17c15K1R14C15G14I19B18F19n11w13b13O13N2P8r2I19a7u2Y2i9A11V17E19C11K15S17X15N9

    for index, value in enumerate(data):
        if value.isalpha():
            char = value
            i = 1
            number = ''
            while data[index + i].isdigit():
                number += data[index + i]
                i += 1
            message.append(char * int(number))

    message = ''.join(message)
    print(message)


with open('response.txt', 'w') as decoded_message:
    decoded_message.write(message)
