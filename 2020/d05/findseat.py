import sys

oldseat = 0
for seat_id in sys.stdin:
    seat = int(seat_id, 2)
    if seat - oldseat == 2:
        print(seat-1)
        exit()
    oldseat = seat
