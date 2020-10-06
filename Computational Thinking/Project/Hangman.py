from Graphics import PrintColors, STATE_WON, STATE_DEAD
from Logic import Game, GameState, get_random_word

name = input("Welcome to Hangman. Please tell me your name... ")
print("What a wonderful name you have " + name)
print("Lets start a round of Hangman")

running = True
while (running):

    game = Game(secret_word=get_random_word())

    while (game.state == GameState.IN_GAME):
        print(game.getHangman())
        print("Hint: " + game.getHint())
        print("Guess a symbol: ")

        guess = input()
        game.guess(guess=guess)

    if game.state == GameState.WON:
        print(STATE_WON)
        print(PrintColors.OKGREEN + "Congratulations you won, " + name + "! " + PrintColors.ENDC)

    if game.state == GameState.LOST:
        print(STATE_DEAD)
        print(
            PrintColors.FAIL + "Sorry but you have lost " + name + "! The word was " + game.secret_word + ". " + PrintColors.ENDC)

    hasGivenCorrectInput = False
    while (not hasGivenCorrectInput):
        print("Do you want to play again? (Y/n)")
        replay = input()

        if replay == "Y":
            hasGivenCorrectInput = True
            print("Allright. I am starting a new game. :)")
        elif replay == "n":
            hasGivenCorrectInput = True
            running = False
            print("See you next time! :(")
        else:
            print("You can only enter Y or n. Y=Yes; n=no")
