word = "kertenkele"
word = word.upper()
guessfinished = False
counter = 0
user_letter = "--"
word3 = ""
word2 = ""
for i in range(len(word)):
    word2 = word2 + "-"
print(word2)

print("Let's play Hangman!")


def finding_letter_in_word(user_letter):
    global word2
    global word3
    x = word.find(user_letter)
    if x < 0:
        print("Try again.")
    else:
        print("Found at line" + str(x))
        for i in range(len(word2)):
            if word2[i] == "-":
                if i == x:
                    word3 = word3 + user_letter
                else:
                    word3 = word3 + "-"
            else:
                word3 = word3 + word[i]
        word2 = word3
    print(word2)


while counter < 8:
    user_letter = str(input("Guess letter"))
    user_letter = user_letter.strip()
    user_letter = user_letter.upper()
    user_letter = user_letter[0]
    counter = counter + 1
    # print(user_letter)
    finding_letter_in_word(user_letter)
