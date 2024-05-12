from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=8000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}
        self.foglalasok = {}

    def add_szoba(self, szoba):
        self.szobak[szoba.szobaszam] = szoba

    def foglal(self, szobaszam, datum):
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d")
            formazott_datum = datum_obj.strftime('%Y-%m-%d')
        except ValueError:
            return "Hibás dátum formátum."

        foglalas_key = f"{szobaszam}_{formazott_datum}"
        if foglalas_key in self.foglalasok:
            return "A szoba már foglalt ekkor."

        if szobaszam in self.szobak:
            self.foglalasok[foglalas_key] = self.szobak[szobaszam].ar
            return f"A foglalás megerősítve a(z) {formazott_datum}-i dátumra {self.szobak[szobaszam].ar} Ft-ért."
        return "Hibás szobaszám."

    def lemondas(self, szobaszam, datum):
        foglalas_key = f"{szobaszam}_{datum}"
        if foglalas_key in self.foglalasok:
            del self.foglalasok[foglalas_key]
            return "A foglalás sikeresen törölve."
        return "Nincs ilyen foglalás."

    def listaz(self):
        if self.foglalasok:
            return "\n".join([f"Szoba: {foglalas.split('_')[0]}, Dátum: {foglalas.split('_')[1]}, Ár: {self.foglalasok[foglalas]} Ft" for foglalas in self.foglalasok])
        else:
            return "Nincs foglalás."

def create_sample_hotel():
    hotel = Szalloda("Szálloda")
    hotel.add_szoba(EgyagyasSzoba("101"))
    hotel.add_szoba(EgyagyasSzoba("102"))
    hotel.add_szoba(KetagyasSzoba("201"))
    hotel.add_szoba(KetagyasSzoba("202"))
    hotel.add_szoba(KetagyasSzoba("203"))
    return hotel

def main():
    hotel = create_sample_hotel()

    for _ in range(5):
        tomorrow = datetime.now() + timedelta(days=1)
        datum = tomorrow.strftime('%Y-%m-%d')
        print(datum)
        hotel.foglal("101", datum)
        hotel.foglal("201", datum)
        tomorrow += timedelta(days=1)

    print("Üdvözöljük a Példa Szállodában!")
    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Választott művelet: ")

        if choice == "1":
            try:
                szobaszam = input("Adja meg a foglalandó szoba számát: ")
                datum = input("Adja meg a foglalni kívánt időpontot (YYYY-MM-DD): ")
                print(hotel.foglal(szobaszam, datum))
            except ValueError as e:
                print(f"Hiba: {e}")
        elif choice == "2":
            try:
                szobaszam = input("Adja meg a lemondandó szoba számát: ")
                datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
                print(hotel.lemondas(szobaszam, datum))
            except ValueError as e:
                print(f"Hiba: {e}")
        elif choice == "3":
            try:
                print(hotel.listaz())
            except ValueError as e:
                print(f"Hiba: {e}")
        elif choice == "4":
            try:
                print("Köszönjük, hogy minket választott!")
                break
            except ValueError as e:
                print(f"Hiba: {e}")
        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")

if __name__ == "__main__":
    main()