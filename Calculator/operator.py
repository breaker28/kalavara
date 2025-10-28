#!/usr/bin/env python3
import rospy
def main():
  rospy.init_node('operators',anonymous= True)
  print("Simple Mathematical Operator using Ros")
  while not rospy.is_shutdown():
      try:
        num1 =float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        op = input("choose operation(+,-,*,/): ")
        if op =='+':
          print("Result: " , num1+num2)
        elif op == '-':
          print("Result: ", num1-num2)
        elif op == '*':
          print("Result: ",num1*num2)
        elif op == '/':
          print("Result: ",num1/num2
        else :
          print("Invalid Operator")
      except Exception as e:
        print("Error: ", e)
if __name__ =='__main__':
    main()
