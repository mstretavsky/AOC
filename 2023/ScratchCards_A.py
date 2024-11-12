import filecmp
from pathlib import Path

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\ScratchCards_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
for fileline in filelines:
    fileline = fileline[fileline.find(":")+1:]
    fileline = fileline.strip('\n')
    fileline += ' '
    cardsides = fileline.split('|')
    numofmatches:int = 0
    for i in cardsides[0].strip().split(' '):
        i.strip()
        if not i:
            continue
        numtofind = " {0} ".format(i)
        if cardsides[1].find(numtofind) != -1:
            numofmatches += 1
    if numofmatches > 0:
        numofmatches -= 1
        finalvalue += 1 * (2**numofmatches)
    
print(finalvalue)
input()