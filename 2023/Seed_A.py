import sys

filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Seed_InputData.txt"
filelines = open(filepath, "r").readlines()
filelines[0] = filelines[0].replace("seeds: ", '')
seeds = filelines[0].split(' ')
seeds = [int(i) for i in seeds]
inputmaps = []
inputmapsidx = -1
inputmap = []
for i in range(1, len(filelines)):
    filelines[i] = filelines[i].strip('\n')
    if not filelines[i]:
        if len(inputmap) > 0:
            inputmaps.append(inputmap)
            inputmap = []
        continue
    if filelines[i].find('map:') != -1:
        inputmapsidx += 1
        continue
    inputmapsnumbers = filelines[i].split(' ')
    inputmapsnumbers = [int(j) for j in inputmapsnumbers]
    inputmap.append([inputmapsnumbers[1], inputmapsnumbers[1]+inputmapsnumbers[2], inputmapsnumbers[0]])

lowestlocation:int = sys.maxsize
for seed in seeds:
    for i in range(7):
        for j in inputmaps[i]:
            if seed >= j[0] and seed <= j[1]:
                seed = j[2] + (seed - j[0])
                break
    if lowestlocation > seed:
        lowestlocation = seed
print(lowestlocation)
