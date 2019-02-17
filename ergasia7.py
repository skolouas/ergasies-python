import random
print("Ayto einai ena paixnidi triliza 3x3")
board=["","","","","","","","","",""]
#deigma tou board
def arxiko_dapedo():
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('------')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('------')
    print('7' + ' | ' + '8' + ' | ' + '9')
#ftiaxnei to board
def dapedo():
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
#epilogh pioniou    
def dialexepioni():
    global player
    global oponnent
    while True:  
        pioni=input("Dialexe X h O: ").upper()
        if pioni=="X" or pioni=="O":
            if pioni=="X":
                player="X"
                oponnent="O"
            else:
                player="O"
                oponnent="X"
            break       
        else:
            print("PREPEI ANAGASTIKA MONO X H O")
    return player        
            
    print ("To pioni mou einai to: ",player)
#nikhths tou paixnidiou    
def nikhths(x,y):       

    return ((x[7] == y and x[8] == y and x[9] == y) or 
    (x[4] == y and x[5] == y and x[6] == y) or
    (x[1] == y and x[2] == y and x[3] == y) or
    (x[7] == y and x[4] == y and x[1] == y) or
    (x[8] == y and x[5] == y and x[2] == y) or
    (x[9] == y and x[6] == y and x[3] == y) or
    (x[7] == y and x[5] == y and x[3] == y) or
    (x[9] == y and x[5] == y and x[1] == y))
#arxikopoihseis
playagain=True
done=True
# elenxei gia isopalia
def isopalia():
    k=1
    for i in range(1,9):
        if board[i]!="":
            k=k+1
    if k==9:
        return True
    else:
        return False
        
while done==True:
    dialexepioni()
    arxiko_dapedo()
    while True:
        while True:    
            epilogh=input("Dialexe tetragwno(1-9): ")
            if str.isdigit(epilogh):
                epilogh=int(epilogh)
                if epilogh>=1 and epilogh<=9:
                    break
                else:
                    print("Prepei 1-9")
            else:
                print("Prepei 1-9")
        if board[epilogh] !="X" and board[epilogh]!="O":
            if player=="X":
                board[epilogh]="X"
            else:
                board[epilogh]="O"
            if nikhths(board,player):
                dapedo()
                print("Nikhses")
                playagain=False
                break
            while True:
                random.seed()
                ypologisths=random.randint(1,9)
                if board[ypologisths] !="X" and board[ypologisths]!="O":
                    if oponnent=="X":
                        board[ypologisths]="X"
                    else:
                        board[ypologisths]="O"    
                    if nikhths(board,oponnent):
                        dapedo()
                        print("Exases")
                        playagain=False
                        break
                    break
                else:
                    if isopalia() == True:
                        print("isopalia")
                        playagain=False
                        break
        else:
            print("Dialexe allo tetragwno")
        if playagain==False:
            break
        dapedo()
    while playagain==False:
        print("Thes na xanapaixeis/nai h oxi?")
        apanthsh=input()
        if apanthsh=="nai" or apanthsh=="oxi":
            if apanthsh=="oxi":
                done="False"
                playagain=True
            else:
                 playagain=True
                 board=["","","","","","","","","",""]
        else:
            print("Lathos apanthsh")
                
            
        

            
                
            
    

        
    
    
    
    
