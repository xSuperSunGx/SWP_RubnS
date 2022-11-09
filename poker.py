import random

cards = []
stats = {}
def init():
    cards.clear()
    for i in range(52):
        cards.append(i)

def checkPair(list):
    for i in range(len(list)):
        list[i] = list[i] % 13
    used = set()
    erg = []
    for i in list:
        if i in used:
            erg.append(i)
            used.remove(i)
        else:
            used.add(i)
    return erg
def checkDripple(list):
    for i in range(len(list)):
        list[i] = list[i] % 13
    used = {}
    erg = []
    for i in list:
        if i in used:
            if used[i] == 1:
                used[i] = 2
            elif used[i] == 2:
                del used[i]
                erg.append(i)
        else:
            used[i] = 1
    return erg
def checkStraight(list):
    for i in range(len(list)):
        list[i] = list[i] % 13
    erg = 0
    number_of_cards_in_row = 0
    last_number = 0

    for i in sorted(list):
        if last_number == i-1:
            number_of_cards_in_row = number_of_cards_in_row+1
            if number_of_cards_in_row == 5:
                erg = erg+1
                number_of_cards_in_row = 0
        else:
            number_of_cards_in_row = 0

        last_number = i


def generateCrads(amount):
    l = []
    for i in range(amount):
        a = random.randint(0,52)
        while a not in l:
            l.append(a)
    return l
def defCard():
    number_of_cards = 7
    gen_cards = generateCrads(number_of_cards)
    c = 0
    for i in range(int(number_of_cards/2)):
        c = i+1
        if len(checkPair(gen_cards)) == c:
            if f"{c}-Pair" in stats:
                stats[f"{c}-Pair"] = stats[f"{c}-Pair"]+1
            else:
                stats[f"{c}-Pair"] = 1
    for i in range(int(number_of_cards/3)):
        c = i+1
        if len(checkDripple(gen_cards)) == c:
            if f"{c}-Dripple" in stats:
                stats[f"{c}-Dripple"] = stats[f"{c}-Dripple"]+1
            else:
                stats[f"{c}-Dripple"] = 1
    for i in range(int(number_of_cards/5)):
        c = i+1
        if checkStraight(gen_cards) == c:
            if f"{c}-Straight" in stats:
                stats[f"{c}-Straight"] = stats[f"{c}-Straight"]+1
            else:
                stats[f"{c}-Straight"] = 1



def glatzl():
    init()

    for i in range(0,1000000):
        defCard()
    print(stats)

if __name__ == '__main__':
    glatzl()
