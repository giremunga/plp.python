
# Assignment: OOP Classes + Polymorphism in Python


#  Activity 1: Design Y Class 
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # percentage
    
    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery charged to {self.battery}%"

# Inheritance example
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        super().__init__(brand, model, battery)
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        return f"📸 Photo taken with {self.camera_megapixels}MP camera!"

#  Activity 2: Polymorphism Challenge 
class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        return "🐕 Running on four legs!"

class Bird(Animal):
    def move(self):
        return "🐦 Flying in the sky!"

class Fish(Animal):
    def move(self):
        return "🐟 Swimming in the water!"



# Testing the classes

# Activity 1 test
print("=== Activity 1: Smartphone Classes ===")
phone1 = Smartphone("Samsung", "A52", 50)
print(phone1.call("0712345678"))
print(phone1.charge(30))

pro_phone = SmartphonePro("iPhone", "15 Pro", 80, 48)
print(pro_phone.take_photo())
print(pro_phone.charge(25))

# Activity 2 test
print("\n=== Activity 2: Polymorphism with Animals ===")
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.move())
