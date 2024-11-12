testingdata = [(71530, 940200)]
realdata = [(61709066, 643118413621041)]
for oneinput in realdata:
    firstvalidvalue = 0
    for i in range(1, oneinput[0]):
        if int(oneinput[1]/i) <= (oneinput[0] - i):
            firstvalidvalue = i
            break
    lastvalidvalue = 61709066
    for i in reversed(range(1, oneinput[0])):
        if int(oneinput[1]/i) <= (oneinput[0] - i):
            lastvalidvalue = i
            break

print(lastvalidvalue-firstvalidvalue)
input()