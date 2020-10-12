# CHANGE IT BACK TO 100 if you want

import traceback

def fibonacci():
    prevNum = 1 #previous number
    curNum = 1 # current number
    fibNumList = [prevNum, curNum]
    i = 2

    while i < 10:
        newNum = prevNum + curNum
        fibNumList.append(newNum)
        prevNum = curNum
        curNum = newNum
        i+=1
    return(fibNumList)

def getRatio(fibNumList):
    ratioList = []

    for i in range(0,len(fibNumList)-1):
        ratio = fibNumList[i+1]/fibNumList[i]
        ratioList.append(ratio)

    return(ratioList)

if __name__ == "__main__":
    try:
        print(getRatio(fibonacci()))

    except:
        traceback.print_exc()

    finally:
        print(f":)")
