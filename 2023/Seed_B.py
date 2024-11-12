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

seedranges = [[seeds[seedidx], seeds[seedidx] + seeds[seedidx+1]] for seedidx in range(len(seeds)-1)]
lowestlocation:int = sys.maxsize
for seedrange in seedranges:
        evolvedseedranges = []
        evolvedseedranges.append(seedrange)
        for i in range(7):
            anotherseedranges = []
            for evolvedseedrange in evolvedseedranges:
                for j in inputmaps[i]:
                    if (evolvedseedrange[0] >= j[0] and evolvedseedrange[0] <= j[1]) and (evolvedseedrange[1] >= j[0] and evolvedseedrange[1] <= j[1]):
                        anotherseedranges.append([j[2] + (evolvedseedrange[0] - j[0]), j[2] + (evolvedseedrange[1] - j[0])])
                        break
                    if evolvedseedrange[0] >= j[0] and evolvedseedrange[0] <= j[1]:
                        anotherseedranges.append([j[2] + (evolvedseedrange[0] - j[0]), j[2] + (j[1] - j[0])])
                        continue
                    if evolvedseedrange[1] >= j[0] and evolvedseedrange[1] <= j[1]:
                        anotherseedranges.append([j[2], j[2] + (evolvedseedrange[1] - j[0])])
                        continue
            evolvedseedranges = anotherseedranges
        minvalue = min(min(v) for v in evolvedseedranges)
        if lowestlocation > minvalue:
            lowestlocation = minvalue
    
print(lowestlocation)
input()
