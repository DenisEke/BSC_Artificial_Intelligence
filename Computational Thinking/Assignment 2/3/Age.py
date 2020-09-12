#this module or library is used to get the current year so that is program will also work in the future
#NOTE: it can be used for many more date operations
import datetime

#Print small description and ask for name
print("This program print out your age. But let us start with your name: ")

#Store inputed name in a var
name = input()

#For a better user experience I complement the user on his name and ask when he was born
print("Thats a wonderful name, "+name+". What year were you born? ")

#store the birth year of the user
birthYear = int(input())

#get the current year
nowYear = datetime.datetime.now().year

#print out his age by subtracting users birth year from the current year
print("So you are "+str(nowYear-birthYear)+" years old. Not bad, "+name+"!")