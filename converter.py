import re


def readSMCFile(ruta_archivo):
    """
    Lee un archivo SMC y extrae la información de orientación y los valores del dataframe
    Keyword arguments:
    ruta_archivo -- ruta del archivo con formato smc
    """
    f = open(ruta_archivo, "r")
    lines = f.readlines()

    Orientation = getOrientationData(lines)
    data = getData(lines)
    f.close()

    return {"orientation": Orientation, "data": data}

def getOrientationData(lines):

    orientation = ""
    orientation_data = lines[12]
    orientation_data = re.sub(' +', ' ', orientation_data).strip().split(" ")
    vOrientation = orientation_data[4]
    hOrientation = orientation_data[5]
    if (vOrientation == "90" and hOrientation == "360"):
        orientation = "X"
    elif (vOrientation == "0" and hOrientation == "-32768"):
        orientation = "Y"
    elif (vOrientation == "0"):
        orientation = "Z"
    return orientation

def getData(lines):
    datalines = lines[36:]
    data = []
    for line in datalines:
        line_fixed = re.sub('(?<=E[-+]\d)', ' ', line)
        line_stripped = re.sub(' +', ' ', line_fixed).strip().split(" ")
        for number in line_stripped:
            data.append(float(number))
    return data


result = readSMCFile("archivos_smc\OTAV.HN1.IU.20_a.smc")

print(result.get("orientation"))
print(result.get("data"))


