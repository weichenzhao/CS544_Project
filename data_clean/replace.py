filein =open('title.txt', 'rb')
fileout =open('title_total.txt', 'wb')

"""
    fix some small problems about the encoding in the dataset
"""
for line in filein:
    data = line.decode("utf8")
    data.replace(u'\xc2\xa0', "\n")
    #line.replace(u'\xc2', "\n")
    list_t = data.split()
    for elem in list_t:
        fileout.write(elem.encode("utf8") + "\n")
