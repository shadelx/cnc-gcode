import colorama

colorama.init()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
print(CLEAR_SCREEN + RED + 'Welcome!' + RESET)
# fil = 'ahl'

# phrase = ['hello', 'world']


# for x in phrase:
#     for y in x:
#         if y in fil:
#             print("true: {}".format(y))

operationArray = []
resultArray = []
commandFilter = ['G00','G01']

txt ="G00 X[0.0139*135.277] Y[0.0139*585.301]"
print("[+] original text: {}".format(txt))

modText = txt.replace("]","[").replace("[",'')
print("[+] first modification: {}".format(modText))
modText = modText.split()
print("[+] array modification: {}".format(modText))

for x in modText:
    if x not in commandFilter:
        operationArray.append(x)
print("operationArray value: {}".format(operationArray))

for y in operationArray:
    print("[+] operation: {}".format(y[1:]))
    resultArray.append(eval(y[1:]))

print(resultArray)