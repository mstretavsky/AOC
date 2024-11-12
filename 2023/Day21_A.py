filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day21_InputData.txt"
filelines = open(filepath, '+r').readlines()
gardenplots = set()
garden = [[char for char in line.strip('\n')] for line in filelines]
garden.insert(0, ['-'] * len(garden[0]))
garden.append(['-'] * len(garden[len(garden) - 1]))
for i in range(len(garden)):
    garden[i].insert(0, '-')
    garden[i].append('-')
    if garden[i].count('S') > 0:
        gardenplots.add((i, garden[i].index('S')))
        garden[i][garden[i].index('S')] = '.'

for i in range(64):
    tempgardenplots = gardenplots.copy()
    gardenplots.clear()
    for gardenplot in tempgardenplots:
        if (garden[gardenplot[0] + 1][gardenplot[1]] == '#' or garden[gardenplot[0] + 1][gardenplot[1]] == '-') and \
        (garden[gardenplot[0] - 1][gardenplot[1]] == '#' or garden[gardenplot[0] - 1][gardenplot[1]] == '-') and \
        (garden[gardenplot[0]][gardenplot[1] + 1] == '#' or garden[gardenplot[0]][gardenplot[1] + 1] == '-') and \
        (garden[gardenplot[0]][gardenplot[1] - 1] == '#' or garden[gardenplot[0]][gardenplot[1] - 1] == '-'):
            gardenplots.add(gardenplot)
            continue
        if garden[gardenplot[0] + 1][gardenplot[1]] == '.':
            gardenplots.add((gardenplot[0] + 1, gardenplot[1]))
        if garden[gardenplot[0] - 1][gardenplot[1]] == '.':
            gardenplots.add((gardenplot[0] - 1, gardenplot[1]))
        if garden[gardenplot[0]][gardenplot[1] + 1] == '.':
            gardenplots.add((gardenplot[0], gardenplot[1] + 1))
        if garden[gardenplot[0]][gardenplot[1] - 1] == '.':
            gardenplots.add((gardenplot[0], gardenplot[1] - 1))
print(len(gardenplots))