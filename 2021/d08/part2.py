from pprint import pprint
with open('input') as f:
    patterns = [(line.split()[:10], line.split()[-4:]) for line in f.readlines()]

sum = 0
for pattern in patterns:
    # build luts
    lut = {frozenset(s): [] for s in pattern[0]}
    back_lut = [[] for _ in range(0, 10)]
    for key in lut:
        len_dig = {
            2: [1],
            3: [7],
            4: [4],
            5: [2, 3, 5],
            6: [0, 6, 9],
            7: [8]
        }
        lut[key] = len_dig[len(key)]
        for idx in len_dig[len(key)]:
            back_lut[idx].append(key)
    # 1, 4, 7, 8 are done
    # find 3
    for poss in back_lut[3]:
        if back_lut[1][0] < poss:
            back_lut[3] = [poss]
            back_lut[2].remove(poss)
            back_lut[5].remove(poss)
            lut[poss] = [3]
            break
    # 1, 3, 4, 7, 8 are done
    # find 6
    for poss in back_lut[6]:
        if not back_lut[1][0] < poss:
            back_lut[6] = [poss]
            back_lut[0].remove(poss)
            back_lut[9].remove(poss)
            lut[poss] = [6]
            break
    # 1, 3, 4, 6, 7, 8 are done
    # find 0 and 9
    for poss in back_lut[0]:
        if not back_lut[4][0] < poss:
            back_lut[0] = [poss]
            back_lut[9].remove(poss)
            lut[poss] = [0]
            lut[back_lut[9][0]] = [9]
            break
    # 0, 1, 3, 4, 6, 7, 8, 9 are done
    # find 2 and 5
    for poss in back_lut[5]:
        if poss < back_lut[6][0]:
            back_lut[5] = [poss]
            back_lut[2].remove(poss)
            lut[poss] = [5]
            lut[back_lut[2][0]] = [2]
            break
    # lut is done
    lut = {key: val[0] for key, val in lut.items()}
    sum += lut[frozenset(pattern[1][0])] * 1000
    sum += lut[frozenset(pattern[1][1])] * 100
    sum += lut[frozenset(pattern[1][2])] * 10
    sum += lut[frozenset(pattern[1][3])] * 1

print(sum)
