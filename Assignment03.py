
'''1'''
def a_fun():
	global name
	name = 'A'
def b_fun():
	global name
	name = 'B'
b_fun()
a_fun()
print (name)

# output= A


'''2'''
a = 10
def f():
    print ('Inside f() : ', a)
def g():
    a = 20
print ('Inside g() : ',a)
def h():
    global a
    a = 30
    print ('Inside h() : ',a)
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)


# output:
# Inside g() :  10
# global :  10
# Inside f() :  10
# global :  10
# global :  10
# Inside h() :  30
# global :  30


'''3'''
a_var = 10
b_var = 15
e_var = 25
d_var = 100
def a_func(a_var):
    print("in a_func a_var =", a_var)
    b_var = 100 + a_var
    d_var = 2 * a_var
    print("in a_func b_var =", b_var)
    print("in a_func d_var =", d_var)
    print("in a_func e_var =", e_var)
    return b_var + 10
c_var = a_func(b_var)
print("a_var =", a_var)
print("b_var =", b_var)
print("c_var =", c_var)
print("d_var =", d_var)

# OUTPUT
"""
in a_func a_var = 15
in a_func b_var = 115
in a_func d_var = 30
in a_func e_var = 25
a_var = 10
b_var = 15
c_var = 125
d_var = 100
"""


'''4'''
a,b,x,y=1,15,3,4
def fun(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print (a,b,x,y)
fun(17,4)
print (a,b,x,y)

# OUTPUT
"""
42 17 4 17
42 15 3 4
"""

'''5'''
def f():
    x = 42

    def g():
        global x
        x = 43


print("Before calling g: ",x)
g()
print("After calling g: ",x)

f()
print("x in main: ",x)

# OUTPUT
"""
Before calling g:   42
After calling g:   42
x in main:  43
"""


'''6'''
def outer():
    s="Ludhiana"
    def inner1():
        s="punjab"
    def inner2():
        nonlocal s
        s="Chandigarh"
    def inner3():
        global s
        s="Haryana"
    print(s)
    inner1()
    print(s)
    inner2()
    print(s)
    inner3()
    print(s)
outer()
print(s)


# OUTPUT:
"""
Ludhiana
Ludhiana
Chandigarh
Chandigarh
Haryana'''

'''7'''
eid, ename, esal = 1, 'aaa', 10000.56

def emp(eid, ename, esal):
	globals()['eid'] = eid
	globals()['ename'] = ename
	globals()['esal'] = esal


print(eid, ename, esal)


def disp():
	print(eid, ename, esal)


emp(111, 'ratan', 10000.45)
disp()
print(eid, ename, esal)


# OUTPUT
"""
1 aaa 10000.56
111 ratan 10000.45
111 ratan 10000.45"""
'''8'''
a,b=100,200
class MyClass():
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print(globals()['a']+globals()['b'])
        print(self.a+self.b)
    def mul(self,a,b):
        print(a * b)
        print(globals()['a'] + globals()['b'])
        print(self.a * self.b)
c = MyClass()
c.add(3, 3)
c.mul(4, 4)

# output:
"""
6
300
30
16
300
200"""


'''9'''
class Emp:
    def _init_(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def _str_(self):
        return "emp id=%d Emp name=%s Emp sal=%g"%(self.eid,self.ename,self.esal)
e1 = Emp(111,"kamal",100000.45)
print(e1)
e2 = Emp(111,"anu",200000.46)
print(e2)

# output:
"""
emp id=111 Emp name=kamal Emp sal=100000
emp id=111 Emp name=anu Emp sal=200000
"""