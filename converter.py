import re


def readfile():
    f = open("archivos_smc\OTAV.HN1.IU.20_a.smc", "r")
    lines = f.readlines()
    orientation_data = lines[12]
    orientation_data = re.sub(' +', ' ', orientation_data).strip().split(" ")
    vOrientation = orientation_data[4]
    hOrientation = orientation_data[5]

    print(vOrientation)
    print(hOrientation)

    datalines = lines[37:]
    data = []
    for line in datalines:
        line_stripped = re.sub(' +', ' ', line).strip().split(" ")
        data = data + line_stripped

    print(data)


readfile()
