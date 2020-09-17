#Ask for number of friend in a friendly way
print("Hey I am here to check whether your party is corona proof. How many friends are you planning to invite? ")
numberFriends=int(input())

#If less than or equal to 6 friends
if numberFriends<=6:

    #ask for friends name
    print("This should work out fine. Tell me their names and I will invite them. Just enter the names with spaces between: (Casy Mendel Lister)")

    #split is used to divide a string by a certain char (default is sapce)
    #creates an array of the entered friends.
    friends=input().split()

    #for every of the friends we print that he/she/it was invited!
    for friend in friends:
        print(friend +" has been invited!")

#If more than 6 friends
else:
    #inform user that he can't throw this party
    print("You can't throw this party. It is not Corona proven.")