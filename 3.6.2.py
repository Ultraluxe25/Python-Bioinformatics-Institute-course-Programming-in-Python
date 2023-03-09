'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

'''
import requests

with open('dataset_3378_3.txt', 'r') as file:
    url = file.readline().strip()
    # here we found name for second file

# we save prime part of each link
storage = 'https://stepic.org/media/attachments/course67/3.6.3/'
info = ''

while info[:2] != 'We':
    # we find and open the file
    response = requests.get(url)
    content = response.text
    # link storage with title of the next file
    url = storage + content
    print(content)

# if we are here, then last printed content is the answer
result = requests.get(url)
print(result.text)
