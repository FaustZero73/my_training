import random

pole1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pole2 = []
n = (int(input("Введите число: ")))

def passport():
    kode = random.choice(pole1)
    return kode
    kode = passport()

def kode(n):
    sum_ = {}
    sum_.apdate({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
    10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
    14: 1611325212343114105968, 15: 1214114232133124115106978,
    16: 1317115262143531341251161079, 17: 11621531441351261171089,
    18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
    20: 13141911923282183731746416515614713812911})
    kode2 = sum_.get(n)
    return kode2

n = passport()
print('Код 1: ', n)

rang1 = list(range(1, n))
rang2 = list(range(1, n))
rangs = []
result = ''

for i in rang1:
    for j in rang2:
        if i >= j:
            continue
        else:
            sum_zn = n % (i + j)
            if sum_zn == 0:
                rangs.append([i, j])
                result = result + str(i) + str(j)
print('Код 2: ', *rangs)
print('Пароль: ', result)