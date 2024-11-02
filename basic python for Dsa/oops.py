# class Student:
#     #instance variable/attribute
#     name = "Sanaan"
#     age = 27
#     def display(self):
#         print("This is my method")

# obj = Student()#object
# print(obj.name)
# obj.display()



#-------------------
'''
class: it a collection of attribute and methods, or it a buel print or template by which object followes

object: instance of class


self: its an argument that call itself, it similar to "this" Keyword in JAVA

'''
class Student:
    #instance variable/attribute
    name = "Sanaan"
    age = 27
    def student_detail(self):
        print(f"Then name is: {self.name} and age is: {self.age}")

obj = Student()#object
print(obj.name)
obj.student_detail()

print("-------------")
#multiple student
class Student:
    def student_detail(self,name,age):
        print(f"Then name is: {name} and age is: {age}")

obj = Student()#object
obj.student_detail("Ameen",26)
obj.student_detail("Sanaan", 26)
obj.student_detail("Ameen",26)

#or
#Constructor
class Student:
    #constructor: it is used to initialize instance variable
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def student_details(self):
        print(f"The name is {self.name} and marks is {self.marks} and age is {self.age}")
        
obj = Student("Alen",25,90)
obj.student_details()

sanaan_obj = Student("Sanaan",26,95)
sanaan_obj.student_details()



#Scope of variable
'''
1.global vairable
2.instance variable
3.local variable
'''


n = 786 #glabal variable bhai
class MyClass:
    n = 100 #instance variable 
    
    def display(self):
        n = 10000 #local variable
        print(n)
        
obj = MyClass()
print(obj.n)
obj.display()
print(n)


#inheritance
'''
1.single level inheritance
2.multi level inheritance
3.multiple inheritance (In Java no multiple inheritance, we can achieve this usint interfaces)
4.Hybrid inheritance


NOTE:
PARENT CLASS: BASE CLASS or super class
Child CLASS: DERIVED CLASS or sub class
'''
#SINGLE LEVEL INHERITENCE
class Parent:
    def pdisplay(self):
        print("This is parent property")

class Child(Parent):
    def cdisplay(self):
        print("This is child property")

c = Child()#child object
c.cdisplay()
c.pdisplay()



#MULTI LEVEL INHERITANCE
class GParent:
    def gpdisplay(self):
        print("This is grand parent property")
class Parent(GParent):
    def pdisplay(self):
        print("This is parent property")

class Child(Parent):
    def cdisplay(self):
        print("This is child property")

c = Child()#child object
c.cdisplay()
c.pdisplay()
c.gpdisplay()

print("--------------")
#Multiple inheritance
# class Father:
#     def fd(self):
#         print("This is father property")
# class Mother:
#     def md(self):
#         print("Mother property")
# class Child(Father,Mother):
#     def cd(self):
#         print("This is child dispay")
        
# c = Child()
# c.cd()
# c.fd()
# c.md()

#Hybrid inheritance
class Parent:
    def pdisplay(self):
        print("This is parent display")
        
class Child1(Parent):
    def c1(self):
        print("This is child 1")
class Child2(Parent):
    def c2(self):
        print("This is child 2")
class Child3(Parent):
    def c3(self):
        print("This is child 3")

c1 = Child1()
c1.pdisplay()
c2 = Child2()
c2.pdisplay()
c3 = Child3()
c3.pdisplay()