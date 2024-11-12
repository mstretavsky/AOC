from collections import defaultdict
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
nodes = networkmap.get('AAA')
finalvalue:int = 0
reachedzzz:bool = False
while not reachedzzz:
    for instruction in instructions:
        finalvalue += 1
        if nodes[int(instruction)] == 'ZZZ':
            reachedzzz = True
            break
        nodes = networkmap.get(nodes[int(instruction)])
print(finalvalue)
input()
