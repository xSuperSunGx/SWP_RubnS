import enum


class Firma():
    def __init__(self):
        self.abteilungen = []
    def get_abteilungen(self):
        return self.abteilungen
    def get_mitarbeiter(self):
        mitarbeiter = []
        for abteilung in self.abteilungen:
            mitarbeiter = mitarbeiter + abteilung.get_mitarbeiter()
        return mitarbeiter
    def get_gruppenleiter(self):
        gruppenleiter = []
        for abteilung in self.abteilungen:
            gruppenleiter.append(abteilung.get_gruppenleiter())
        return gruppenleiter
    def get_amount_mitarbeiter(self):
        return len(self.get_mitarbeiter())
    def get_amount_gruppenleiter(self):
        return len(self.get_gruppenleiter())
    def get_amount_abteilungen(self):
        return len(self.abteilungen)
    def get_max_amount_mitarbeiter(self):
        max_amount = 0
        max_abteilung = None
        for abteilung in self.abteilungen:
            if (abteilung.get_amount_mitarbeiter()+1) > max_amount:         # +1 for gruppenleiter
                max_amount = abteilung.get_amount_mitarbeiter() + 1         # +1 for gruppenleiter
                max_abteilung = abteilung
        return max_abteilung
    def get_percentage_person(self):
        frauen = 0
        maenner = 0
        insgesamt = 0
        mitarbeiter = self.get_mitarbeiter() + self.get_gruppenleiter()
        for mitarbeiter in mitarbeiter:
            if mitarbeiter.get_geschlecht() == Geschlecht.MAENNER:
                maenner = maenner + 1
            elif mitarbeiter.get_geschlecht() == Geschlecht.FRAUEN:
                frauen = frauen + 1
            insgesamt = insgesamt + 1
        return maenner/insgesamt, frauen/insgesamt

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)




class Geschlecht(enum.Enum):
    MAENNER = 1
    FRAUEN = 2
    NICHT_ANGEGEBEN = 3

class Person:

    def __init__(self, name, alter, geschlecht):
        self.geschlecht = geschlecht
        self.name = name
        self.alter = alter

    def get_name(self):
        return self.name
    def get_alter(self):
        return self.alter
    def get_geschlecht(self):
        return self.geschlecht




class Mitarbeiter(Person):
    def __init__(self, name, alter, geschlecht, abteilung):
        super().__init__(name, alter, geschlecht)
        self.abteilung = abteilung

    def get_abteilung(self):
        return self.abteilung

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.name + " " + self.abteilung.get_name() + " " + str(self.alter) + " " + str(self.geschlecht)


class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, alter, geschlecht, abteilung):
        super().__init__(name, alter, geschlecht, abteilung)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.name + " " + self.abteilung.get_name() + " " + str(self.alter) + " " + str(self.geschlecht) + " Gruppenleiter"


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.gruppenleiter = None

    def get_amount_mitarbeiter(self):
        return len(self.mitarbeiter)

    def get_mitarbeiter(self):
        return self.mitarbeiter

    def get_gruppenleiter(self):
        return self.gruppenleiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self

    def set_gruppenleiter(self, gruppenleiter):
        self.gruppenleiter = gruppenleiter
        gruppenleiter.abteilung = self

    def remove_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)
        mitarbeiter.abteilung = None

    def get_name(self):
        return self.name


def main_glatzl():
    firma = Firma()
    abteilung1 = Abteilung("IT")
    abteilung2 = Abteilung("Verkauf")
    abteilung3 = Abteilung("Marketing")
    firma.add_abteilung(abteilung1)
    firma.add_abteilung(abteilung2)
    firma.add_abteilung(abteilung3)
    mitarbeiter1 = Mitarbeiter("Max", 25, Geschlecht.MAENNER, abteilung1)
    mitarbeiter2 = Mitarbeiter("Noah", 18, Geschlecht.MAENNER, abteilung2)
    mitarbeiter3 = Mitarbeiter("Tebe", 18, Geschlecht.MAENNER, abteilung3)
    mitarbeiter4 = Mitarbeiter("Lena", 22, Geschlecht.MAENNER, abteilung3)
    abteilung1.add_mitarbeiter(mitarbeiter1)
    abteilung2.add_mitarbeiter(mitarbeiter2)
    abteilung3.add_mitarbeiter(mitarbeiter3)
    abteilung3.add_mitarbeiter(mitarbeiter4)
    gruppenleiter1 = Gruppenleiter("Peter", 45, Geschlecht.FRAUEN, abteilung1)
    gruppenleiter2 = Gruppenleiter("Lisa", 35, Geschlecht.FRAUEN, abteilung2)
    gruppenleiter3 = Gruppenleiter("Hans", 50, Geschlecht.FRAUEN, abteilung3)
    abteilung1.set_gruppenleiter(gruppenleiter1)
    abteilung2.set_gruppenleiter(gruppenleiter2)
    abteilung3.set_gruppenleiter(gruppenleiter3)

    print("Anzahl der Mitarbeiter: ", firma.get_amount_mitarbeiter())
    print("Anzahl der Gruppenleiter: ", firma.get_amount_gruppenleiter())
    print("Anzahl der Abteilungen: ", firma.get_amount_abteilungen())
    print("Maximale Anzahl an Mitarbeitern: ", firma.get_max_amount_mitarbeiter().get_name())
    print("Prozent der Männer: ", firma.get_prozent_person()[0])
    print("Prozent der Frauen: ", firma.get_prozent_person()[1])
    print("Mitarbeiter in Abteilung 1: ", abteilung1.get_mitarbeiter())
    print("Mitarbeiter in Abteilung 2: ", abteilung2.get_mitarbeiter())
    print("Mitarbeiter in Abteilung 3: ", abteilung3.get_mitarbeiter())

if __name__ == '__main__':
    main_glatzl()
