gym = int(input("Hur många dagar ska du gymma? "))
pris1 = 70
pris2 = gym * pris1
if pris2 > 1800:
    print("Vill du köpa ett årskort som är billiagare för anatl dagar du ska gymma vilekt är 2700kr för ett år")
elif pris2 < 1800:
    print("Din totala summa är", pris2)


