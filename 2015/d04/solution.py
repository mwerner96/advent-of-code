import hashlib

with open('input') as f:
    input = f.readline().splitlines()[0]

# part 1
num = 0
hash = ''
while not hash.startswith('00000'):
    num += 1
    to_hash = input + str(num)
    hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()

print(num)

# part 2
num = 0
hash = ''
while not hash.startswith('000000'):
    num += 1
    to_hash = input + str(num)
    hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()

print(num)
