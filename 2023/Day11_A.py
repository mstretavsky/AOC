filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day11_InputData.txt"
filelines = open(filepath, '+r').readlines()

_2d_list = [[v for v in filelines[i].strip('\n')] for i in range(len(filelines))]

#rotations
_2d_list = [list(row) for row in zip(*_2d_list)]

#insert empty lines
rowidx:int = 0
while rowidx < len(_2d_list):
    if all([True if v == '.' else False for v in _2d_list[rowidx]]):
        _2d_list.insert(rowidx, ['.']*len(_2d_list[rowidx]))
        rowidx += 2
        continue
    rowidx += 1

#rotations
_2d_list = [list(row) for row in zip(*_2d_list)]

#insert empty lines and calculate distances between points
points = []
rowidx = 0
while rowidx < len(_2d_list):
    if all([True if v == '.' else False for v in _2d_list[rowidx]]):
        _2d_list.insert(rowidx, ['.']*len(_2d_list[rowidx]))
        rowidx += 2
    else:
        for rowvalidx in range(len(_2d_list[rowidx])):
            if _2d_list[rowidx][rowvalidx] == '#':
                points.append((rowidx, rowvalidx))
        rowidx += 1

shortestdist:int = 0
numofpairs:int = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        dist = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
        print("Distance between points {0} and {1} is {2}".format(points[i], points[j], dist))
        shortestdist += dist
        numofpairs += 1
print(numofpairs)
print(shortestdist)