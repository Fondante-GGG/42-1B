


# def hello():
#     print("Hello, World!")

# hello()


# def heello(name, age):
#     print("Hello, " + name + "! You are " + str(age) + " years old.")

# print(heello("Alice", 25))


# class Student:
#     def __init__(self):
#         self.name = "Bob"
#         self.age = 20

# s = Student()
# print(s.name)
# print(s.age)


# class Student:
#     def __init__(self, name):
#         self.name = name

# student = Student("Alice")
# student2 = Student("Bob")
# print(student.name)


# name = "Alice"
# print(name)
# name = "Bob"
# print(name)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def study(self):
#         print(f"Учусь студент {self.name}, возраст {self.age} лет.")
# 
#     def birthday(self):
#         self.age += 1
#         print(f"{self.name} исполнилось {self.age}")
# 
# s1 = Student("Ali", 20)
# s2 = Student("Bob", 19)
# s3 = Student("Alice", 18)
# s1.study()
# s1.birthday()
# s2.study()
# s2.birthday()
# s3.study()
# s3.birthday()
# 
# 
# '''
# класс - это чертеж 
# объекты - это готовый экземпляр
# методы - это поведение объект
# атрибуты - это состояние объект
# # '''


#                     класс Студент 

#                 name
#                 age
#                 study()
#                 birthday()

#     Student           Student         Student 
#       ALI              ALI              Bob



class User:
    pass 

print(type(User))

num1 = 10
print(type(num1))
name = "Name"
print(type(name))
list = []
print(type(list))
print(type(type))