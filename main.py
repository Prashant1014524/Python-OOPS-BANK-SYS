# # OOPs 
# class Factory:
#     @staticmethod
#     def Hello():
#         print("Hello")
#     # dender method 
#     def __init__(self,material,zips,pock):
#         self.material=material
#         self.zips=zips
#         self.pock=pock
#     def show(self):
#         print(f"your object details are{self.material},{self.pock},{self.zips}")
#     # static method that doesnot need the self in the paramerer 
   


# reebook=Factory("Leather",3,2);
# campus=Factory("HardL",5,7);
# # print(reebook.pock)
# # print(campus.pock)
# reebook.show()


##static method class method 

# Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"name is{self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age

#     def show(self):
#         print(f"Name is {self.name},{self.age}")
    


# p1=Human("Prashant",23)
# p1.show()

# MUltilevel inheritance 

# class Factory:
#     def __init__(self,material):
#         self.material=material

# class BhopalF(Factory):
#     def __init__(self, material,color):
#         super().__init__(material)
#         self.color=color

# class DelhiF(BhopalF):
#     def __init__(self, material, color,size):
#         super().__init__(material, color)
#         self.size=size

# obj=DelhiF()

# Duck typing

# class Dog:
#     def sound(self):
#         print("Bark!")

# class Cat:
#     def sound(self):
#         print("Meow!")

# def make_sound(self):
#     self.sound()

# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)

# Abstract classes and methods  abstaract class is the class that have abstractmethods and abstract method is the method that is onky defined not implemented but implemented in its subclaasses


# decorator 
# def decorate(func):
#     def wrapper(a,b):
#         print("The two number for additon is")
#         func(a,b)
#         print("I hope the answer is correct")
#     return wrapper

# @decorate

# def addition(a,b):
#     print(f"addition is{a+b}")

# addition(12,12)

# args and kargs