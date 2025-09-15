def meow(string):
    peow = ""
    for asd in string:
        peow += "chr(" + str(ord(asd)) + ")+"
    print(peow[:-1])

meow("/flag.txt")
