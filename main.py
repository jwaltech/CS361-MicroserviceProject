# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def clearReceive():
    f1 = open("receive.txt", "w")
    f1.write("")
    f1.close()


def calculateNewPrice(num, cuRarity,newRarity):
    returnVal = 0

    if(isfloat(num) == True):
        #print("writing to file");
        floatNum = float(num)

        f1 = open("send.txt","w")
        mssgString = "S,"+ "{:.2f}".format(floatNum) + "," + cuRarity + "," + newRarity
        f1.write(mssgString)
        f1.close()

        isListening = True

        while (isListening == True):
            f2 = open("receive.txt","r")
            input = f2.read()
            f2.close()

            if(len(input) > 0):
                clearReceive()
                if(input[0]=='R'):
                    stringArr = input.split(",")
                    if ((isfloat(stringArr[1]) == True) and len(stringArr) == 2):
                        newFloatPrice = float(stringArr[1])
                        returnVal = newFloatPrice

                elif(input[0]=='E'):
                    print(input)
                    returnVal = 0
                else:
                    print(input)
                    returnVal = 0

                isListening = False
            else:
                isListening = True
    else:
        print("number is not a float value")
    return returnVal


print(calculateNewPrice(20, "rare", "ultra-rare"))
