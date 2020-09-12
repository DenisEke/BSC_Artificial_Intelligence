
#For the convinience of the user I print a simple statement
print("This program will add 2 whole numbers you provide. Please enter the first number? ")

#Stores the users input
num1 = input()

#Ask for second number
print("Your first number is "+num1+". What do you wish as the second number? ")

#Store second number
num2 = input()

#print the result and the numbers the user entered
print("The sum of your numbers ("+num1+","+num2+") is "+str(int(num1)+int(num2)))