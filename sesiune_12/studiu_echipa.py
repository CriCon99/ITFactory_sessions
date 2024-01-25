from datetime import date


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(self.nume, self.prenume, self.salariu)

    def nume_complet(self):
        print(self.nume, self.prenume)

    def salariu_lunar(self):
        print(self.salariu)

    def salariu_anual(self):
        print(self.salariu * 12)

    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu * procent / 100)


angajat1 = Angajat("Popescu", "Ion", 5000)
angajat1.marire_salariu(10)
angajat1.salariu_lunar()
angajat1.salariu_anual()


class Factura:
    seria = 'XM'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        data = date.today().strftime("%d-%m-%Y")
        total = self.pret_buc * self.cantitate
        print(f'Factura seria {self.seria} numar {self.numar}')
        print(f"Data: {data}")
        print("Produs    | Cantitate | Pret bucata | Total")
        print(f"{self.nume_produs}   |      {self.cantitate}    |     {self.pret_buc}     |  {total}")


factura = Factura(4250, 'Iphone', 2, 5500)
factura.genereaza_factura()
