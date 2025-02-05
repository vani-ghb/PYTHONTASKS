#conditional statements
num1=1
if num1 == 1:
    print("puspha the rise")
else:
    print("puspha the rule")
    print("150 cr")
print("code ended") 
if num1 > 0:
    if num1==0:
        print("one")
    else:  
       print("positive")
else:
    if num1 == 0:
      print("zero")
    else:
        if num1 == 1:
            print("1")
        else:
            print("negative")
#elseif-elif
if num1 > 0:
    print("positive")
elif num1 == 1:
    print("1")
elif num1 == 0:
    print("zero")
elif num1 ==-1:
    print("-1")
elif num1 ==-2:
    print("-2") 
else:
    print("negative")

#current bill
# 100unitd-per unit 50 rupess
# 101 to 200-per unit 100 rupees
# 201 to 300-per unit 150 rupees
#if 0 to 50 -per unit 0 rupees  
current_units=int(input("enter units"))    
if current_units <= 100:
    if current_units < 0:
        print("invalid")
    else:
        if current_units<=50:
            print("jai balaya")
    print(current_units * 50)
else:
    if current_units <=201 :
            print(current_units * 100)
    else:
        print(current_units * 150)
    if current_units <= 300:
            print(current_units * 150)
    else:
        print(current_units * 250)
# #loops
#uses-to reduce the time and easy way 
for i in range(0,10):
    print("heloo")



        