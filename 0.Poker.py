#IMPORTS
import random
import tkinter as tk
from tkinter import *

##############################################
#suits C=0 D=1 H=2 S=3
#rank A=1,2=2...J=11,Q=12,K=13

card =["01", "02", "03", "04", "05", "06", "07", "08", "09", "0X", "0J", "0Q", "0K", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1X", "1J", "1Q", "1K","21", "22", "23", "24", "25", "26", "27", "28", "29", "2X", "2J", "2Q", "2K","31", "32", "33", "34", "35", "36", "37", "38", "39", "3X", "3J", "3Q", "3K"]

cards=[]
deck=[]
p1deck=[]
p2deck=[]
pcard =[]
p1nums=[]
p2nums=[]
p1suits=[]
p2suits=[]
###################################
#all the global variables
entryBox = None
root = None
p1name = None
p2name = None
p1stack = None
p2stack = None
p1stackbox = None
p1namebox = None
p2stackbox = None
p2namebox = None
p1hand = None
p2hand =None
p1handname = "temphand1"
p2handname = "temphand2"
potamount = None


###############################################
#MAKING ALL THE CARDSq
def make_cards():
    global card
    global cards
#    x=range(1,13)
#    y=range(0,4)
#    for n in x:
#        n=str(n)#CANT CONCATINATE STR + INT
#        for m in y:
#            m=str(m)
#            card_image=n+m+".png" 
#            cards.append(card_image)#ADD TO THE END OF CARDS LIST

   
    for item in card:
        tempcard = item + ".png"
        cards.append(tempcard)
    print (cards)
    return cards
###############################################
#pickinga ll the cards displayed ont he screen
#picking [how_many] random cards and adding to a new list after checking not already picked and remove from list of all cards
def pick():
    global cards
    global deck 
    for i in range (3):
        deck_card=random.choice(cards)
        if deck_card not in deck:
            cards.remove(deck_card)
            deck.append(deck_card)
        else:
            pick()
    print (deck)
def pickp1():
   global cards
   global deck
   for i in range (2):
        deck_card=random.choice(cards)
        if deck_card not in deck or p1deck or p2deck:
            cards.remove(deck_card)
            p1deck.append(deck_card)
        else:
            pick()
   print (p1deck)

def pickp2():
   for i in range (2):
        deck_card=random.choice(cards)
        if deck_card not in deck or p1deck or p2deck:
            cards.remove(deck_card)
            p2deck.append(deck_card)
        else:
            pick()
   print(p2deck)
#################################################################################
   #handranking algorithm
def handmake():
   global cards
   global deck
   global p1deck
   global p1hand
   global p2deck
   global p2hand

   p1hand = p1deck + deck
   print (p1hand)
   p2hand = p2deck + deck
   print (p2hand)


def suitandnum():#listof thte suits and the numbers of eachdeck

   global p1hand
   global p2hand
   global p1nums
   global p2nums
   global p1suits
   global p2suits
   for string in p1hand:
      temp12=(string[1])
      p1nums.append(temp12)


   print (p1nums)


   for string in p2hand:
      temp2=(string[1])
      p2nums.append(temp2)
   print (p2nums)

   for string in p1hand:
      if string[0] =="X":
         temp6 = "10"
      elif string[0] =="J":
         
         temp6 =  "11"
      elif string[0] =="Q":
         temp6 = "12"
      elif string[0] =="K":
         temp6 = "13"
      else:
         temp6 = int(string[0])
      p1suits.append(temp6)
   print (p1suits)

   for string in p2hand:
         if string[0] =="X":
            temp6 = "10"
         elif string[0] =="J":
            
            temp6 =  "11"
         elif string[0] =="Q":
            temp6 = "12"
         elif string[0] =="K":
            temp6 = "13"
         else:
            temp6 = int(string[0])
         p2suits.append(temp6)
   print (p2suits)

#
def flush(tempdeck):#see if all the suits are the same
      first_suit = tempdeck[0]
      for suit in tempdeck[1:4]:
         if suit != first_suit:
               print ("f")
               return False
      print("t")
      return True
def ofakinds(tempdeck):
    numrepeats = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "X": 0, "J": 0, "Q": 0, "K": 0}
    for card in tempdeck:
        numrepeats[card] += 1  # Increment the count for the card value
    print (numrepeats)




def straight_high_card(cards):
    for value in range(1, 11):
        straight_found = True
        for k in range(5):
            if str(value + k) not in cards:  # Convert value + k to string before checking
                straight_found = False
                break
        if straight_found:
            return value + 4
    return None

def ranking():###actual raanking part
   global p1hand
   global p2hand
   global p1nums
   global p2nums
   global p1suits
   global p2suits
   p1testdeck =["1","2","3","4","5"]
   p2testdeck=["1","1","1","1","1"]
   suitandnum()
   flush(p1suits)
   flush(p2suits)
   ofakinds(p1testdeck)
   ofakinds(p2testdeck)
   ari= straight_high_card(p1testdeck)
   print(ari)

   
###############################################
   #give the check bet fold raise buttons functions
def check():
   print ("0")

def bet():
   print ("1")

def betmore():
   print ("2")

def fold():
   print ("3")
#####################################################
def kill():
 global root
 root.destroy() # Kill the root window!

def openandclose2():
   get_input()
   kill()
   pokerwindow()

def pokerwindow():
   global potamount
   global root
   global p1name
   global p1stack
   global p2name
   global p2stack
   global p1handname
   global p2handname
   
   root= Tk()
   root.attributes("-fullscreen", True)
   root.title("poker")
   root.configure(background="#35654d")

   close = Button (root,text="close",bg="red",command = kill)# to close window 
   close.place(x=1300, y=35)

   
# Add the public cards to the screen
   for i in range (0,3):
    i=str(i)
    pcard= "card" + i
    i=int(i)
    im = PhotoImage(file=deck[i]) # Create the PhotoImage widget
    smallim = im.subsample(4,4)
    pcard= Label(root, image=smallim) # Create a label with#### image
    pcard.image = smallim# Always keep a reference to avoid garbage collection
    if i == 2:
     pcard.place(x=125,y=35) # Put the label into the window
    elif i== 1:
     pcard.place(x=400,y=35)
    elif i==0:
     pcard.place(x=675,y=35)
    else:
       print ("doesnt work")

#p1 cards on screen
   for i in range (0,2):
    i=str(i)
    p1card= "card" + i
    i=int(i)
    im = PhotoImage(file=p1deck[i]) # Create the PhotoImage widget
    smallim = im.subsample(5,5)
    p1card= Label(root, image=smallim) # Create a label with#### image
    p1card.image = smallim# Always keep a reference to avoid garbage collection
    if i== 1:
     p1card.place(x=110,y=380)
    elif i==0:
     p1card.place(x=285,y=380)
    else:
       print ("doesnt work")


   for i in range (0,2):
    i=str(i)
    p2card= "card" + i
    i=int(i)
    im = PhotoImage(file=p2deck[i]) # Create the PhotoImage widget
    smallim = im.subsample(5,5)
    p2card= Label(root, image=smallim) # Create a label with#### image
    p2card.image = smallim# Always keep a reference to avoid garbage collection
    if i== 1:
     p2card.place(x=600,y=380)
    elif i==0:
     p2card.place(x=775,y=380)
    else:
       print ("doesnt work")

   ############## p1 details
   p1label = Label (root,text=p1name,height=1, width=5,bg="#23a3e8",borderwidth=1, relief="solid",font=('Helvetica 17 bold',"20"))
   p1stacklabel = Label (root,text=p1stack,height=1, width=5,bg="#1d8ac4",borderwidth=3, relief="groove",font=('Helvetica 17 bold',"20"))#replace 1000 with some act text
   p1handlabel = Label (root,text=p1handname,height=1, width=9,bg="#1d8ac4",borderwidth=3, relief="groove",font=('Helvetica 17 bold',"20"))
   p1handlabel.place (x=200,y=600)
   p1label.place (x=110,y=600)
   p1stacklabel.place(x=110,y=650)
   
   ############ p2 details
   p2label = Label (root,text=p2name,height=1, width=5,bg="light blue",borderwidth=1, relief="solid",font=('Helvetica 17 bold',"20"))
   p2stacklabel = Label (root,text=p2stack,height=1, width=5,bg="light blue",borderwidth=3, relief="groove",font=('Helvetica 17 bold',"20"))#replace 1000 with some act text
   p2handlabel = Label (root,text=p2handname,height=1, width=9,bg="#1d8ac4",borderwidth=3, relief="groove",font=('Helvetica 17 bold',"20"))
   p2handlabel.place (x=680,y=600)
   p2label.place (x=600,y=600)
   p2stacklabel.place(x=600,y=650)
   ###################
       #check bet raise fold buttons
   checkbutton = Button (root,text="check",height=2, width=8,bg="#cac2f2",font=('Helvetica 17 bold',"19"),command = check)
   betbutton = Button (root,text="bet",height=2, width=8,bg="#e2aef2",font=('Helvetica 17 bold',"19"),command = bet)
   raisebutton = Button (root,text="raise",height=2, width=8,bg="#d3b0e8",font=('Helvetica 17 bold',"19"),command = betmore)
   foldbutton = Button (root,text="fold",height=2, width=8,bg="#f092a3",font=('Helvetica 17 bold',"19"),command = fold)
#give the buttons functions
   checkbutton.place(x=1200,y=320)
   betbutton.place(x=1200,y=420)
   raisebutton.place(x=1200,y=520)
   foldbutton.place(x=1200,y=620)
#################
   #pot
   
   potlabel = Label (root,text="pot",height=1, width=5,bg="light blue",font=('Helvetica 17 bold',"35"))
   pot = Label (root,text=potamount,height=1, width=5,bg="light blue",font=('Helvetica 17 bold',"35"))#replace 1000 with some act text
   potlabel.place (x=1000,y=35)
   pot.place(x=1000,y=95)
    
def get_input():
   global p1name
   global p1stack
   global p2name
   global p2stack   
   global p1namebox
   global p1stackbox
   global p2namebox
   global p2stackbox
   p1name = p1namebox.get()
   p2name = p2namebox.get()
   p1stack = p1stackbox.get()
   p2stack = p2stackbox.get()


def joingame():
   global root
   global p1name
   global p1stack
   global p2name
   global p2stack   
   global p1namebox
   global p1stackbox
   global p2namebox
   global p2stackbox

   root= Tk()
   root.attributes("-fullscreen", True)
   root.title("Join Game")

   close = Button (root,text="close",command = kill)# to close window 
   submit = Button (root,text="submit",height=3, width=11,bg="light blue",font=('Helvetica 17 bold',"18"),command = openandclose2)


   first = Label(root, text="player 1",font=('Helvetica 17 bold',20))# Create a label with words
   p1namelabel = Label(root, text = "p1's username ",font=('Helvetica 17 bold',20))
   p1namebox = Entry(root,
                width = 25,
                bg = "light yellow")
   
   p1stacklabel = Label(root, text = "p1's stack ",font=('Helvetica 17 bold',20))
   p1stackbox = Entry(root,
                width = 25,
                bg = "light yellow")


   second = Label(root, text="player 2",font=('Helvetica 17 bold',20))# Create a label with words
   p2namelabel = Label(root, text = "p2's username ",font=('Helvetica 17 bold',20))
   p2namebox =    Entry(root,
                width = 25,
                bg = "light yellow")
   p2stacklabel = Label(root, text = "p2's stack ",font=('Helvetica 17 bold',20))
   p2stackbox =   Entry(root,
                width = 25,
                bg = "light yellow")



   
   first.place(x=250, y=90)
   p1namelabel.place (x=250,y=120)
   p1namebox.place (x=450, y=122 )
   p1stacklabel.place (x=250,y=220)
   p1stackbox.place (x=450, y=222 )

   second.place(x=700, y=90)#where to put button on screen
   p2namelabel.place (x=700,y=120)
   p2namebox.place (x=900, y=122 )
   p2stacklabel.place (x=700,y=220)
   p2stackbox.place (x=900, y=222 )

   close.place(x=1300, y=35)
   submit.place(x=550,y=400)

def openandclose(): #only is needed for openingpoker()
  kill()
  joingame()

def openingpoker():
 global root
 root = Tk() # Create the root (base) window where all widgets go
 root.geometry("250x190")
 root.title ("welcome")
 first = Label(root, text="poker?",font=('Helvetica 17 bold',11))# Create a label with words
 first.pack()#.pack(pady=30) Put the label into the window
 myButton = Button(root, text="yes",command=openandclose)
 myButton.pack()
 nobutton = Button (root,text="no",command = kill)
 nobutton.pack()





###########################################
#ACTUAL RUNNING  
make_cards()
pick()
pickp1()
pickp2()
handmake()
ranking()
openingpoker()

root.mainloop()

