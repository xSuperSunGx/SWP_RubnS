import random

dic = {}
def init():

    dic = {}
    for x in range(0,45):
        dic[x] = 0

def get_Statistics(zahl):
    dic[zahl] = dic[zahl]+1

def lotto():
    for x in range(0,45):
        dic[x+1] = 0
    for i in range(0,1000):
        r = random.randint(1, 45)
        get_Statistics(r)
    for i in dict(reversed(sorted(dic.items(), key=lambda item: item[1]))):
        print(f"{i} -> {dic[i]} mal")

if __name__ == '__main__':
    init()
    lotto()
