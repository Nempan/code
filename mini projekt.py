# Quiz game

print("Välkommen till mitt quiz!")

playing = input("Vill du spela? N/Y? ")

if playing != "Y":
    quit()

print("Okej! Då kör vi :)")

answer = input(" Vad står CPU för?")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Fel svar!")

