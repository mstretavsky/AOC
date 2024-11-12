filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day1_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
for fileline in filelines:
    linedigits:str = ''
    for filelinechar in fileline:
        if(filelinechar.isdigit()):
            linedigits += filelinechar
    finalvalue += (int(linedigits[0])*10 + int(linedigits[len(linedigits)-1])*1)
print(finalvalue)
input()
