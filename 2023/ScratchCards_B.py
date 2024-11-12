filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\ScratchCards_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
numofmatchesdict = {}
for filelineidx in range(len(filelines)):
    fileline = filelines[filelineidx]
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
    numofmatchesdict[filelineidx + 1] = [numofmatches, 1]

finalvalue:int = 0;
for key in list(numofmatchesdict):
    for j in range(numofmatchesdict[key][1]):
        for i in range(1, numofmatchesdict[key][0]+1):
            numofmatchesdict[key+i][1] += 1
    finalvalue += numofmatchesdict[key][1]

print(finalvalue)
input()