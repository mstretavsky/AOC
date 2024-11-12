filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day2_InputData.txt"
filelines = open(filepath, "r").readlines()
finalvalue:int = 0
for filelineidx in range(0, len(filelines)):
    fileline = filelines[filelineidx]
    game:str = "Game {0}:".format(filelineidx+1)
    fileline = fileline.replace(game, "")
    for idx in range(12, 0, -1):
        phrase:str = str(idx) + " red"
        fileline = fileline.replace(phrase, "")
    for idx in range(13, 0, -1):
        phrase:str = str(idx) + " green"
        fileline = fileline.replace(phrase, "")
    for idx in range(14, 0, -1):
        phrase:str = str(idx) + " blue"
        fileline = fileline.replace(phrase, "")
    fileline = fileline.strip(';, \n')
    if fileline:
        continue
    finalvalue += (filelineidx + 1)
print(finalvalue)
input()