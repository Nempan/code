import math
x1 = float(input("Ange x-koordinaten för punkt 1: "))
y1 = float(input("Ange y-koordinaten för punkt 1: "))

x2 = float(input("Ange x-koordinaten för punkt 2: "))
y2 = float(input("Ange y-koordinaten för punkt 2: "))

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print("Avståndet mellan punkt 1 och punkt 2 är:", distance)
