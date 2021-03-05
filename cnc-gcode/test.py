import serial
import colorama

def fileManager():

    #file locations
    inputPath = '/home/zai/Dropbox/coding/python/cnc-gcode/resources/inputData.txt'
    outputPath = '/home/zai/Dropbox/coding/python/cnc-gcode/resources/outputData.txt'

    with open(inputPath, 'r') as f, open(outputPath,'w')as w:
        for x in f:
            print("[+]line: {}".format(x))
            newLine = x.replace("#1000","0.100")
            newLine = newLine.replace("#1001","10.0")
            newLine = newLine.replace("#1002","-0.010")
            newLine = newLine.replace("#1003","0.0139")
            newLine = newLine.replace("#1004","0.0139")
            operation1= newLine.split("[")
            print(operation1)
            print("modi: {}".format(newLine))
            w.write(newLine)

def split():

    operationArray = []
    txt ="G00 X[0.0139*135.277] Y[0.0139*585.301]"

    operationVal = ['0','1','2','3','4','5','6','7','8','9','*','.']

    print("[+] original text: {}".format(txt))

    #replace "[" caracter and split accordinly
    modText = txt.replace("]","[").split("[")
    
    print("[+] split list:{}\n[-] lenght of list: {}".format(modText,len(modText)))

    for x in range(len(modText)):
        for y in modText[x]:
            if y in operationVal:
                print("[+] operation: {}".format(modText[x]))
                operationArray.append(modText[x])
                break

    print("[+] operation array: {}".format(operationArray))

def serialConnection():
    port = "/dev/ttyACM0"
    baudrate =115200

    try:
        arduino = serial.Serial(port, baudrate, timeout= 1)
        print("[+] Connection succesfull")
    except:
        print("[-] Unsuccessfull connection")

    while True :
        line = arduino.readline().strip().decode()
        print(line)

def main():
    #fileManager()
    split()

if __name__ == "__main__":
    main()
