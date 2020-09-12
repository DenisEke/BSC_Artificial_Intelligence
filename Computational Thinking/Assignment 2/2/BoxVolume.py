#The following 3 blocks each get one of the dimension of the box (height, depth, width)
print("Let me calcuate the volume of the box for you. Please enter the height in meters: ")
height=int(input())

print("Not please enter the width in meters: ")
width=int(input())

print("Last please enter the depth again in meters: ")
depth=int(input())

#calculate the volume by multiplying the h w and d
volume=height*width*depth

#print the volume and the dimensions input by the user
print("The Volume of your "+str(height)+" * "+str(width)+" * "+str(depth)+" box is "+ str(volume)+" m^2")