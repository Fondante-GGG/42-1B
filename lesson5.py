


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Привет! Меня зовут {self.name} и мне {self.age} лет.")

#     def have_birthday(self):
#         self.age += 1
#         print(f"С днем рождения! Теперь мне {self.age} лет.")


# u1 = User("Алексей", 25)
# u1.greet()

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)

#     def __eq__(self, other): 
#         if isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         return False

#     def __len__(self):
#         return int((self.x ** 2 + self.y ** 2) ** 0.5)

# v1 = Vector(3, 4)
# v2 = Vector(1, 2)

# print(v1)

# v3 = v1 + v2
# print(v3)
# print(len(v1))
# print(v1 == v2)


# class User:
#     role_default = "quest"
# 
#     def __init__(self, name: str, age :int):
#         self.name = name
#         self.age = age
# 
#     @classmethod    
#     def from_string(cls, user_str : str):
#         name, age = user_str.split(",")
#         return cls(name, int(age))
# 
#     @classmethod
#     def set_default_role(cls, new_role: str):
#         cls.role_default = new_role
# 
# u1 = User("Алексей", 25)
# u2 = User.from_string("Bob,25")
# print(u2.name, u2.age)
# 
# User.set_default_role("admin")
# print(u1.role_default, u2.role_default)

class DateValidator:
    def __init__(self, day, month, year):
        if not self.is_valid_date(day, month, year):
            raise ValueError("Некорректная дата")
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_valid_date(day, month, year):
        if year < 1 or not (1 <= month <=12):
            return False
        if not (1 <= day <= 31):
            return False
        return True

print(DateValidator.is_valid_date(32, 12, 2020))  

print(DateValidator.mro())

class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        print("Start B")
        super().action()
        print("End B")

class C(A):
    def action(self):
        print("Start C")
        super().action()
        print("End C")

class D(B, C):
    def action(self):
        print("Start D")
        super().action()
        print("End D") 

# D > C > B > A == Камбар 
# D > C, B - C > A, B > A = Байтур 
# A > B A > C A > A B C D = Орозбек байке 
# 

print(D.mro())