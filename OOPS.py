#Class & Objects

class Demo:
    def love(self,m):
        print("Hai love")
        print(m)
m = "sasi"
s = Demo()
s.love(m)

#Constructor Passing

class Transport:
    def __init__(self,val,val1):
        self.val=val
        self.val1=val1
    def type(self):
        print(self.val+" "+self.val1)
m1 = Transport("Road","12km")
m2 = Transport("air","36km")
m1.type()
m2.type()

#Without Constructor

class Transport:
    def type(self,val,val1):
        print(val+" "+val1)
m1=Transport()
m2=Transport()
m1.type("sasi","18")
m2.type("Kavin","19")

#variablesPassing

class Music:
    def __init__(self,name,age):
        self.name=name #instance valiables
        self.age=age
    def view(self):
        print(self.name+" "+str(self.age))
m1=Music("chithra",22)
m2=Music("suchi",36)
m1.name = "sasi"
m2.age = 56#Classvariables
m1.view()
m2.view()

#getsetmethods

class school:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        avg=self.m1+self.m2+self.m3/3
        print(avg)
    def get(self):
        print(self.m1)
    def set_(self,val):
        self.m2=val
ms=school(23,87,67)
ms1=school(28,99,44)
ms.avg()
ms1.avg()
ms.get()
ms1.get()
ms1.set_(77)
ms1.avg()

#types of methods
#instance method - normal (method/function)
#class method - @classmethod
#static method - @staticmethod

class methods():
    vm = "vasi"
    def __init__(self,name):
        self.name=name 
    def student(self):
        print(self.name)
    @classmethod
    def clsmethod(cls):
        print(cls.vm)
    @staticmethod
    def static():
        print("I am static")
m1 = methods("sasi")
m1.student()
methods.clsmethod()
methods.static()

#Inheritance
#Single Inheritance - A to B
#Multilevel Inheritance - A to B to C
#Multiple Inheritance - A , B , C(A,B)

#Single
class A:
    def add(self,a,b):
        res = a+b
        print(res)
    def sub(self,a,b):
        res = abs(a-b)
        print(res)
class B(A):
    def mul(self,a,b):
        res = a*b
        print(res)
    def div(self,a,b):
        res = a//b
        print(res)
m1 = A()
m2 = B()
m1.add(10,20)
m2.mul(20,90)
m2.add(15,30)

#Multiple Inheritance
class A:
    def behaviour1(self):
        print("class A1")
    def behaviour2(self):
        print("class A2")
class B(A):
    def behaviour3(self):
        print("class B1")
    def behaviour4(self):
        print("class B2")
class C(B):
    def behaviour5(self):
        print("class C1")
    def behaviour6(self):
        print("class C2")
O1 = A()
O2 = B()
O3 = C()
O1.behaviour2()
O2.behaviour4()
O3.behaviour1()


#MultipleInheritance
class A:
    def a(self):
        print("A")
class B:
    def b(self):
        print("B")
class C(A,B):
    def c(self):
        print("C")
O1=A()
O2=B()
O3=C()
O1.a()
O2.b()
O3.a()

#Superclass - Constructors in Inheritance

#MultipleInheritance
class A:
    def __init__(self):
        print("init in A")
    def a(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")
    def b(self):
        print("B")
a1=A()
a2=B()

#OperatorOverloading
class operator:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = operator(m1,m2)
        return m3
s1 = operator(10,20)
s2 = operator(20,40)
s3=s1+s2
print(s3.m2)

#MethodOverloading
class overload:
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            return a+b+c
        elif(a!=None and b!=None):
            return a+b
        else:
            return a
s = overload()
m = s.sum(10)
print(m)

#MethodOverriding
class A:
    def a(self):
        print("Parent class")
class B(A):
    def a(self):
        print("child class")
m = B()
m.a()

#3.Data Abstraction
#abstract class and method
from abc import ABC
class method(ABC):
    def abstract(self):
        pass
class A:
    def abstract(self,a,b):
        print(a+b)
class B:
    def abstract(self):
        print("Hai")
m1 = A()
m1.abstract(10,29)
m2 = B()
m2.abstract()

#4.Encapsulation
#private method
class Encapsulation:
    def __init__(self):
        self.__private()
    def A(self):
        print("normal method")
    def __private(self):
        print("privated function")
m = Encapsulation()
m.A()

#private variable
class Encapsulation:
    __a=0 
    __name=''
    def __init__(self):
        self.__a=10
        self.__name="sasi"
    def A(self):
        print(self.__a)
m = Encapsulation()
m.__a=20
m.A()



