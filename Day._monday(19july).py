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

'''o/p
10
10
50'''


'''construtor'''
class DemoClass:
    a=10
    def SumValue(self):
        print(self.a)
obj=DemoClass()
obj.SumValue();

'''o/p
10'''