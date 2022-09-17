num1 = int(input("Enter First Numeber: "))

num2 = int(input("Enter Second Number: "))



print("Enter Which Operation Would You Like to Perform")

op = input("Enter Operation That You Like +,-,*,/: ")



result = 0

if op == '+':

  result = num1 + num2

elif op == '-':

  result = num1 - num2

elif op == '*':

  result = num1 * num2

elif op == '/':

  result = num1 / num2

else:
  print("INVALID")



print(num1, op , num2, "=", result)