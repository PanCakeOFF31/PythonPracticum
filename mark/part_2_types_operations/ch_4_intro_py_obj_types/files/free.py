from helpers import print_section


def program_1():
    file_write = open('free.txt', 'w')
    file_write.write('some text\nsome text\nsome text again')
    file_write.close()

    file_read = open('free.txt', 'r')
    file_read.seek(3)
    read = file_read.read()
    print(read)
    file_read.close()


print_section("Выполнить запись данных в файл")
program_1()


def program_2():
    file_write = open('free.txt', 'w')

    text = """This creates a file in the
current directory and writes text
to it (the filename can be a full
directory path if you need to
access a file elsewhere on your
computer). To read back what you just wro"""

    file_write.write(text)
    file_write.close()

    for line in open('free.txt'):
        print(line.rstrip())


print_section("Чтение файла по строкам")
program_2()
