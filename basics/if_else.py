n=int(input("enter a number:"))


if (n>0) :
     print("The number is positive")
elif(n==0):
      print("The number is zero")    
else:
     print("The number is negative")

if(n%2==0):
     print("the number is even")
else:
     print("the number is odd")

if(n>=18):
     print("the person is eligible for voting")
else:
     print("the person is not eligible for voting")


a=int(input("enter a number:"))
b=int(input("enter a number:"))
if(a>b):
     print("a is greater than b") 
else:
     print("b is greater than a")


marks = int(input("enter your marks:"))
if(marks>40):
     print("you are passed") 
else:
     print("better luck next time")


year = int(input("enter a year:"))
if year < 1000:
    print("Please enter a valid 4-digit year.")
else:
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")


mark = int(input("enter your marks:"))
if(mark>=90):
     print("A")
elif(mark>=75):
     print("B")
elif(mark>=60):
     print("C")
else:
     print("fail")


a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
o = input("Enter an operation number:")
if (o=="+"):
     sum = a+b
     print("The sum of the numbers is:", sum)
elif (o=="-"):
     diff = a-b
     print("The diffrence of the numbers is:", diff)          
elif (o=="*"):
     mul = a*b
     print("The multiplication of the numbers is:", mul)
elif (o=="/"):
     div = a/b
     print("The division of the numbers is:", div)
else:
     print("Enter a correct operator")


ch = input("#Enter a character")
if(len(ch) != 1):
     print("please enter a single character")
else:
     if ch.isalpha():
          ch = ch.lower()
          if ch in "aeiou":
               print("character is a vowel")
          else:      
               print("character is a consonant")
     else:
            print("character is not alphabet")



units = int(input("Enter units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 0) + (100 * 5) + (units - 200) * 10

print("Your electricity bill is: ₹", bill)



a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
c= int(input("Enter a number:"))
if(a>b):
     print("a is greater than b")
     if(a>c):
         print("a is the largest number.")
     else:
         print("c is the largest number.")      
else:
     print("b is the largest number.")