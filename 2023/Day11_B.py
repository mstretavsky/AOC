def GetCrossedExpandedLines(pointA:(), pointB:(), insertedrow:[], insertedcolumns:[]):
    crossedexpandedlines:int = 0
    rowrange = [pointA[0], pointB[0]]
    columnrange = [pointA[1], pointB[1]]
    rowrange.sort()
    columnrange.sort()
    for v in range(rowrange[0], rowrange[1]):
        if any(True for i in insertedrow if i == v):
            crossedexpandedlines += 1
    for v in range(columnrange[0], columnrange[1]):
        if any(True for i in insertedcolumns if i == v):
            crossedexpandedlines += 1
    return crossedexpandedlines

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day11_InputData.txt"
filelines = open(filepath, '+r').readlines()

_2d_list = [[v for v in filelines[i].strip('\n')] for i in range(len(filelines))]
#rotation
_2d_list = [list(row) for row in zip(*_2d_list)]

insertemptycolumn = []
for rowidx in range(len(_2d_list)):
    if all([True if v == '.' else False for v in _2d_list[rowidx]]):
        insertemptycolumn.append(rowidx)

#rotation
_2d_list = [list(row) for row in zip(*_2d_list)]
points = []
insertemptyrow = []
for rowidx in range(len(_2d_list)):
    if all([True if v == '.' else False for v in _2d_list[rowidx]]):
        insertemptyrow.append(rowidx)
    else:
        for columnidx in range(len(_2d_list[rowidx])):
            if _2d_list[rowidx][columnidx] == '#':
                points.append((rowidx, columnidx))

shortestdist:int = 0
numofpairs:int = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        numcrossedexpanedlines = GetCrossedExpandedLines(points[i], points[j], insertemptyrow, insertemptycolumn)
        #print("Number of crossed empty lines between point {0} and {1} is {2}".format(points[i], points[j], numcrossedexpanedlines))
        shortestdist += (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])) + numcrossedexpanedlines * 999999
print(shortestdist)