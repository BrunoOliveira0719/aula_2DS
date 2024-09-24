class car:
    def __init__(self, mark, model, color, value, year):
        self.mark = mark 
        self.model = model
        self.color = color
        self.year = year
        self.value = value

class storage(car):
    def __init__(self):
        self.cars = []
    
    def create(self, car):
        self.cars.append(car)
        
    def read(self):
        for car in self.cars:
            print(f"{car.model},{car.mark}")
        
car_1 = car('car1','123','blue',3212000000,'1975')
car_2 = car('car2','321','red',4254367000,'2025')

storage = storage()

storage.create(car_1)
storage.create(car_2)
storage.read()