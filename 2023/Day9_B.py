def GetExtrapolateValue(numbers:list):
    if all([True if numbers[numbersidx] == numbers[numbersidx+1] else False for numbersidx in range(len(numbers)-1)]):
        if len(numbers) == 0:
            print("0 size")
        return numbers[0]
    else:
        numbers2 = [numbers[numbersidx+1] - numbers[numbersidx] for numbersidx in range(len(numbers)-1)]
        return numbers[0] - GetExtrapolateValue(numbers2)
    
filepath:str = "c:\\Users\\usr\\Documents\\Advent Of Code\\2023\\Day9_InputData.txt"
filelines = open(filepath, '+r').readlines()

finalvalue:int = 0
for fileline in filelines:
    linenumbers = [int(v) for v in fileline.split(' ') ]
    finalvalue += GetExtrapolateValue(linenumbers)
print(finalvalue)
input()
    