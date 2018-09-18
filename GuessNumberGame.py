# Your friend will complete this function

# Add logic so that the players take turns to play first. - YTD

def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

#Write the main program which repeatedly calls this function to play the game,
# and after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
# It then asks the player “Do you want to play again?” and either plays again, or says “Goodbye”, and terminates.

def game():
    counter_player = 0 # Keep score of how many wins each player has had, and how many draws there have been. After each round of play, also announce the scores.
    counter_comp = 0
    counter_draws = 0

    total_games_played =0 # Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each round.

    wannaPlay = input("Do you want to play a game? ")
    while wannaPlay == "yes":
        total_games_played = total_games_played+1
        n = int(input("Enter your value: -1, 0, 1: "))
        a = play_once(n)
        if a == -1:
            print("You Win.", "\n")
            counter_player = counter_player+1
        elif a == 0:
            print("Game Drawn.", "\n")
            counter_draws += 1
        elif a == 1:
            print("I Win.", "\n")
            counter_comp += 1

        print("You won: ", counter_player, "times")
        print("I won: ", counter_comp, "times")
        print("Game drawn: ", counter_draws, "times \n")

        winPercent_1 = (counter_player/total_games_played) *100
        winPercent = round(winPercent_1,2)

        print("Hooman win percent after this round", winPercent)

        wannaPlay = input("Do you want to play again?")
    else:
        print("Good Bye")

game()
