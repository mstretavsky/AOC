import math
from collections import defaultdict
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

def checkStarAtPos(searchedstring:str, pos:int):
    if pos < 0 or pos >= len(searchedstring):
        return False
    if searchedstring[pos] == '*':
        return True
    return False

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day3_InputData.txt"
filelines = open(filepath, "r").readlines()
filelines.insert(0, '.' * 140)
filelines.append('.' * 140)
starsnumbersmap = defaultdict(list)
for filelineidx in range(1, len(filelines)-1):
    fileline = filelines[filelineidx]
    fileline = fileline.strip('\n')
    strnumbers = extractNumbers(fileline)
    endpos:int = 0
    for strnumber in strnumbers:
        startpos = fileline.find(strnumber, endpos) - 1
        endpos = startpos + 1 + len(strnumber)
        for i in range(startpos, endpos + 1):
            if checkStarAtPos(filelines[filelineidx-1].strip('\n'), i):
                starsnumbersmap['{0},{1}'.format(filelineidx-1, i)].append(int(strnumber))
            elif checkStarAtPos(filelines[filelineidx+1].strip('\n'), i):
                starsnumbersmap['{0},{1}'.format(filelineidx+1, i)].append(int(strnumber))
            elif checkStarAtPos(fileline, i):
                starsnumbersmap['{0},{1}'.format(filelineidx, i)].append(int(strnumber))
finalvalue:int = 0
for starnumbers in starsnumbersmap.values():
    if len(starnumbers) > 1:
        finalvalue += math.prod(starnumbers)
print(finalvalue)
input()