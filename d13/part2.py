f = open('input','r').readlines()

schedule = [int(bus) if bus != "x" else 1 for bus in f[1].split(',')]

time = schedule[0]
factor = 1
for idx, bus in enumerate(schedule[1:]):
    while (time + idx + 1) % bus:
        time += factor * schedule[0]
    factor *= bus

print(time)
