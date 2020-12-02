f = open('report','r').readlines()

for l1 in f:
    for l2 in f:
        for l3 in f:
            if (int(l1)+int(l2)+int(l3)) == 2020:
                print(l1, l2, l3)
                print(int(l1)*int(l2)*int(l3))
                exit()
