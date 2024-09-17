print('Welcome to the calculator of rent of vehicle')

days = float(input('Enter the amount the days: '))
km = float(input('Enter the amount the km: '))

rate_days = 60
rate_km = 0.15

print(f'You will have what pay {(days * rate_days) + (km * rate_km)}')