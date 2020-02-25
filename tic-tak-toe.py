import sys
import os
import time
p1=[]
p2=[]
ps1=0
ps2=0
os.system('clear')
print('*'*20,"welcome to TIC-TAC-TOE the game",'*'*20)
board=[['| 0 |','1 |','2 |'],['| 3 |','4 |','5 |'] ,['| 6 |','7 |','8 |']]
win_combination=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
print()
def board_change1(k):
    if k==0:
        board[0][0]='| X |'
    elif k==3:
        board[1][0]='| X |'
    elif k==6:
        board[2][0]='| X |'
    elif k==1 or k==2:
        board[0][k]='X |'
    elif k==4: 
        board[1][1]='X |'
    elif k==5:
        board[1][2]='X |'
    elif k==7:
        board[2][1]='X |'
    elif k==8:
        board[2][2]='X |'

def board_change2(k):
    if k==0:
        board[0][0]='| O |'
    elif k==3:
        board[1][0]='| O |'
    elif k==6:
        board[2][0]='| O |'
    elif k==1 or k==2:
        board[0][k]='O |'
    elif k==4: 
        board[1][1]='O |'
    elif k==5:
        board[1][2]='O |'
    elif k==7:
        board[2][1]='O |'
    elif k==8:
        board[2][2]='O |'

for q in range(1,10):
    print()
    os.system('clear')
    print('-------------')
    for i in board:
        for x in i:
            print(x,end=" ")
        print('\n-------------')
    
    if q%2==0:
        k2=int(input("enter the position player2 >>>"))
        for m in p1:
            if m==k2:
                while m==k2:
                    print()
                    print("THE POSITION IS ALREADY TAKEN !!!")
                    print()
                    k2=int(input("please enter another position player2 >>>"))
        for m in p2:
            if m==k2:
                while m==k2:
                    print()
                    print("THE POSITION IS ALREADY TAKEN !!!")
                    print()
                    k2=int(input("please enter another position player2 >>>"))
        else:            
            p2.append(k2)
            board_change2(k2)
    else:
        k1=int(input("enter the position player1 >>>"))
        for m in p2:
            if m==k1:
                while m==k1:
                    print()
                    print("THE POSITION IS ALREADY TAKEN !!!")
                    print()
                    k1=int(input("please enter another position player1 >>>"))
        for m in p1:
            if m==k1:
                while m==k1:
                    print()
                    print("THE POSITION IS ALREADY TAKEN !!!")
                    print()
                    k1=int(input("please enter another position player1 >>>"))
        else:
            p1.append(k1)
            board_change1(k1)
    if q==9:
        print()
        os.system('clear')
        print('-------------')
        for i in board:
            for x in i:
                print(x,end=" ")
            print('\n-------------')
                
        
for combination in win_combination:
    if set(combination) <= set(p1):
        ps1+=1
    elif set(combination) <= set(p2):
        ps2+=1
print()
print("calculating results....")
time.sleep(2)
if ps1>ps2:
    os.system('clear')
    print('*'*30)
    print('*'*30)
    print()
    print(" PLAYER 1 WINS THE GAME")
    print()
    print('*'*30)
    print('*'*30)
elif ps1<ps2:
    os.system('clear')
    print('*'*30)
    print('*'*30)
    print()
    print(" PLAYER 2 WINS THE GAME")
    print()
    print('*'*30)
    print('*'*30)
else:
    os.system('clear')
    print('*'*30)
    print('*'*30)
    print()
    print(" THE GAME ENDS IN TIE")
    print()
    print('*'*30)
    print('*'*30)	



