# создаем файл в директории doc. а- специальный мод
from asyncore import write


# fw = open("doc/file.txt", "a")
# fw.write("hello world\n")  # записываем file.txt строку hello world
# fw.write("hi, serg\n")
# fw.close()
# a- запись новых данных в файл и помещение их в конец файла
# w- запись новых данных, но с удалением старых данных
var = input("Напиши что-нибудь: ")
fw = open("doc/file_1.txt", "a")
fw.write(var)
fw.close(var)
