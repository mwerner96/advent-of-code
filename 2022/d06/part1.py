msg = open("input").read()

min_len = 4

idxs = [
    i + min_len
    for i, lst in enumerate(zip(*list(msg[j:] for j in range(min_len))))
    if len(set(lst)) == min_len
]

print(idxs[0])
