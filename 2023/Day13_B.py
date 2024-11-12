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
def GetMirroredLines2(mirrors:[], originmirroredlines:int):
    anothermirroredlines = 0
    for j in [0, len(mirrors)-1]:
        for k in range(len(mirrors[j])):
            mirrors[j][k] =  oposite(mirrors[j][k])
            anothermirroredlines = GetMirroredLines(mirrors)
            mirrors[j][k] =  oposite(mirrors[j][k])
            if anothermirroredlines > 0 and anothermirroredlines != originmirroredlines:
                return anothermirroredlines
    return 0
            
    

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
        numrows = GetMirroredLines(mirrors)
        numrows2 = GetMirroredLines2(mirrors, numrows)

        mirrors = [list(row) for row in zip(*mirrors)]
        
        numcolumns = GetMirroredLines(mirrors)
        numcolumns2 = GetMirroredLines2(mirrors, numcolumns)

        if numrows2 != 0 and numrows2 != numrows and numrows2 != numcolumns:
            finalvalue += numrows2*100
        elif numcolumns2 != 0 and numcolumns2 != numcolumns and numcolumns2 != numrows:
            finalvalue += numrows2
        else:
            finalvalue += numrows*100
            finalvalue += numcolumns
        mirrors.clear()
print(finalvalue)