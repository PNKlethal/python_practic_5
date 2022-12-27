#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
import codecs

try:
    with codecs.open("text_4.txt") as read_file:
        with open("text_4res.txt", "w", encoding= "utf-8") as write_file:
            number_words_list = ["Один", "Два", "Три", "Четыре"]
            all_read_lines = read_file.readlines()
            for num, line in enumerate(all_read_lines):
                if len(line):
                    words = line.split()
                    print(f"{number_words_list[num]} {words[1]} {words[2]}",
                          file=write_file)
            print("\tГотово\n")
except IOError:
    print("\tОшибка открытия файла!\n")