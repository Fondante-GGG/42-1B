



# class Cat:
#     def speak(self):
#         print("speak")

#     def sleep(self):
#         print("sleep")

# class Dog:
#     def speak(self):
#         print("speak")

#     def sleep(self):
#         print("sleep")

# class Cow:
#     def speak(self):
#         print("speak")

#     def sleep(self):
#         print("sleep")

# IS - A = Vehicle - Car

# class Animal:
#     def speak(self):
#         print("speak")
    
#     def sleep(self):
#         print("sleep")
        
# class Cat(Animal):
#     pass

# class Dog(Animal):
#     pass

# HAS - A = car -> engine 

# class Engine:
#     pass 

# class Car:  # Наследование
#     def __init__(self):
#         self.engine = Engine() # компазиция 

#         # CAR 
#         #     Engine 


# Animal -> Bird - Penguin 

# class Bird:
#     def fly(self):
#         print("fly")
# 
# class Penguin(Bird):
#     pass 
# 
# class Owl(Bird):
#     pass
# 
# o1 = Owl()
# o1.fly()

# class Animal:
#     pass
# 
# class Dog(Animal):
#     pass
# 
# print(Dog.__mro__)


# if isinstance(animal, Dog):
#     print("Это собака")
# elif isinstance(animal, Cat):
#     print("Это кошка")
# elif isinstance(animal, Owl):
#     print("Это сова")
# elif isinstance(animal, Animal):
#     print("Это животное")

# class Animal:
#     def speak(self):
#         pass
# 
# class Dog(Animal):
#     def speak(self):
#         print("Gav Gav")
# 
# class Cat(Animal):
#     def speak(self):
#         print("Meow Meow")
# 
# class Owl(Animal):
#     def speak(self):
#         print("Hoot Hoot")
# 
# class Mowse(Animal):
#     def speak(self):
#         print("Squeak Squeak")
# 
# def make_animal_speak(animal: Animal):
#     animal.speak()
# 
# make_animal_speak(Dog())
# make_animal_speak(Cat())
# make_animal_speak(Owl())
# make_animal_speak(Mowse())


# class Payment:
#     def __init__(self, amount):
#         self.amount = amount

#     def pay(self):
#         print(f"Опалата на сумму {self.amount} прошла успешно")

# class CardPayment(Payment):
#     def pay(self):
#         print(f"Опалата картой : {self.amount} прошла успешно")

# class CashPayment(Payment):
#     def pay(self):
#         print(f"Опалата наличными : {self.amount} прошла успешно")

# class QRPayment(Payment):
#     def pay(self):
#         print(f"Опалата QR : {self.amount} прошла успешно")

# def checkout(payment: Payment):
#     payment.pay()

# payments = [
#     CardPayment(100),
#     CashPayment(200),
#     QRPayment(500),
# ]

# for payment in payments:
#     checkout(payment)