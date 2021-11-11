import math

f = open('input','r').readlines()

earliest_departure = int(f[0])
schedule = [int(bus) for bus in f[1].split(',') if bus != "x"]

waittime = -1
best_bus = -1
for bus in schedule:
    thiswait = bus * math.ceil(earliest_departure / bus) - earliest_departure
    if waittime == -1:
        waittime = thiswait
    if thiswait < waittime:
        waittime = thiswait
        best_bus = bus

print(waittime * best_bus)
