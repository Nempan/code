import random
import time

print("Spelaren börjar.")

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
                print("Du förlorade!")
                break
            print("Vill du slå igen")
            svar = input("Ja eller Nej: ")
            if svar == "Ja":
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
    if dator == 14:
        print("Datorn har vunnit!")
        break
    dicecountdator += 1



