import random

zahlen = []
def lotto():
    ret = []
    for i in range(0,45):
        zahlen.append(i+1)
    print(f"Zahlen verfügbar: {zahlen}")
    for i in range(0,6):
        r = random.randint(1, 45)
        for x in range(len(zahlen)+1):
            if zahlen[x] is r:
                zahlen[x] = zahlen[-1]
                del zahlen[-1]
                ret.append(r)
                break

    print(f"Zahlen verfügbar: {zahlen}")
    print(f"Lottozahlen: {ret}")
    return ret

if __name__ == '__main__':
    lotto()
