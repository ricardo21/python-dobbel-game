import random
import os
import time
import sys
from classes.bcolors import bcolors

ronde = 1
wins_computer = 0
wins_gebruiker = 0

SCHERM_TIMEOUT = 5
AANTAL_RONDES = 10
RONDE_NIVEAU_VERHOGEN = 5


def laat_een_zien(getal1_computer, getal1_gebruiker):
    print(bcolors.OKCYAN, "NIVEAU 2 - moeilijk", bcolors.ENDC)
    print("computer gooit: " , getal1_computer, bcolors.WARNING, " ?   ? " , bcolors.ENDC)
    print("u gooit: " , getal1_gebruiker, bcolors.WARNING,  " ?   ? ", bcolors.ENDC)
    print("\nDoe een gok...")

def laat_twee_zien(getal1_computer, getal2_computer, getal1_gebruiker, getal2_gebruiker):
    print("computer gooit: " , getal1_computer, " " , getal2_computer , bcolors.WARNING ,' ?' , bcolors.ENDC)
    print("u gooit: " , getal1_gebruiker, " ", getal2_gebruiker, bcolors.WARNING ,' ?' , bcolors.ENDC , "\n" )
    print("\nDoe een gok...")

def laat_dobbelstenen(computer1,computer2, computer3, gebruiker1,gebruiker2, gebruiker3):
    print("computer gooide: " , computer1, " " , computer2, ' ' , computer3)
    print("u gooide: " , gebruiker1, " ", gebruiker2, ' ' , gebruiker3 , "\n" )
    

def render_getallen(): 
     
    global result, ronde, wins_computer, wins_gebruiker    
    
    getal1 = random.randint(1,6)
    getal2 = random.randint(1,6)
    getal3 = random.randint(1,6)
    
    sum_gebruiker = getal1 + getal2 + getal3
    
    computer1 = random.randint(1,6)
    computer2 = random.randint(1,6)
    computer3 = random.randint(1,6)
    sum_computer = computer1 + computer2 + computer3
    
    winnende_hand = "(Winnende hand voor computer)"
    if wins_gebruiker > wins_computer:
        winnende_hand = "(Winnende hand voor u!)"
    elif ronde == 1:
        winnende_hand = ""
    elif wins_computer == wins_gebruiker:
        winnende_hand = "(gelijkspel)"    
    
    #print(quit)
    #print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

    print(bcolors.OKGREEN + '#Ronde:' , ronde , winnende_hand , "\n" + bcolors.ENDC)
    print("\nTussenstand: computer:", wins_computer , "u:" , wins_gebruiker)
    
    print("\nU krijgt een hulplijn...")
    
    #laat_een_zien(computer1, getal1)
    
    if wins_gebruiker >= RONDE_NIVEAU_VERHOGEN:
        laat_een_zien(computer1, getal1)
    elif wins_gebruiker <  RONDE_NIVEAU_VERHOGEN:
        laat_twee_zien(computer1, computer2, getal1, getal2)    
    
    gok = input("Wie gooit het hoogst? \nTyp nummer in:[1]computer [2]ikke [q] stoppen\n\n")
    
    if (gok == 1) or (2):
        gok = gok
    elif gok == 'q':
        sys.exit()
        quit()
    elif gok > 2:
        gok = 2        
        
    print("U heeft gekozen voor:" , gok)
    
    
    winnaar = 1
    if sum_gebruiker > sum_computer:
        winnaar = 2
    elif sum_gebruiker == sum_computer:
        winnaar = 0        
         
    print("Winnaar is " , winnaar)
    
    if winnaar == 2:
        print(bcolors.OKGREEN + "Gefeliciteerd! u heeft gewonnen! Uw punten:" , sum_gebruiker ,  " computer verliest met punten:" , sum_computer , bcolors.ENDC, "\n")
        wins_gebruiker = wins_gebruiker + 1        
    elif winnaar == 1: 
        print(bcolors.FAIL + "Jammer, u heeft verloren, De computer wint met punten:" , sum_computer , " u heeft " , sum_gebruiker , " punten",  bcolors.ENDC ,"\n")
        wins_computer = wins_computer + 1
    elif winnaar == 0: 
        print(bcolors.OKBLUE + "---- Gelijkspel ----- ", bcolors.ENDC ,"\n")
        wins_computer = wins_computer + 1
        wins_gebruiker = wins_gebruiker + 1
        
        
    laat_dobbelstenen(computer1, computer2, computer3, getal1, getal2, getal3)    
    
        
    time.sleep(SCHERM_TIMEOUT)
    os.system('cls' if os.name == 'nt' else 'clear')

#statistieken
