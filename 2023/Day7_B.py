from functools import cmp_to_key
def GetTypeOfCards(cards:str):
    cardsmap = {}
    for v in cards:
        if v == 'J':
            continue
        cardsmap[v] = cards.count(v)
    if len(cardsmap) == 0:
        cardsmap[2] = 5
    else:
        maxvaluekey = max(cardsmap, key=cardsmap.get)
        cardsmap[maxvaluekey] = cards.count(maxvaluekey) + cards.count('J')
    if len(cardsmap) == 1:
        return 7
    elif any([True for i, j in cardsmap.items() if j == 4]):
        return 6
    elif len(cardsmap) == 2 and any([True for i, j in cardsmap.items() if j == 3 or j == 2]):
        return 5
    elif len(cardsmap) == 3 and any([True for i, j in cardsmap.items() if j == 3]):
        return 4
    elif len(cardsmap) == 3 and any([True for i, j in cardsmap.items() if j == 2]):
        return 3
    elif len(cardsmap) == 4:
        return 2
    else:
        return 1
def CompareValues(valueA:str, valueB:str):
    valueA = valueA.split(' ')[0]
    valueB = valueB.split(' ')[0]
    typeCardsA = GetTypeOfCards(valueA)
    typeCardsB = GetTypeOfCards(valueB)
    if typeCardsA > typeCardsB:
        return 1
    elif typeCardsA < typeCardsB:
        return -1
    else:
        cardmapvalue = {'A': 14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
        for i, v in zip(valueA, valueB):
            if cardmapvalue[i] > cardmapvalue[v]:
                return 1
            elif cardmapvalue[i] < cardmapvalue[v]:
                return -1
filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day7_InputData.txt"
filelines = open(filepath, '+r').readlines()
finalvalue:int = 0
filelines.sort(key = cmp_to_key(CompareValues))
for line, idx in zip(filelines, range(1, len(filelines)+1)):
    finalvalue += (int(line.split(' ')[1]) * idx)
print(finalvalue)
