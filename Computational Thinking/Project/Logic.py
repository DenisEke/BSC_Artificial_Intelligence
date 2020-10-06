from enum import Enum
from random import randint

from Graphics import PrintColors, STATES


class GameState(Enum):
    LOST = 0
    WON = 1
    IN_GAME = 2


class Game:
    state = GameState.IN_GAME
    guesses = []
    wrong_guesses = 0

    def __init__(self, secret_word):
        self.secret_word = secret_word

    def guess(self, guess):

        guess = guess.upper()

        if len(guess) > 1:
            print(PrintColors.WARNING + "You can only enter one letter" + PrintColors.ENDC)

        if guess in self.guesses:
            print(PrintColors.WARNING + "You have already tried the letter " + guess + PrintColors.ENDC)
            return
        self.guesses.append(guess)

        if self.hasWon():
            self.state = GameState.WON
            return

        if self.hasLost(guess):
            self.state = GameState.LOST
            return

    def hasLost(self, guess):
        if guess not in self.secret_word:
            self.wrong_guesses += 1

        if self.wrong_guesses >= len(STATES):
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

    def getHangman(self):
        return STATES[self.wrong_guesses]


WORDLIST = ["Pizza", "Burger", "Taco", "Buritto"]


def get_random_word():
    return WORDLIST[randint(0, len(WORDLIST) - 1)].upper()
