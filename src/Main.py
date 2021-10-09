
import random
import datetime


def convertOne(num):
    num = str(num)
    list_num = []
    for n in num:
        n = int(n)
        list_num.append(n)

    reference = {0: "F", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M",
                 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: "a", 28: "b", 29: "c", 30: "d", 31: "e", 32: "f", 33: "g", 34: "h", 35: "i", 36: "j", 37: "k", 38: "l", 39: "m",
                 40: "n", 41: "o", 42: "p", 43: "q", 44: "r", 45: "s", 46: "t", 47: "u", 48: "v", 49: "w", 50: "x", 51: "y", 52: "z", 53: "#", 54: "$", 55: "@", 56: "0", 57: "1", 58: "2", 59: "3", 60: "4", 61: "5", 62: "6", 63: "7", 64: "8", 65: "9"}

    xd = ""
    ran = len(list_num)
    for i in range(0, ran, 2):
        if int(list_num[i]) > 6:
            list_num[i] -= 3
        try:
            if int(list_num[i+1]) > 5 and int(list_num[i]) >= 6:
                list_num[i+1] -= 5
        except:
            list_num.append("0")
        if (len(xd) < 32):
            pre = int(str(list_num[i])+str(list_num[i+1]))
            xd = xd+reference[pre]
        random.seed(pre)
        if (i > 1):
            for i in range(0, 3):
                op = int(random.random()*100)
                if op > 65:
                    op -= 35
                if (len(xd) < 32):
                    xd = xd+reference[op]
    return xd


def convertTwo(text):
    reference = {"F": "00", "A": "01",  "B": "02",  "C": "03", "D": "04", "E": "05", "F": "06", "G": "07",  "H": "08",  "I": "09",  "J": 10,  "K": 11,  "L": 12,  "M": 13, "N": 14,  "O": 15,  "P": 16,  "Q": 17,  "R": 18,  "S": 19,  "T": 20,  "U": 21,  "V": 22,  "W": 23,  "X": 24,  "Y": 25,  "Z": 26,
                 "a": 27,  "b": 28,  "c": 29,  "d": 30,  "e": 31,  "f": 32,  "g": 33,  "h": 34,  "i": 35,  "j": 36,  "k": 37,  "l": 38,  "m": 39,  "n": 40,  "o": 41,  "p": 42,  "q": 43,  "r": 44,  "s": 45,  "t": 46,  "u": 47,  "v": 48,  "w": 49,  "x": 50,  "y": 51,  "z": 52,  "#": 53,  "$": 54,  "@": 55,  "0": 56,  "1": 57,  "2": 58,  "3": 59,  "4": 60,  "5": 61,  "6": 62,  "7": 63,  "8": 64,  "9": 65}
    r = ""
    for char in text:
        r = r+str(reference[char])
    return r


def first():
    current_time = datetime.datetime.now()
    date = int(str(current_time.year)+str(current_time.month)+str(current_time.day)+str(current_time.hour) +
               str(current_time.minute)+str(current_time.second) +
               str(current_time.microsecond))
    gen = random.random()
    gen = int(gen*10000)
    random.seed(gen)
    mul = 0
    while mul == 0:
        mul = int(random.random()*100)
    seedN = mul*date
    data = convertOne(seedN)

    with open('data.txt', 'w') as f:
        f.write(data)


def Basic(pag, contr):
    with open('data.txt', 'r') as f:
        data = f.read()
    Bseed = int(convertTwo(data))
    pagi = int(convertTwo(pag))
    contri = int(convertTwo(contr))
    fin = pagi*contri+Bseed
    random.seed(fin)
    gen = int(random.random()*10**64)
    return convertOne(gen)


def verify():
    try:
        file = open('data.txt')
        file.close()
    except FileNotFoundError:
        first()
        exit()
