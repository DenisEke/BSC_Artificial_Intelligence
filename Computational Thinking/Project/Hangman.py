# The Graphics file/module contains all the graphical stuff
from Graphics import PrintColors, STATE_WON, STATE_DEAD
# The Logic file/module contains all the game logic
from Logic import Game, GameState, get_random_word

# ask for the user name
name = input("Welcome to Hangman. Please tell me your name... ")
# complement the user for a better experience
print("What a wonderful name you have " + name)
# Tell him that we start a new round of hangman
print("Lets start a round of Hangman")

# so we can start a new round when the user won or lost we put the game
# loop in a while and need to have a variable to keep track whether the
# program should end or start over
running = True
while (running):

    # create a new Game
    game = Game(secret_word=get_random_word())

    # While the game is in progress
    while (game.state == GameState.IN_GAME):
        # draw the hangman graphic
        print(game.getHangman())
        # tell the user the parts of the word he/she knows
        print("Hint: " + game.getHint())

        # tell him to guess a symbol
        print("Guess a symbol: ")

        # get users input
        guess = input()

        # let our game handle the users input
        game.guess(guess=guess)

    #is the user has won
    if game.state == GameState.WON:
        #show the winning hangman
        print(STATE_WON)
        #congratulate the user on this win
        print(PrintColors.OKGREEN + "Congratulations you won, " + name + "! " + PrintColors.ENDC)

    #if the user has lost
    if game.state == GameState.LOST:
        # show the dead hangman
        print(STATE_DEAD)
        # tell the user he lost
        print(
            PrintColors.FAIL + "Sorry but you have lost " + name + "! The word was " + game.secret_word + ". " + PrintColors.ENDC)

    #We had to put a while loop here to handle other inputs than Y and n
    hasGivenCorrectInput = False
    while (not hasGivenCorrectInput):
        #ask user whether he wants to play again and store his input
        print("Do you want to play again? (Y/n)")
        replay = input()

        #if his input is Y
        if replay == "Y":
            #end the current while loop so we start from the top
            hasGivenCorrectInput = True
            print("Allright. I am starting a new game. :)")
        #if it is n
        elif replay == "n":
            #and the while loop and set running to false to exit the program
            hasGivenCorrectInput = True
            running = False
            print("See you next time! :(")
        else:
            #clarify what the user has to enter
            print("You can only enter Y or n. Y=Yes; n=no")
