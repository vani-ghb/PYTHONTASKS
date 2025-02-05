#complex numbers
a=2+3j
b=4+5j
print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/b))
print(type(a**b))
# print(type(a%b))
# print(type(a//b))
#not working these two operaters in python
#boolean values
num1="abc"
num2="bca"
print(num1==num2)
print(10<7)
print(333.23>23)
print(7>7)
#list
#it is mutable we can change the value
#we can added or deleted the value
#compartble list is slowerthan tuple
#memory effeicent not fixed
list_new=[2,3,4,"string", True,[1,"hello",3]]
print(list_new)
print(list_new[3])
print(list_new[5])
print(len(list_new))
print(len(list_new[5]))
print(list_new[-2])
print(list_new[1:4:2])
print(list_new[3])
print(list_new[1:4:2])
print(list_new[1:4])
#tuple
#it is imutable we can not change the value
#we can not change the value
#tuple is faster than the list
#abit more memory effecient is fixed
#range-limit
#range from starting value to ending value
print(list(range(0,100)))
print(list(range(0,100,2)))
print(list(range(0,100,1)))
print(list(range(0,100,-1)))
print(list(range(100,1,-1)))
print(list(range(0,100)))

