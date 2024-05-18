'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на 
d строках указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''

d = int(input())
dictionary = []
for _ in range(d):
    dictionary.append(input().lower())
# print(dictionary)
l = int(input())
incorrect_words = set()
for _ in range(l):
    phrase = input().split()
    # print(phrase)
    for word in phrase:
        if word.lower() not in dictionary:
            incorrect_words.add(word.lower())

for no_name in incorrect_words:
    print(no_name)
    