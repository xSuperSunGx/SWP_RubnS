import enum


class Firma() :
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
            gruppenleiter = gruppenleiter + abteilung.get_gruppenleiter()
        return gruppenleiter
    def get_amount_abteilungen(self):
        return len(self.abteilungen)
    def get_max_amount_mitarbeiter(self):
        max_amount = 0
        max_abteilung = None
        for abteilung in self.abteilungen:
            if abteilung.get_amount_mitarbeiter() > max_amount:
                max_amount = abteilung.get_amount_mitarbeiter()
                max_abteilung = abteilung
        return max_abteilung
    def get_prozent_person(self):
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






class Geschlecht(enum.Enum):
    MAENNLICH = 1
    WEIBLICH = 2
    NICHT_ANGEGEBEN = 3

class Person:

    def __init__(self, name, alter, geschlecht):
        self.geschlecht = Geschlecht.NICHT_ANGEGEBEN
        self.name = ''
        self.alter = 0

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





class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, alter, geschlecht, abteilung):
        super().__init__(name, alter, geschlecht, abteilung)

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.gruppenleiter = []

    def get_amount_mitarbeiter(self):
        return len(self.mitarbeiter)
    def get_amount_gruppenleiter(self):
        return len(self.gruppenleiter)

    def get_mitarbeiter(self):
        return self.mitarbeiter

    def get_gruppenleiter(self):
        return self.gruppenleiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self

    def add_gruppenleiter(self, gruppenleiter):
        self.gruppenleiter.append(gruppenleiter)
        gruppenleiter.abteilung = self

    def remove_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)
        mitarbeiter.abteilung = None

    def remove_gruppenleiter(self, gruppenleiter):
        self.gruppenleiter.remove(gruppenleiter)
        gruppenleiter.abteilung = None
    def get_name(self):
        return self.name