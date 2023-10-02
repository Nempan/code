n = int(input("Ange ett heltal: "))
summa = 0

for i in range(1,n + 1):
    kvadrat = i**2
    summa += kvadrat

print("Summan av kvadraterna från 1 till", n, "är", summa)