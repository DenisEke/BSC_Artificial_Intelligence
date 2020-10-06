# NOTE: it was wrong to call the graphics state. But we did not want to change it that late in development

# Source: https://stackoverflow.com/a/287944
# Wanted to find a way to add color to print statements.
class PrintColors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# How the hangman looks when he is dead
STATE_DEAD = PrintColors.FAIL \
             + "__________  \n" \
             + "|        |  \n" \
             + "|        0  \n" \
             + "|       /|\ \n" \
             + "|       / \ \n" \
             + "|___________\n" \
             + PrintColors.ENDC

#how the hangman looks when he won
STATE_WON = PrintColors.OKGREEN \
            + "__________  \n" \
            + "|        |   \n" \
            + "|            \n" \
            + "|      \ 0 / \n" \
            + "|        |   \n" \
            + "|_______/_\  \n" \
            + PrintColors.ENDC

#how the hangman looks throughout the game.
STATES = [
    # State 0
    "__________  \n" +
    "|        |  \n" +
    "|          \n" +
    "|        \n" +
    "|        \n" +
    "|___________\n",
    # State 1
    "__________  \n" +
    "|        |  \n" +
    "|        O  \n" +
    "|        \n" +
    "|        \n" +
    "|___________\n",
    # State 2
    "__________  \n" +
    "|        |  \n" +
    "|        O  \n" +
    "|        | \n" +
    "|        \n" +
    "|___________\n",
    # State 3
    "__________  \n" +
    "|        |  \n" +
    "|        O  \n" +
    "|       /| \n" +
    "|         \n" +
    "|___________\n",
    # State 4
    "__________  \n" +
    "|        |  \n" +
    "|        O  \n" +
    "|       /|\ \n" +
    "|        \n" +
    "|___________\n",
    # State 5
    "__________  \n" +
    "|        |  \n" +
    "|        O  \n" +
    "|       /|\ \n" +
    "|       /  \n" +
    "|___________\n",
]
