import random

print("Spelaren börjar.")

spelarvärde = 0
dice = random.randint(1,6)
dicecount = 0

while dicecount < 4:
    dicecount += 1
    spelarvärde += dice
    print("Du har fått", spelarvärde, "poäng", ". runda:", dicecount)
    

    if spelarvärde == 14:
        print("Du har vunnit!")
        break

    elif dicecount <4:
        print("Vill du slå igen")
        svar = input("Ja eller Nej: ")
        if svar == "Ja":
            dice = random.randint(1,6)
            spelarvärde += dice
            print("Du har fått", spelarvärde, "poäng")
        elif svar == "Nej":
            print("Du har stannat på", spelarvärde, "poäng")
            break
    