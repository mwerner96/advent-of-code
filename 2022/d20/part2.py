original = [
    (idx, int(n) * 811589153) for idx, n in enumerate(open("input").read().splitlines())
]

decrypted = [n for n in original]

LEN = len(original)

for _ in range(10):
    for idx, n in original:
        old_idx = decrypted.index((idx, n))
        new_idx = (old_idx + n) % (LEN - 1)
        if (old_idx != new_idx) and (new_idx == 0):
            new_idx = LEN - 1
        decrypted.pop(old_idx)
        decrypted.insert(new_idx, (idx, n))

flat_decrypted = [n for _, n in decrypted]
idx_zero = flat_decrypted.index(0)

print(sum(flat_decrypted[(idx_zero + coord) % LEN] for coord in (1000, 2000, 3000)))
