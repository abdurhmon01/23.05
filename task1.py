class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def bark(self):
        print(f"{self.name} says: wow wow")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age}")
        print("Tricks:")
        for trick in self.tricks:
            print(f"{trick}")
my_dog=Dog(name="bobik",breed="pitbul",age="1_yera")
my_dog.add_trick("salto")
my_dog.bark()
my_dog.display_info()
