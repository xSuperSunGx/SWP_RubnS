import random
import webbrowser

import requests


class TypeGen:


    def __init__(self):
        self.big_ben = ['Stein', 'Schere', 'Papier', 'Echse', 'Spock']
        self.input = ''
        self.coop = ''

    def generate_random(self):
        self.coop = self.big_ben[random.randint(0, len(self.big_ben))]
    def change_input(self, input):
        self.input = input

    def get_big_ben(self):
        return self.big_ben
    #Return: is_player_winner, equal
    def is_player_winner(self):
        if self.input != '':
            pc = self.big_ben.index(self.coop)
            player = self.big_ben.index(self.input)
            if player == 0: # Stein
                if pc == 0:
                    return False, True
                elif pc == 1:
                    return True, False
                elif pc == 2:
                    return False, False
                elif pc == 3:
                    return True, False
                elif pc == 4:
                    return False, False
            elif player == 1: # Schere
                if pc == 0:
                    return False, False
                elif pc == 1:
                    return False, True
                elif pc == 2:
                    return True, False
                elif pc == 3:
                    return True, False
                elif pc == 4:
                    return False, False
            elif player == 2: # Papier
                if pc == 0:
                    return True, False
                elif pc == 1:
                    return False, False
                elif pc == 2:
                    return False, True
                elif pc == 3:
                    return False, False
                elif pc == 4:
                    return True, False
            elif player == 3: # Echse
                if pc == 0:
                    return False, False
                elif pc == 1:
                    return False, False
                elif pc == 2:
                    return True, False
                elif pc == 3:
                    return False, True
                elif pc == 4:
                    return True, False
            elif player == 4:
                if pc == 0:
                    return True, False
                elif pc == 1:
                    return True, False
                elif pc == 2:
                    return False, False
                elif pc == 3:
                    return False, False
                elif pc == 4:
                    return False, True

typegen = TypeGen()






def get_type_input():
    print(f"Wählen sie einen Typ aus: ")
    for i in range(len(typegen.get_big_ben())):
        print(f"({i+1}) -> {typegen.get_big_ben()[i]}")
    return input()
    new_line(1)

def start():
    new_line(5)
    new_minus_line()
    print(f"{new_space(20)}Herzlich Willkommen beim Spiel")
    print(f"{new_space(18)}Stein, Papier, Schere, Echse, Spock")
    new_minus_line()
    new_line(2)
    print(f"Möchten Sie die Spielregeln öffnen? (Y/N)")
    answer = input()
    if answer == "Y" or answer == "y":
        webbrowser.open_new_tab("http://localhost:5050/")
    new_line(30)
    answer = get_type_input()
    typegen.generate_random()
    typegen.change_input(typegen.get_big_ben()[int(answer)-1])
    winner, equal = typegen.is_player_winner()
    print(f"PC: {typegen.coop}")
    print(f"DU: {typegen.input}")
    new_line(1)

    if equal:
        print(f"{new_space(4)}!!!!! GLEICHSTAND !!!!!")

    return winner, equal



def new_line(index):
    for i in range(index):
        print("")

def new_space(index):
    str = ""
    for i in range(index):
        str = str + " "
    return str

def new_minus_line():
    print("-"*50)

def main():
    winner, equal = start()
    while not winner:
        if not equal:
            print(f"{new_space(4)}VERLOREN!!!!!")
        else:
            print(f"{new_space(4)}GLEICHSTAND !!!!!")
        winner, equal = start()
    print(f"{new_space(4)}GEWINNER!!!!!")

def upload_statistics(replace, file):
    url = "http://localhost:5000/upload"
    files = {'file': open(file, 'rb')}
    data = {'replace': replace}
    r = requests.post(url, files=files, params=data)
    print(r.text)


if __name__ == '__main__':
    upload_statistics(True, 'requirements.txt')
