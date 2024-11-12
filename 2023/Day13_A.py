def GetMirroredLines(mirrors:[]):
    for i in range(1, len(mirrors)):
        abovemirror = mirrors[:i][::-1]
        bellowmirror = mirrors[i:]

        abovemirror = abovemirror[:len(bellowmirror)]
        bellowmirror = bellowmirror[:len(abovemirror)]

        if abovemirror == bellowmirror:
            return i
    return 0
def oposite(symbol:str):
    if symbol == '#':
        return '.'
    return '#'
def GetMirroredLines2(mirrors:[]):
    anothermirroredlines = []
    for j in [0, len(mirrors)-1]:
        for k in range(len(mirrors[j])):
            mirrors_copy = mirrors[:]
            mirrors_copy[j][k] =  oposite(mirrors_copy[j][k])
            anothermirroredlines.append(GetMirroredLines(mirrors_copy))        
    return anothermirroredlines
            
    

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day13_InputData.txt"
filelines = open(filepath, '+r').readlines()
filelines.append('')
filelines = [v.strip('\n') for v in filelines]

finalvalue = 0
mirrors = []
for fileline in filelines:
    if fileline:
        mirrors.append(fileline)
    else:
        mirrors = [[i for i in mirrors[v]] for v in range(len(mirrors))]
        mirroredrows = GetMirroredLines2(mirrors)
        finalvalue += 100*mirroredrows
        
        mirrors = [list(row) for row in zip(*mirrors)]
        
        mirroredcolumns = GetMirroredLines2(mirrors)
        finalvalue += mirroredcolumns
        mirrors.clear()
print(finalvalue)