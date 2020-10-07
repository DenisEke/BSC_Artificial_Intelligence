# enum is used to store the game state
from enum import Enum
# random is used to get a random word
from random import randint

# Graphics contains graphics for this game
from Graphics import PrintColors, STATES


# Create an enum that stores the game state which is either
# LOST: the player has lost
# WON: the player has won
# IN_GAME: the player has neither lost or won
# we decided to create this enum for better code readability
# which is very important when coworking on a project
class GameState(Enum):
    LOST = 0
    WON = 1
    IN_GAME = 2


# This class contains all the game logic and stores the games state
# You initialize it with a word
# You then feed it the users input
# You can access getHint and getHangman to get the word only showing the guessed letters
# and to draw a hangman based on the wrong guesses of the user
# Access the state of the game through the state variable
class Game:
    # stores the state of the game
    state = GameState.IN_GAME
    # keeps track of users guesses
    guesses = []
    # keeps track of how many wrong guesses the user took
    wrong_guesses = 0

    # constructor
    # secret_word is word the user should guess
    def __init__(self, secret_word):

        # reset those always on init because somehow they got stored beetween multiple games
        self.guesses = []
        self.wrong_guesses = 0

        self.secret_word = secret_word

    # This function handles the users input
    def guess(self, guess):

        # check whether it is really only one letter
        if len(guess) > 1:
            # if so print a message. The first and last part adds color to the statement
            print(PrintColors.WARNING + "You can only enter one letter" + PrintColors.ENDC)

        # turns the guess uppercase
        guess = guess.upper()

        # if the guessed letter is already in the letters the user guessed before
        if guess in self.guesses:
            # inform him of it
            print(PrintColors.WARNING + "You have already tried the letter " + guess + PrintColors.ENDC)
            return

        # add his/her guessed letter to the guessed letters
        self.guesses.append(guess)

        # if the guess is part of the word
        if guess in self.secret_word:
            # check whether the user has won
            if self.hasWon():
                # change state to won
                self.state = GameState.WON
                return

        # check if the user hast lost if the guess is not part of the word
        else:
            # because the guess is wrong we add it to the wrong guesses
            self.wrong_guesses += 1
            if self.hasLost():
                # change state to lost
                self.state = GameState.LOST
                return

    # checks whether the user has lost
    def hasLost(self):

        # if the user has more wrong guesses than we have graphics for the hangman he has lost
        if self.wrong_guesses >= len(STATES):
            return True

        return False

    # checks whether user has won
    def hasWon(self):

        # if every char of the secret word is in the guesses the user has won
        for char in self.secret_word:
            if char not in self.guesses:
                return False

        return True

    # give user his word with dashes for not guessed letters
    def getHint(self):

        # start with an empty string
        hint = "";

        # for each letter in our secret word
        for char in self.secret_word:

            # if the letter is not in the users guesses add a dash
            if char not in self.guesses:
                hint += "_ "

            # if it is add the letter itself
            else:
                hint += char + " "

        return hint

    # get the current hangman graphic
    def getHangman(self):
        # returns the hangman graphic based on the current wrong guesses
        return STATES[self.wrong_guesses]


# our extraordinary wordlist the secret word gets chosen from
# SOURCE: https://www.hangmanwords.com/words HARD HANGMAN WORDS
WORDLIST = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom",
    "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini",
    "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo",
    "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph",
    "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri",
    "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip",
    "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack",
    "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia",
    "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph",
    "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic",
    "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest",
    "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful",
    "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch",
    "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis",
    "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays",
    "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm",
    "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz",
    "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm",
    "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff",
    "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome",
    "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong",
    "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka",
    "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring",
    "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy",
    "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy",
    "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"
]


# this function is a helper function and returns a random word from the wordlist
def get_random_word():
    # randint returns a pseudo random integer between the first param and the second param
    # in this case the first is 0 and the second is the length of out list -1 one.
    # this way we easily can add words later on
    return WORDLIST[randint(0, len(WORDLIST) - 1)].upper()
