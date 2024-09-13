import random
import time

print("Spelaren börjar.")
time.sleep(1)

målvärde = 14

spelarvärde1 = 0
dator = 0
dicecount = 0
dicecountdator = 0
svar = ""

dice1 = random.randint(1,6)

dice2 = random.randint(1,6)

dice3 = dice1 + dice2 

spelarvärde1 = dice3 + spelarvärde1

while dicecount < 4:
    if spelarvärde1 > 14:
                break
    if svar == "Nej":
        break
    if dicecount >= 3:
        break
    dice = random.randint(1,6)
    dicecount += 1
    print("Du har fått", spelarvärde1, "poäng", ". runda:", dicecount)
    
    while dicecount > 0 & dicecount < 3:
        if spelarvärde1 > 14:
                print("Du förlorade!")
                time.sleep(3)
                exit()
        if spelarvärde1 > 14:
                break
        if svar == "Nej":
            break
        if dicecount >= 3:
            print("Datorns tur!")
            break
        if spelarvärde1 == 14:
            print("Du har vunnit!")
            break
        while dicecount < 3:
             if spelarvärde1 > 14:
                  break
             if spelarvärde1 == 14:
                  break
             print("Vill du slå igen")
             svar = input("Ja eller Nej: ")
             if svar == "Ja":
                time.sleep(2)
                dice = random.randint(1,6)
                spelarvärde1 += dice
                dicecount += 1
                print("Du har fått", spelarvärde1, "poäng")
             elif svar == "Nej":
                print("Du har stannat på", spelarvärde1, "poäng")
                break


time.sleep(2)
print("Datorn börjar")

while dicecountdator < 4:
    if dator > 10 and dator < 14:
         break
    if dator > 14:
        print("Du vann!")
        break
    dice4 = random.randint(1,6)
    if dator == 14:
        print("Datorn har vunnit!")
        break
    dicecountdator += 1
    while dator < 10 and dicecountdator < 4:
         dice4 = random.randint(1,6)
         dator += dice4
         print("Datorn har fått", dator, "poäng")
         if dator > 14:
            break

spelardiff = abs(spelarvärde1 - målvärde)

datordiff = abs(dator - målvärde)

if spelardiff < datordiff:
    print("Du vann!")
    
elif spelardiff > datordiff:
    print("Datorn vann!")




