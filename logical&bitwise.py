#logical & bitwise opertors
#logical and or and not
#&&,||,!
print(True and True)#if first is true then next value to move
print(False and True)#if first is false the next not move to next value
print(True and False)
print(False and True)
#print----numbers---
print(2 and 3)#and opetaors and depend to second value
print(3 and 2)
print(3 and "" )
print("" and 0)
print(-1 and -3)
print(0 and "")
print(False and 45)
print(None  and 3)#none is falsy
print(True or False )
print(False or True )
print(False or (False and True ))
print(True and (False or True )and (True or False))
print(2 or 3)#logical opeartes return operands
print( 3 or 2)
print("" or True )
print(0 or 0 or 1)
#not operater
print(not True)
print(not False)
print(not (2 or 3))
print(not("" and 3))

#bitwise operater-&,|,^,~,>>,<<
print(4 & 3)
#0100 & 0011 => 0000=0
  

#xor operaters 
print(12^14)

#Left shift-
#Right shift-
print(3 << 1)
print(3 >> 1)
print(4 >> 1)#interger division by 2
print(4 << 1)#doubled


#~  +1 added to the value
print(~13)
print(~15)
print(~26)

#conditional statments
print("i can vote")
print(" i can not vote")
#if my age is condition then print "" or else ""
age=18
if age >= 18:
    print("hurry! dabullu istharu")
    print("jai Democracy")
else:
    print("ivaru sirr")
