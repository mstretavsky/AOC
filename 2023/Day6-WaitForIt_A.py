testingdata = [(7,9), (15,40), (30,200)]
realdata = [(61, 643), (70, 1184), (90, 1362), (66, 1041)]
finalvalue:int = 1
for oneinput in realdata:
    numofways:int = 0
    for i in range(1, oneinput[0]):
        if oneinput[1]/i <= (oneinput[0] - i):
            numofways += 1
    finalvalue *= numofways

print(finalvalue)
input()