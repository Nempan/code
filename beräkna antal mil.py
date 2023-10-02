# Miltals kalkyl


def drar():
    while True:
        förbruk = input('Hur mycket förbrukar din bil per mil? ')
        try:
            förbruk = float(förbruk)
            if förbruk > 0 and förbruk < 4:
                break
            else:
                print("Tror att din bil är trasig. Fixa den sen kommer du tillbaka för den ska inte dra så mycket.")
        except ValueError:
            print("Du måste välja ett nummer mer än 0.")
    return förbruk

def mil_idag():
    while True:
        idag = input('Mätarställning i dag?')
        if idag.isdigit():
            idag = float(idag)
            if idag > 0:
                break
            else:
                print("Har du verkligen aldrig kört din bil? Välj någon du kört med helst.")
        else:
            print("Du måste välja ett nummer mer än 0.")
    return idag


def mil_förut():
    while True:
        tidigare = input('Mätarsätllning för ett år sedan?')
        if tidigare.isdigit():
            tidigare = float(tidigare)
            if tidigare > 0:
                break
            else:
                print("Om du kört 0 mil bör du veta hur lånt du kört efter.")
        else:
            print("Du måste välja ett nummer mer än 0.")
    return tidigare




 

def main():
    mil1 = mil_förut()
    mil2 = mil_idag()
    mil3 = mil2 - mil1
    drag = drar()
    print("------------------------------------------")
    print("Mätarställning idag är:", mil2)
    print("Mätarställningar förut var:", mil1)
    print('Antalet mil du kört är', mil3)
    print("Antal liter bensin dragits:", mil3 * drag)
        



main()