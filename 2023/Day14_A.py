filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day14_InputData.txt"
filelines = open(filepath, '+r').readlines()
filelines.append('#'*len(filelines[0]))
filelines.insert(0, '#'*len(filelines[0]))
dishplane = [[i for i in v.strip('\n')] for v in filelines]
dishplane = [list(row) for row in zip(*dishplane)]

finalvalue:int = 0
for dishplaneline in dishplane:
    tags = {i for i, x in enumerate(dishplaneline) if x == '#'}
    tags = sorted(tags)
    for tagidx in range(len(tags)-1):
        group = dishplaneline[tags[tagidx]:tags[tagidx+1]]
        numofo = group.count('O')
        for i in range(tags[tagidx], tags[tagidx]+numofo):
            finalvalue += (len(dishplaneline) - (i+2))
print(finalvalue)

    

