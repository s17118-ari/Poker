p = 1  # Starting with player 1
betamount = 10
potamount = 0
optionsloop = False
p1stack = 100
p2stack = 100
p1option = 1
p2option =2




def bet(player):
    global p # Starting with player 1
    global betamount 
    global potamount
    player = player - betamount
    potamount = potamount + betamount
    return player, potamount

def turns():    
    global optionsloop
    global p
    global p1stack
    global p2stack
    global p1option
    global p2option
####this is just the first intial bet code - so when the game starts both players lose 10 from their stacks andthe pot = 20
    
    while not optionsloop :  # Run indefinitely
        if p == 1:
            # Player 1's turn
            print("Player 1's turn")
            # Add your code for player 1's turn here
            p1stack,potamount = bet(p1stack)
               
            print("Player 1's stack:", p1stack)
            print("Pot amount:", potamount)
            # Switch to player 2
            p = 2
            #if p1stack == 0 or p1option == 3 :
             #   optionsloop = True
            #else:
            #    turns()
            
        elif p == 2:
            # Player 2's turn
            print("Player 2's turn")
            # Add your code for player 2's turn here
            p2stack,potamount = bet(p2stack)
            print("Player 2's stack:", p2stack)
            print("Pot amount:", potamount)
            # Switch back to player 1
            p = 1
            break
            #if p2stack == 0 or p2option == 3 :
             #   optionsloop = True
            #else:
             #   turns()
#############
#delete this, this is just for testing
    while (p1option != 3 and p2option != 3) and (p1stack != 0 and p2stack != 0):
        p1option = int(input("p1,what option do you want, check, bet 10, raise or fold"))#these will be the option which is pressed, so button input
        if p1option == 0:
            p2option =int(input("p2, what option do you want, check, bet, raise or fold"))
            if p2option == p1option:
                print ("show a card")#make it actually show a card
            else:
                if p2option == 1:
                    bet(p2stack)
                    print("Player 2's stack:", p2stack)
                    print("Pot amount:", potamount)
                    break
                else:
                    print("doesnt work")
        elif p1option == 1:
            bet(p1stack)
            break
        elif p1option == 2:
            betamount = int(input("how much would you liek to bet"))
            bet(p1stack)
            break
        else:
            print ("doenst work omfg")



turns()