class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, new_floor + 1):
            if new_floor < 1 or new_floor > self.numbers_of_floors:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Названеие: {self.name}, кол-во этажей: {self.numbers_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
