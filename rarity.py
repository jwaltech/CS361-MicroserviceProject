def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def clearSend():
    f1 = open("send.txt", "w")
    f1.write("")
    f1.close()

def writeErr(str):
    f1 = open("receive.txt","w")
    errorString = "E," + str
    f1.write(errorString)
    f1.close()
    clearSend()

def rarityNum(str):
    returnVal = 0
    if(str == "common"):
        returnVal = 1
    elif(str == "rare"):
        returnVal = 2
    elif(str == "super-rare"):
        returnVal = 3
    elif(str == "ultra-rare"):
        returnVal = 4
    else:
        returnVal = 0

    return returnVal

isRunning = True

while (isRunning == True):
    f1 = open("send.txt", "r")
    input = f1.read()
    f1.close()

    if(len(input) > 0):
        if(input[0] == 'S'):
            stringArr = input.split(",")

            if((isfloat(stringArr[1]) == True) and len(stringArr) == 4):
                floatPrice = float(stringArr[1])

                cuValue = rarityNum(stringArr[2])
                newValue = rarityNum(stringArr[3])

                if((cuValue == 0) or (newValue == 0)):
                    writeErr("Incorrect rarity values")
                else:

                    valueDiff = 0
                    multFactor = 1.5
                    newPrice = floatPrice

                    if (newValue > cuValue):
                        valueDiff = newValue - cuValue
                        for i in range(valueDiff):
                            newPrice = newPrice * multFactor
                    elif (cuValue > newValue):
                        valueDiff = cuValue - newValue
                        for i in range(valueDiff):
                            newPrice = newPrice / multFactor
                    else:
                        valueDiff = 0

                    #stringPrice = str(newPrice)
                    newString = "R," + "{:.2f}".format(newPrice)

                    f4 = open("receive.txt", "w")
                    f4.write(newString)
                    f4.close()
                    clearSend()
            else:
                writeErr("string is not correct length")
        else:
            writeErr("S flag is not correct")





