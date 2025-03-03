class Animal:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.weight} kg and {self.height} m"

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def walk(self):
        return f"{self.name} is walking."


class Cow(Animal):
    def __init__(self, name, height, weight, age, produced_milk):
        super().__init__(name, height, weight, age)
        self.produced_milk = produced_milk

    def produce_milk(self):
        return f"{self.name} produces {self.produced_milk} milk"


class Rabbit(Animal):
    def __init__(self, name, height, weight, age, kit):
        super().__init__(name, height, weight, age)
        self.kit = kit

    def no_kit(self):
        return f"{self.name} usually have {self.kit} kit"


class Hen(Animal):
    def __init__(self, name, height, weight, age, no_eggs):
        super().__init__(name, height, weight, age)
        self.egg == no_eggs

    def eggs(self):
        return f"{self.name} produces {self.eggs} eggs"