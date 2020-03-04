with open("simple_text.txt", 'r') as fr:
    print(fr.read())

print(fr.name)
print(fr.mode)

with open("simple_text.txt", 'r') as fr:
    line = fr.readline()
    print(line, end="")
    line = fr.readline()
    print(line, end="")
    line = fr.readline()
    print(line, end="")
    line = fr.readline()
    print("Length of last read is {}".format(len(line)))
    print(line, end="")

print("+++++Loop through all the line i n file++++")
with open("simple_text.txt", "r") as fr:
    for line in fr:
        print(line, end="")

print("++ print lines in file as a list+++")
with open("simple_text.txt", "r") as fr:
    lines = fr.readlines()
    print(lines)

print("+++++++ Read only specified number of character from file +++++")
with open("simple_text.txt", "r") as fr:
    first_twenty = fr.read(20)
    print(first_twenty, end="")
    second_twenty = fr.read(20)
    print(second_twenty)
    print(fr.tell())

print("++++++++ write to  a file +++++++++++")
with open("simple_text.txt", "r+") as fd:
    print(fd.read())
    fd.seek(0)
    fd.write("Hello, Extra text is added!!!")
    print(fd.read())


with open("simple_text_sec.txt", "w") as fw:
    with open("simple_text.txt", "r") as fr:
        for line in fr:
            fw.write(line)

print("============ Second file ============")
with open("simple_text_sec.txt", "r") as fr:
    print(fr.read())

with open("simple_text_sec.txt", "r") as fr:
    with open("simple_text_thrid.txt", "w") as fd:
        for line in fr:
            fd.write(line)

print(" ++++File 3 contents++++")
with open("simple_text_thrid.txt", "r") as fr:
    for line in fr:
        print(line, end="")
    fr.seek(0)
    print("Reprinting !!!!")
    print(fr.readlines())

print("++++++++++ Binary file+++++++++++")
with open("RCB.jpg", "rb") as fr:
    with open("RCB_sec.jpg", "wb") as fw:
        for line in fr:
            fw.write(line)


listfile = []
with open("RCB.jpg", "rb") as fr:
    listfile = fr.readlines()

print(listfile)

with open("RCB_three.jpg", "wb") as fw:
    for line in listfile:
        fw.write(line)

    print("___________________________")
    print(dir(fw))

with open("RCB4.jpg", "wb") as fw:
    fw.writelines(listfile)

