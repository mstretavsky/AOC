def extractNumbers(searchedString:str):
    numbersinstring = []
    number:str = ''
    for i in searchedString:
        if i.isdigit():
            number += i
        else:
            if number:
                numbersinstring.append(number)
                number = ''
    if number:
        numbersinstring.append(number)
    return numbersinstring

def checkSymbolAtPos(searchedstring:str, pos:int):
    if pos < 0 or pos >= len(searchedstring):
        return False
    if searchedstring[pos] != '.' and not searchedstring[pos].isdigit():
        return True
    return False

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day3_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
filelines.insert(0, '.' * 140)
filelines.append('.' * 140)
for filelineidx in range(1, len(filelines)-1):
    fileline = filelines[filelineidx]
    fileline = fileline.strip('\n')
    strnumbers = extractNumbers(fileline)
    endpos:int = 0
    for strnumber in strnumbers:
        startpos = fileline.find(strnumber, endpos) - 1
        endpos = startpos + 1 + len(strnumber)
        for i in range(startpos, endpos + 1):
            if checkSymbolAtPos(filelines[filelineidx-1].strip('\n'), i) or checkSymbolAtPos(filelines[filelineidx+1].strip('\n'), i) or checkSymbolAtPos(fileline, i):
                finalvalue += int(strnumber)
                break
print(finalvalue)
input()