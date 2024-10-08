seats = [[0 for _ in range (8)] for _ in range(5)]

def reserve_seat(seats, row, seat):
    if 0 <= row < len(seats) and 0 <= seat < len(seats[0]):
        if seats[row][seat] == 0:
            seats[row][seat] = 1
            print(f'seat ({row + 1}, {seat + 1}) reserved with success.')
        else:
            print(f'seat ({row + 1}, {seat + 1}) will be reserved.')
    else:
        print('seat invalid')

def cancel_reserve(seats, row, seat):
    if 0 <= row < len(seats) and 0 <= seat < len(seats[0]):
        if seats[row][seat] == 1:
            seats[row][seat] = 0
            print(f'reserve do seat ({row + 1}, {seat + 1}) cancel with success')
        else:
            print(f'seat ({row + 1}, {seat + 1}) not will be reserved.')
    else:
        print('seat invalid.')

def read_map_seats(seats):
    print('map seats:')
    for i, row in enumerate(seats):
        print(f'row {i + 1}: ' + ' '.join(str(seat) for seat in row)) 