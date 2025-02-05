#for loop and while loop
#you know the values
#converterd into for loop into while loop 
for y in range(0,21):
     print(y)
     print(y+5)
     print("edho okati")
     print("malli edho oakti")       
for i in range(0,21,3):
    print(i)
    for i in range(0,21):
        if i % 3 ==0:
            print(i)
            for i in range(1,21,2):
                print(i)
#skip the one letter
print(i*i*i)
print(i**2)  
#range-start number to ending number in the middle numbers are excuted only this is called range  
#Nested loops- 
for j in range(1,11):#j=1
        if j != 5 and j!=7:#not enter into the loop direct we write the for loop
             for i in range(1,31):
                  print(j,i)
        if j != 5 and j!=7:#5 and 7 are skip 
            print(j,i) 
#while loop-  
#when i am going to the home,i was watching a movie
#some what diffcult to the converted  while loop into for loop
# if a condition that condition  to a false that loop are running contionusly while condition:
#check the condition 
#if condition true then code is running 
# num1=2
# while num1 < 5:
#      print("eat...")
#      print("still eating")
#      num1 += 1
#for loop converted while loop   
# num1=1
# while num1 < 26:
#      if num1 % 2 ==0:
#         print (num1, "even")
# else:
#      print( num1,"odd") 
#      num1 +=1
j=1
while j <11:
    i=1
    print(i)
    if j !=5 and j !=7:
        while i<31:
            print(j,i)
            i+=1
            j+=1

          
             