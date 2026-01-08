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