storage = [20, 15, 10, 30, 5]

def get_product(storage, product, amount):
    if 0 <= product < len(storage):
        if storage[product] >= amount:
            storage[product] -= amount

        else:
            print(f'Insufficient product. {product + 1}° product')

    else:
        print('Invalid product')

def add_in_storage(storage, product, amount):
    if 0 <= product < len(storage):
        storage[product] += amount
    else:
        print('Invalid product')
        
def read_storage(storage):
    for i, amount in enumerate(storage):
        print(f'product: {i + 1}°\n amount: {amount}')

get_product(storage, 4, 5)

read_storage(storage)

add_in_storage(storage, 4, 10)

read_storage(storage)