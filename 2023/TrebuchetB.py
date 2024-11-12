def replaceWordsNumber(line:str):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day1_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
for fileline in filelines:
    fileline = replaceWordsNumber(fileline)
    linedigits:str = ''
    for filelinechar in fileline:
        if(filelinechar.isdigit()):
            linedigits += filelinechar
    finalvalue += (int(linedigits[0])*10 + int(linedigits[len(linedigits)-1])*1)
print(finalvalue)
input()
