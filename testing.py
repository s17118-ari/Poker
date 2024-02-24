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
p1handname = None
p2handname =None
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
##############################################
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
    
    for string in p1hand:
        print (string[1])
    for string in p2hand:
        print (string[1])





     
def allcardstuff():

    make_cards()
    pick()
    pickp1()
    pickp2()
    handmake()
    suitandnum()
    




allcardstuff()