filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day10_InputData.txt"
filelines = open(filepath, '+r').readlines()

startPos = ()
for filelineidx in range(len(filelines)):
    startPos = (filelineidx, filelines[filelineidx].find('S'))
    if startPos[1] != -1:
        break

stepsrecorder = []
stepsrecorder.append(startPos)
targetPos = (startPos[0]+1, startPos[1])
while targetPos != startPos:
    dirsymbols = filelines[targetPos[0]][targetPos[1]]
    previousPos = targetPos
    if dirsymbols == '|':
        if stepsrecorder[-1][0] < targetPos[0]:
            targetPos =  targetPos[0] + 1, targetPos[1]
        else:
            targetPos =  targetPos[0] - 1, targetPos[1]
    elif dirsymbols == '-':
        if stepsrecorder[-1][1] < targetPos[1]:
            targetPos =  targetPos[0], targetPos[1] + 1
        else:
            targetPos =  targetPos[0], targetPos[1] - 1
    elif dirsymbols == 'J':
        if stepsrecorder[-1][1] < targetPos[1]:
            targetPos = targetPos[0] - 1, targetPos[1]
        else:
            targetPos = targetPos[0], targetPos[1] - 1
    elif dirsymbols == 'L':
        if stepsrecorder[-1][1] > targetPos[1]:
            targetPos =  targetPos[0] - 1, targetPos[1]
        else:
            targetPos =  targetPos[0], targetPos[1] + 1
    elif dirsymbols == 'F':
        if stepsrecorder[-1][1] > targetPos[1]:
            targetPos =  targetPos[0] + 1, targetPos[1]
        else:
            targetPos =  targetPos[0], targetPos[1] + 1
    elif dirsymbols == '7':
        if stepsrecorder[-1][1] < targetPos[1]:
            targetPos =  targetPos[0] + 1, targetPos[1]
        else:
            targetPos =  targetPos[0], targetPos[1] - 1
    if targetPos[0] < 0 or targetPos[0] >= (len(filelines)) or targetPos[1] < 0 or targetPos[1] >= len(filelines[0]):
        print("out of range position") 
        input()
    stepsrecorder.append(previousPos)

print(len(stepsrecorder) / 2)

"Part II"
print(abs(sum([stepsrecorder[idx][0] * stepsrecorder[idx+1][1]-stepsrecorder[idx][1] * stepsrecorder[idx+1][0] for idx in range(len(stepsrecorder)-1)]))/2)