def program_1():
    # Unicode str
    S = u"Яa😂"
    print(S)
    print(type(S))

    # Byte str
    print(b'asd', type(b'asd'))
    # print(b"Я")


program_1()


def program_2():
    unicode_str = u"Яблоко is an apple..."
    byte_str = b"Apple is apple!"

    unicode_as_byte_str = unicode_str.encode()
    byte_str_as__unicode_str = byte_str.decode()

    print(len(unicode_str), unicode_str)
    print(len(unicode_as_byte_str), unicode_as_byte_str)
    print(len(byte_str), byte_str)
    print(len(byte_str_as__unicode_str), byte_str_as__unicode_str)


program_2()

print(u'\u044f')
