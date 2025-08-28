num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
OP=input("Enter operator to use: ")
if OP =="+":
 result=num1+num2
 print("result")
elif OP =="-":
 result=num1-num2
 print("result")
elif OP =="*":
 result=num1*num2
 print("result")
elif OP =="/":
 if num2!=0.0:
   result=num1/num2
   print("result")
 else:
  print("infinity")
else:
 print("Invalid Operation")

