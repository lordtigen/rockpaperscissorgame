import random 
import time
#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[random.randint(0,2)]

print("""\nCONDITIONS
      \nTOPLAM 3 EL OYNANIR. 3 ELDEN EN FAZLA ELI KAZANAN GALIPTIR.
      \nEGER 3 ELDE DE KIMSE GALIP GELEMEZSE TEKRAR OYNANIR.
      \nSIZ HESAPLAYIN ARTIK KIMIN KAZANACAGINI O KADAR KODLAMADIM :D
      \nILK PROJEM OLDUGU ICIN KIZMAYIN LUTFEN. <3
      """)

#set player to False
player = False

oyun_eli = 0

def starter():
    print("Starting Game!!!")
    time.sleep(1)
    print("******3******")
    time.sleep(1)
    print("******2******")
    time.sleep(1)
    print("******1******")
    time.sleep(1)
    game()
    
def game():
    global player
    global oyun_eli
    while player == 0 and oyun_eli < 3:
    #set player to True
        global computer
        player = raw_input("Rock, Paper, Scissors?")

        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose! " + computer + " covers " + player)
            else:
                print("You win! " + player + " smashes " + computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose! " + computer + " cut " + player)
            else:
                print("You win! " + player + " covers " + computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose... " + computer + " smashes " + player)
            else:
                print("You win! " + player + " cut " + computer)
        else:
            print("That's not a valid play. Check your spelling!")

        oyun_eli += 1
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[random.randint(0,2)]
        
starter()