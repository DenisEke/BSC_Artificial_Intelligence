# My code for task 6 of assignment 4

# Describe program and let user enter his sentence
print("Hey. You can enter a sentence and I will count how many words there are init: ")

# Get his sentence and split it
# input returns users input until he presses enter
# split splits a string by a certain character; default is space.

# NOTE: this isn't perfect. Because for example "isn't" technically is two words "is and not" and
# this solution doesn't return this as such. Everything else is far more complicated so I think this
# is what is expected
words = input().split()

# output the length of the users sentence
# len is used to return the length of an array
print("The sentence you entered contains ", len(words), " words.")
