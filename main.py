import random

def chessboard(cbList):
    print("ChessBoard:\n"
          " " + cbList[6] + " | " + cbList[7] + " | " + cbList[8] + " \n"
          "-----------\n"
          " " + cbList[3] + " | " + cbList[4] + " | " + cbList[5] + " \n"
          "-----------\n"
          " " + cbList[0] + " | " + cbList[1] + " | " + cbList[2] + " \n")

def ruler():
    print("please use number keyboard:\n"
          " " + "7" + " | " + "8" + " | " + "9" + " \n"
          "-----------\n"
          " " + "4" + " | " + "5" + " | " + "6" + " \n"
          "-----------\n"
          " " + "1" + " | " + "2" + " | " + "3" + " \n")

def choose():
    a = raw_input("do you want the first?(please enter yes or no):\n")
    c = ["yes", "no"]
    if a not in c:
        print("please enter yes or no")
        choose()
    else:
        return a

def chooseAgain():
    a=raw_input("do you want again?\n")
    c = ["yes", "no"]
    if a not in c:
        print("please enter yes or no")
        chooseAgain()
    else:
        return a

def playermove(cbList, lastList, player):
    a = input("It is you turn\n")
    if a-1 not in lastList:
        print("Please enter the correct content\n")
        playermove(cbList, lastList, player)
    else:
        cbList[a-1] = player
        lastList.remove(a-1)
        return cbList, lastList,a-1

def compStep(cbList,lastList,cList,a,computer):
    cbList[a] = computer
    lastList.remove(a)
    cList.append(a)
    chessboard(cbList)
    return cbList,lastList,cbList

def judgment(wList, List):
    winList = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
    win = 0
    n = 10
    for w in winList:
        if [l for l in List if l in w]:
            continue
        else:
            a=len([l for l in wList if l in w])
            if a == 3:
                win = 1
                break
            else:
                if a == 2:
                    n = [l for l in w if l not in wList][0]
                    break
    return win,n

def compMove(cbList, lastList,cList,pList,computer,player,a):
    if lastList:
        cbList, lastList, cbList = compStep(cbList, lastList, cList, a, computer)
        if lastList:
            win, n = judgment(cList, pList)
            if win == 1:
                print("computer win!")
                return
            else:
                cbList, lastList, playerStep = playermove(cbList, lastList, player)
                pList.append(playerStep)
                win, n = judgment(cList, pList)
                if n != 10:
                    a = n
                    compStep(cbList, lastList, cList, a, computer)
                    print("computer win!")
                    return
                win, n = judgment(pList, cList)
                if win == 1:
                    print("you win!")
                    return
                else:
                    if n != 10:
                        a = n
                        compMove(cbList, lastList, cList, pList, computer, player, a)
                    else:
                        if lastList:
                            a = random.choice(lastList)
                            compMove(cbList, lastList, cList, pList, computer, player, a)
                        else:
                            print("draw!")
                            return
        else:
            print("draw!")
            return
    else:
        print("draw!")
        return

def computerFirst(cbList,lastList):
    pList = []
    cList = []
    player = "X"
    computer = "O"
    a = 4
    cbList, lastList, cbList = compStep(cbList, lastList, cList, a, computer)
    cbList, lastList, playerStep= playermove(cbList, lastList, player)
    pList.append(playerStep)
    if playerStep in [1, 7]:
        a = random.choice([3,5])
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return

    if playerStep in [3, 5]:
        a = random.choice([1,7])
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return

    if playerStep in [0, 8]:
        a = random.choice([1,2,3,5,6,7])
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return
    if playerStep in [2, 6]:
        a = random.choice([1, 0, 3, 5, 8, 7])
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return

def playerFirst(cbList,lastList):
    pList = []
    cList = []
    player = "O"
    computer = "X"
    chessboard(cbList)
    cbList, lastList, playerStep = playermove(cbList, lastList, player)
    pList.append(playerStep)
    if playerStep ==4:
        a = random.choice([0,2,6,8])
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return
    if playerStep !=4:
        a = 4
        compMove(cbList, lastList, cList, pList, computer, player, a)
        return

def main():
    cbList = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
    lastList = [1,2,3,4,5,6,7,8,0]
    ruler()
    firstP = choose()
    if firstP == "no":
        computerFirst(cbList,lastList)
    else:
        playerFirst(cbList, lastList)
    a = chooseAgain()
    if a == "yes":
        main()
    else:
        return

main()



