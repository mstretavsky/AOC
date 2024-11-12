filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day15_InputData.txt"
filelines = open(filepath, '+r').readlines()
data = filelines[0].split(',')

def calculatechar(char:str, initvalue:int):
    return ((ord(char) + initvalue)*17)%256
def updateindexes(listoflists:[[]]):
    maplabeltoindex = {}
    for i in range(len(listoflists)):
        for j in range(len(listoflists[i])):
            delimeteridx = listoflists[i][j].index('=')
            label = listoflists[i][j][:delimeteridx]
            maplabeltoindex[label] = j
    return maplabeltoindex

indexesinboxlist = {}
boxes = [[] for i in range(256)]
for v in data:
    delimeteridx = [idx for idx in range(len(v)) if v[idx] == '-' or v[idx] == '='][0]
    labelvalue = 0
    for i in range(delimeteridx):
        labelvalue = calculatechar(v[i], labelvalue)

    label = v[:delimeteridx]
    operation = v[delimeteridx:]
    index = indexesinboxlist.get(label)
    if operation[0] == '-':
        if index != None:
            box = boxes[labelvalue]
            box.remove(box[index])
            indexesinboxlist = updateindexes(boxes)
    else:
        if index != None:
            boxes[labelvalue][index] = v
        else:
            boxes[labelvalue].append(v)
            indexesinboxlist[label] = len(boxes[labelvalue])-1 
finalvalue:int = 0
for i in range(len(boxes)):
    for v in range(len(boxes[i])):
        focallenght = int(boxes[i][v][boxes[i][v].index('=')+1:])
        finalvalue += ((i+1) * (v+1) * focallenght)
print(finalvalue)