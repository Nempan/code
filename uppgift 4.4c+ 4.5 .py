studs = 0
print("För att avsluta skriv ett tal som är <= 0")
while True:
    
    boll = float(input("Ange hur högt bollen släps ifrån i meter: ")) 
    while boll > 0.01:
        boll = boll * 0.7
        studs = studs + 1
    print(f"Antalet studs från höjden du valt blev {studs}")

    if boll <= 0:
        break
    
    


