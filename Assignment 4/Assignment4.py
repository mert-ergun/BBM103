
import sys




def inputreading():
  player1=open(sys.argv[1]).readlines()

  player2=open(sys.argv[2]).readlines()
  global player1list
  global player2list
  player1list=[]
  player2list=[]
  for i in range(len(player1)):
        player1[i]=player1[i].replace("\n", "")
        list1=[]
        j=0
        if player1[i][j] == ";":
            list1.append("-")

        else:
            list1.append(player1[i][j])
            player1[i]=player1[i][j+1:]

        while j< len(player1[i])-1:

            if player1[i][j+1] == ";":
                list1.append("-")
            else:
                list1.append(player1[i][j+1])
                j+=1

            j+=1
        if player1[i][-1]==";":
            list1.append("-")
        player1list.append(list1)



  for i in range(len(player2)):
        player2[i]=player2[i].replace("\n", "")
        list1=[]
        j=0
        if player2[i][j] == ";":
            list1.append("-")

        else:
            list1.append(player2[i][j])
            player2[i]=player2[i][j+1:]

        while j< len(player2[i])-1:

            if player2[i][j+1] == ";":
                list1.append("-")
            else:
                list1.append(player2[i][j+1])
                j+=1

            j+=1
        if player2[i][-1]==";":
            list1.append("-")
        player2list.append(list1)
  global player1moves
  global player2moves
  player1moves=open(sys.argv[3]).readline().split(";")
  player2moves=open(sys.argv[4]).readline().split(";")
  global output
  output=open("Battleship.txt", "w")


def shipfinder(playerlist):
    for toFind in ["B14", "B24", "P42", "P32","P12","P22"]:
        for i in range(10):
            for j in range(10):
                m=False
                if playerlist[i][j]==toFind[0]:

                    for k,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                        try:
                            if playerlist[i+k][j+b]==toFind[0] and (playerlist[i+k*2][j+b*2]==toFind[0] or toFind[0]=="P"):
                                m = True
                                r=(k,b)
                        except:
                            pass
                    if m== True:
                        playerlist[i][j]=toFind[:2]
                        for t in range(1,int(toFind[-1])):
                            playerlist[i+t*r[0]][j+t*r[1]]=toFind[:2]
                        break

            if m== True:
                break

    global ships
    ships={}
    ships["B1_1"],ships["B2_1"],ships["B2_2"],ships["B1_2"],ships["P3_1"],ships["P4_1"],ships["P3_2"],ships["P4_2"],ships["P1_1"],ships["P2_1"],ships["P1_2"],ships["P2_2"],ships["C_1"],ships["C_2"],ships["D_1"],ships["D_2"],ships["S_1"],ships["S_2"]=4,4,4,4,2,2,2,2,2,2,2,2,5,5,3,3,3,3
    global letters
    letters={}
    letters["A"],letters["B"],letters["C"],letters["D"],letters["E"],letters["F"],letters["G"],letters["H"],letters["I"],letters["J"]=0,1,2,3,4,5,6,7,8,9



def gameOutput(Turn):
    if Turn==1:
        print("Battle of Ships Game\n")
        output.write("Battle of Ships Game\n\n")
    
    
    def player1or2(z):
        if z==2:
            player="_1"
            global player2moves
            turnmoves=player2moves
            global player1list
            notturnlist=player1list
        else:
            player="_2"
            global player2list
            notturnlist=player2list

            global player1moves
            turnmoves=player1moves

        print(f"Player{z}’s Move\n")
        output.write(f"Player{z}’s Move\n\n")
        print(f"Round : {Turn}\t\t\t\t\tGrid Size: 10x10\n")
        output.write(f"Round : {Turn}\t\t\t\t\tGrid Size: 10x10\n\n")
        print("Player1’s Hidden Board\t\tPlayer2’s Hidden Board")
        output.write("Player1’s Hidden Board\t\tPlayer2’s Hidden Board\n")
        print("  A B C D E F G H I J\t\t  A B C D E F G H I J")
        output.write("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
        for i in range(10):
            print(f"{i+1}", end="")
            output.write(f"{i+1}")
            for j in range(10):
                if player1list[i][j][0] == "O":
                    to_print = "O"
                elif player1list[i][j][0] == "X":
                    to_print = "X"
                else:
                    to_print = "-"
                print(" "*(i!=9 or j!=0) + to_print, end="")
                output.write(" "*(i!=9 or j!=0) + f"{to_print}")

            print("\t\t", end="")
            output.write("\t\t")
            print(f"{i+1}", end="")
            output.write(f"{i+1}")
            for j in range(10):
                if player2list[i][j][0] == "O":
                    to_print = "O"
                elif player2list[i][j][0] == "X":
                    to_print = "X"
                else:
                    to_print = "-"
                print(" "*(i!=9 or j!=0) + to_print, end="")
                output.write(" "*(i!=9 or j!=0) + f"{to_print}")
            print("")
            output.write("\n")
        print("")
        output.write("\n")

        for j in [["C"],["B1","B2"],["D"],["S"],["P1","P2","P3","P4"]]:
            ship_1,ship_2="",""

            for k in j:
                ship_1=(ships[k+"_1"]==0)*("X "+ship_1) or ship_1+"- "
                ship_2=(ships[k+"_2"]==0)*("X "+ship_2) or ship_2+"- "

            ship="Carrier"*(k[0]=="C") or "Battleship"*(k[0]=="B") or "Destroyer"*(k[0]=="D") or "Submarine"*(k[0]=="S") or "Patrol Boat"*(k[0]=="P")
            tabNumber="\t"*2*(k[0]=="C") or "\t"
            tabNumber2="\t"*3*(k[0]=="P") or "\t\t\t\t"
            print(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2}")
            output.write(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2}\n")
        print("")
        output.write("\n")
        move= turnmoves[Turn-1]
        print(f"Enter your move: {move}\n")
        output.write(f"Enter your move: {move}\n\n")
        move=move.split(",")

        try:
            ships[notturnlist[int(move[0]) - 1][letters[move[1]]]+player]-=1
        except:
            pass
        notturnlist[int(move[0])-1][letters[move[1]]]=(notturnlist[int(move[0])-1][letters[move[1]]]=="-")*"O" or "X"+notturnlist[int(move[0])-1][letters[move[1]]]


    player1or2(1)
    player1or2(2)
    sumplayer1=0
    sumplayer2=0
    for i in ships:
        if i[-1]=="1":
            sumplayer1+=ships[i]
        else:
            sumplayer2+=ships[i]
    
    
    def finalGame(z):
        print(f"Player{z} Wins!\n")
        output.write(f"Player{z} Wins!\n\n")
        print("Final Information\n")
        output.write("Final Information\n\n")
        print("Player1’s Board\t\t\t\tPlayer2’s Board")
        output.write("Player1’s Board\t\t\t\tPlayer2’s Board\n")
        print("  A B C D E F G H I J\t\t  A B C D E F G H I J")
        output.write("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
        for i in range(10):
            print(i+1,end="")
            output.write(f"{i+1}")
            for j in range(10):
                toprint=player1list[i][j][0]
                print(" "*(i!=9 or j!=0)+toprint,end="")
                output.write(" "*(i!=9 or j!=0)+f"{toprint}")
            print("\t\t",end="")
            output.write("\t\t")
            print(i+1,end="")
            output.write(f"{i+1}")
            for j in range(10):
                toprint=player2list[i][j][0]
                print(" "*(i!=9 or j!=0)+toprint,end="")
                output.write(" "*(i!=9 or j!=0)+f"{toprint}")
            print("")
            output.write("\n")
        print("")
        output.write("\n")
        for j in [["C"],["B1","B2"],["D"],["S"],["P1","P1","P3","P4"]]:
            ship_1,ship_2="",""
            for k in j:
                ship_1=(ships[k+"_1"]==0)*("X "+ship_1) or ship_1+"- "
                ship_2=(ships[k+"_2"]==0)*("X "+ship_2) or ship_2+"- "
            ship="Carrier"*(k[0]=="C") or "Battleship"*(k[0]=="B") or "Destroyer"*(k[0]=="D") or "Submarine"*(k[0]=="S") or "Patrol Boat"*(k[0]=="P")
            tabNumber="\t"*2*(k[0]=="C") or "\t"
            tabNumber2="\t"*3*(k[0]=="P") or "\t\t\t\t"
            print(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2}")
            output.write(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2}\n")
    if sumplayer1==0:
        finalGame(2)
    elif sumplayer2==0:
        finalGame(1)
    else:
        gameOutput(Turn+1)
        

inputreading()
shipfinder(player1list)
shipfinder(player2list)

for element in player1list:
    output.write(f"{element}\n")
gameOutput(1)

for element in player1list:
    output.write(f"{element}\n")