#random gives us the function choices which can select n amount of chars from a provided string or array
import random
#I use this to get the ascii letters and to not have to define them manually
import string

#Ask the user for the wished length of the password
print("Hello there. How long should the password you wish be? ")
#and store it here
length=int(input())

#generate the password by using the choices function which is described in the first comment
#I added some more characters so that the password will be even stronger
#the join function is used to make the array that random.choices returns to a string
password="".join(random.choices("°^!§$%&/()=?`\}][{@+*~|<>"+string.ascii_letters, k=length))

#for a better user experience I print the password in a seperate line from the description text
#this way in can be easily copied
print("Your password is:")
print(password)
