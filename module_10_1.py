from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name): # создание функции с аргументами: количество записываемых слов и название файла, куда будут записываться слова
    for i in range(1, word_count + 1): # цикл по количеству слов
        with open(file_name, 'a', encoding='utf-8') as file: # открытие файла с добавлением в него нового содержимого ('a'
            file.write(f'Какое-то слово № {i}\n') # запись в файл фразы "Какое-то слово № (от 1 до word_count +1)" раз
            sleep(0.1) # задержка
    file.close() #закрытие файла
    print(f'Завершлась запись в файл {file_name}') # вывод сообщения

time_start1 = datetime.now() # переменная - время начала работы программы
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end1 = datetime.now() # переменная - время окончания работы программы
time_res1 = time_end1 - time_start1 # переменная - время работы программы
print('Работа потоков:',  time_res1)

time_start2 = datetime.now() # переменная - время начала работы программы
first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30,'example6.txt'))
third = Thread(target=write_words, args=(200,'example7.txt'))
fourth = Thread(target=write_words, args=(100, 'example8.txt'))
first.start() # запуск потока первого
second.start() # запуск потока второго
third.start() # запуск потока третьего
fourth.start() # запуск потока
first.join() # остановка потока первого
second.join() # остановка потока второго
third.join() # остановка потока третьего
fourth.join() # остановка потока четвертого
time_end2 = datetime.now() # переменная - время окончания работы программы
time_res2 = time_end2 - time_start2 # переменная - время работы программы
print('Работа потоков: ', time_res2)
