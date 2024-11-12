from collections import defaultdict
import math
filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day8_InputData.txt"
filelines = open(filepath, '+r').readlines()
networkmap = defaultdict(list)
for fileline in filelines:
    fileline = fileline.strip('\n')
    splitsbyequal = fileline.split(' = ')
    splitsbycomma = splitsbyequal[1].strip('()').split(', ')
    networkmap[splitsbyequal[0]] = [splitsbycomma[0], splitsbycomma[1]]
instructions:str = 'LRRLRRRLLRRRLRRRLLRRLRRRLRRLRRLRLRLRLRLRLLRRRLRRLRLRRRLRRRLRLRRRLRLRRLRRRLRRRLRLLRRRLRLLLRLRRRLRLRRLRRLLLLRRLRRLRLRLRRLRLRRLRRRLRRRLRLRLRRLLLLRRLRLRRLLRRRLRLRLRLRRRLRLLLRLRLRRRLRLRRRLRRRLRRRLLRRLRRRLRRRLRRRLRRRLRLLRRRLRLRRRLRLRLRRRLRRLRRLLRRRLRRRLRRRLRLRLRLRRLRRRLRRLRLRLRLRRRR'
instructions = instructions.replace('L', '0')
instructions = instructions.replace('R', '1')
nodeslist = [networkmap.get('MCA'), networkmap.get('AAA'), networkmap.get('DCA'), networkmap.get('LGA'), networkmap.get('NLA'), networkmap.get('VPA')]
numofstepslist = []
for nodes in nodeslist:
    numofsteps:int = 0
    reachedzzz:bool = False
    while not reachedzzz:
        for instruction in instructions:
            numofsteps += 1
            if nodes[int(instruction)].endswith('Z'):
                reachedzzz = True
                break
            nodes = networkmap.get(nodes[int(instruction)])
    numofstepslist.append(numofsteps)

print(math.lcm(numofstepslist[0], numofstepslist[1], numofstepslist[2], numofstepslist[3], numofstepslist[4], numofstepslist[5]))
input()