'''palidrome'''
a=input("Enter the string:")
b=a[-1::-1]
if(a==b):
	print("Palidrome String")
else:
	print("Not palidrome string")


'''Factorial of a no'''
i=int(input("Enter the num:-"))
fac=1
while(i>0):
    fac=fac*i
    i=i-1
print("Factorial=",fac)


'''fibonacci series'''
num = int(input("Enter any number :"))
n1, n2 =0,1
sum =0
if num<=0:
    print('please enter number greater than 0')
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 =sum
        sum  = n1 + n2
 
 
'''check the no is amstrong'''
i=int(input("Enter the num to check the armstrong:-"))
orig=i
sum=0
while (i>0):
    sum=sum+(i%10)(i%10)(i%10);
    i=i//10
if orig==sum:
    print("num is armstrong")
else:
    print("num is not armstrong")
   

   
'''HOW TO BUILD THE CALCULATER IN PYTHON'''
# ADD
# SUBTRACT
# MULTIPLY
# DIVIDE
print("Select the operation from the following:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation = input()
if operation == "1":
    num1 = input("Enter the 1st no : ")
    num2 = input("Enter the 2nd no : ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation=="2":
     num1=input("Enter the 1st no : ")
     num2=input("Enter the 2nd no : ")
     print("The subtract is " + str(int(num1) - int(num2)))

   

elif operation=="3":
     num1=input("Enter the 1st no : ")
     num2=input("Enter the 2nd no : ")
     print("The multiply is " + str(int(num1) * int(num2)))
elif operation=="4":
     num1=input("Enter the 1st no : ")
     num2=input("Enter the 2nd no : ")
     print("The divide is "+ str(int(num1) / int(num2)))
  
else:
    print("invalid Entry")


'''pattern'''
rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print('*', end=' ')
    print("\r")


'''leap year'''
input_year = int(input("Enter a year:"))
def is_leap(year):
    if (year % 400 ==0) or (year % 4 ==0 and year % 100 !=0):
        return True
        
    return False
     
     
if is_leap(input_year):
    print("It is a leap year")
else:
    print("It is not a leap year")


'''prime number'''
num = 7
for i  in range(2,num):
  if num % i == 0:
        print("Not prime")
        break
else:
    print("prime")


'''Area of triangle'''
a = int(input("enter the length of first side:"))
b = int(input("enter the langth of second side:"))
c = int(input("enter the langth of third side:"))


p = (a+b+c)
s =p/2

area = (s* (s-a)(s-b)(s-c))**0.5

print("area of triangle is:",area)
print("perimeter of triangle is:",p)
print("semi perimeter of triangle is:",s)


'''reverse a list'''
list=[10,20,30,40]
list.reverse()
print(list)


'''sum of all elements in  the list'''
list=[20,10,15,50]
total=sum(list)
print("sum of all elements in given list:", total)


'''max'''
l=[1,2,3,4,5]
m=max(l)
print(m)

'''min'''
l=[1,2,3,4,5]
m=min(l)
print(m)

'''average'''
list1 = [10,20,30]
sum_of_elements = sum(list1)
len_of_list1 = len(list1)
avg = sum_of_elements/len_of_list1
print("average of given numbers in list is:",avg)


'''A set is a subset of another set'''
A = set ([1,2,3,4,5])
B = set ([1,2,3])
if(B.issubset(A)):
    print("true")
else:
    print("False")


'''symmetric difference And set difference'''
setA={1,3,4,5,7}  
setB={0,2,4,5,6}
print(setA.symmetric_difference(setB))
setC=setA-setB
print(setC)

   
'''17'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


'''18'''
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))


'''19'''
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")