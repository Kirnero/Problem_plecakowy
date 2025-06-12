class Backpack:
    def __init__(self):
        self.pojemnosc = None
        self.ilosc_przedmiotow = None
        self.wagi = None
        self.wartosci = None
    
    def __str__(self):
        string = f"Pojemnosc: {self.pojemnosc}\nIlość przedmiotów: {self.ilosc_przedmiotow}"
        for i in range(self.ilosc_przedmiotow):
            temp = f"\nNr.{i+1}\tWaga: {self.wagi[i]}\tWartość: {self.wartosci[i]}"
            string += temp
        return string

    
    def read_data(self, file_name):
        file = open(file_name)
        if file == None:
            return
        self.pojemnosc = int(file.readline())
        self.ilosc_przedmiotow = int(file.readline())
        self.wagi=[]
        self.wartosci=[]
        for i in range(self.ilosc_przedmiotow):
            data = file.readline().split()
            self.wagi.append(int(data[0]))
            self.wartosci.append(int(data[1]))
        file.close()

def bruteforce(Frontpack):
    max_value = 0
    best_combination = 0
    for i in range(1 << Frontpack.ilosc_przedmiotow):
        current_weight = 0
        current_value = 0
        for j in range(Frontpack.ilosc_przedmiotow):
            if (i & (1 << j)): # If the j-th item is included
                current_weight += Frontpack.wagi[j]
                current_value += Frontpack.wartosci[j]
        if current_weight <= Frontpack.pojemnosc :
            max_value = max(max_value, current_value)
            if (max_value == current_value):
                best_combination = i

    print("Maksymalna wartosc: ", max_value)
    print("Wybrane przedmioty: ", end="")
    selected=[]
    for i in range(0, Frontpack.ilosc_przedmiotow):
        if (best_combination & (1 << i)):
            print(i+1, "", end="")
            selected.append(i)
    print()
    selected.reverse()
    return selected

def dynamic(Frontpack):
    tab=[[0]]*(Frontpack.ilosc_przedmiotow+1)
    for i in range(Frontpack.ilosc_przedmiotow+1):
        tab[i] = [0]*(Frontpack.pojemnosc+1)

    for i in range(1, Frontpack.ilosc_przedmiotow+1):
        for j in range(Frontpack.pojemnosc+1):
            if Frontpack.wagi[i-1] <= j:
                tab[i][j] = max(tab[i-1][j], tab[i-1][j-Frontpack.wagi[i-1]] + Frontpack.wartosci[i-1])
            else:
                tab[i][j] = tab[i-1][j]
    
    print(f"Maksymalna wartość: {tab[Frontpack.ilosc_przedmiotow][Frontpack.pojemnosc]}")

    selected = []
    temp = Frontpack.pojemnosc
    for i in range(Frontpack.ilosc_przedmiotow, 0, -1):
        if tab[i][temp] != tab[i-1][temp]:
            selected.append(i-1)
            temp-=Frontpack.wagi[i-1]
    selected.reverse()
    print("Wybrane przedmioty: ", end="")
    for item in selected: print(item+1, end=" ")
    print()
    return selected


Frontpack = Backpack()
Frontpack.read_data("data.txt")
print(Frontpack)
bruteforce(Frontpack)