from matplotlib import pyplot as plt
import traceback

def drawGraph(ratioList):
    figure = plt.figure()
    

    graph = figure.add_subplot(111)
    barGraph = figure.add_subplot(121)
    
    graph.plot(ratioList)

    plt.show()

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
        drawGraph(getRatio(fibonacci()))

    except:
        traceback.print_exc()

    finally:
        print(f":)")
