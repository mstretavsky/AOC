filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day2_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
for filelineidx in range(0, len(filelines)):
    fileline = filelines[filelineidx]
    game:str = "Game {0}:".format(filelineidx+1)
    fileline = fileline.replace(game, "")
    fileline = fileline.replace(";", ",")
    words = fileline.split(',')
    highestRed = 0
    highestBlue = 0
    highestGreen = 0
    for word in words:
        word = word.strip(" \n")
        if(word.find("red") != -1 and int(word.split(' ')[0]) > highestRed):
            highestRed = int(word.split(' ')[0])
            continue
        if(word.find("green") != -1 and int(word.split(' ')[0]) > highestGreen):
            highestGreen = int(word.split(' ')[0])
            continue
        if(word.find("blue") != -1 and int(word.split(' ')[0]) > highestBlue):
            highestBlue = int(word.split(' ')[0])
            continue
    finalvalue += (highestRed * highestGreen * highestBlue)
print(finalvalue)
input()