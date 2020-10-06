from enum import Enum
from random import randint

WORDLIST = ["Pizza", "Burger", "Taco", "Buritto"]
MAX_GUESSES = 5


def get_random_word():
    return WORDLIST[randint(0, len(WORDLIST) - 1)].upper()


class GameState(Enum):
    LOST = 0
    WON = 1
    IN_GAME = 2


class Game:
    state = GameState.IN_GAME
    guesses = []

    def __init__(self, secret_word, max_wrong_guesses):
        self.secret_word = secret_word
        self.MAX_WRONG_GUESSES = max_wrong_guesses

    def guess(self, guess):

        guess = guess.upper()

        if guess in self.guesses:
            print("You have already tried the letter " + guess)
            return
        self.guesses.append(guess)

        if self.hasWon():
            self.state = GameState.WON
            return

        if self.hasLost():
            self.state = GameState.LOST
            return

    def hasLost(self):
        wrong_guesses = 0

        for guess in self.guesses:
            if guess not in self.secret_word:
                wrong_guesses += 1

        if wrong_guesses >= self.MAX_WRONG_GUESSES:
            return True
        return False

    def hasWon(self):

        for char in self.secret_word:
            if char not in self.guesses:
                return False

        return True

    def getHint(self):

        hint = "";
        for char in self.secret_word:
            if char not in self.guesses:
                hint += "_ "
            else:
                hint += char + " "

        return hint


game = Game(secret_word=get_random_word(), max_wrong_guesses=MAX_GUESSES)
while (game.state == GameState.IN_GAME):
    print("Hint: " + game.getHint())
    print("Guess a symbol: ")

    guess = input()
    game.guess(guess=guess)

if game.state == GameState.WON:
    print("Congratulations you won!")

if game.state == GameState.LOST:
    print("I am sorry but you have lost")
'''
###elifs part
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
'''
