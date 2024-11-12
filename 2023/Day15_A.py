filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day15_InputData.txt"
filelines = open(filepath, '+r').readlines()
data = filelines[0].split(',')

def calculatechar(char:str, initvalue:int):
    return ((ord(char) + initvalue)*17)%256

finalvalue:int = 0
for v in data:
    sequencevalue:int = 0
    for j in v:
        sequencevalue = calculatechar(j, sequencevalue)
    finalvalue += sequencevalue

print(finalvalue)

