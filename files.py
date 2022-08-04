# создаем файл в директории doc. а- специальный мод
fw = open("doc/file.txt", "a")
fw.write("hello world\n")  # записываем file.txt строку hello world
fw.write("hi, serg\n")
fw.close()
