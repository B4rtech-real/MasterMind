import random

def randomSelection():
    n = []
    i = 0
    while i < 5:
        i += 1
        n.append(random.randrange(1, 10))
    return n

def input_check():
    while True:
        try:
            number = int(input("Wybierz liczbę od 1 do 9: "))
            if number in range(1, 10):
                return number
            else:
                print("Podana liczba jest poza zakresem. Spróbuj jeszcze raz.")
        except ValueError:
            print("To nie jest liczba. Spróbuj jeszcze raz.")
