'''classes and objects'''
class DemoClass:
    a=10
    def SumValue(self):
        print(20+30)

obj=DemoClass()
obj1=DemoClass()
print(obj.a)
print(obj1.a)
obj.SumValue();

'''construtor'''
class DemoClass:
    a=10
    def SumValue(self):
        print(self.a)
obj=DemoClass()
obj.SumValue();


'''inheritance'''
'''single'''
class A:
    def displayA(self):
        print("welcome to python class A")
class B(A):
     def displayB(self):
        print("welcome to python class B")
obj=B()
obj.displayA()
obj.displayB()



'''multilevel'''

class A:
    def displayA(self):
        print("welcome to python class A")
class B(A):
     def displayB(self):
        print("welcome to python class B")
class C(B):
    def displayC(self):
        print("welcome to python class C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

'''Multiple'''

class A:
    def displayA(self):
        print("welcome to python class A")
class B:
     def displayB(self):
        print("welcome to python class B")
class C(A,B):
    def displayC(self):
        print("welcome to python class C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()


'''Polymorphism'''
l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

'''overloading'''
class Ws:
    def displayinfo(self,name=''):
        print("welcome to python class A" +name)
obj=Ws()
obj.displayinfo()
obj.displayinfo('python')

'''overriding'''
class Ws:
    def displayinfo(self):
        print("welcome to python class A")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("welcome to IIP")
obj=IIP()
obj.displayinfo()




