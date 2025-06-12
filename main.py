class Backpack:
    def __init__(self):
        self.pojemnosc = None
        self.ilosc_przedmiotow = None
        self.wagi = None
        self.wartosci = None
    
    def __str__(self):
        string = f"Pojemnosc: {self.pojemnosc}\nIlość przedmiotów: {self.ilosc_przedmiotow}"
        for i in range(self.ilosc_przedmiotow):
            temp = f"\nWaga: {self.wagi[i]}\tWartość: {self.wartosci[i]}"
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

Frontpack = Backpack()
Frontpack.read_data("data.txt")
print(Frontpack)