import random                  
rng = random.Random()          
number = rng.randrange(1, 11) #get random number between 1 and 10

guesses = 0 #count the number of guesses

while True:
    input_from_user = int(input("Guess the number between 1 and 10: (enter 0 to exit) "))
    guesses += 1
    if input_from_user <1 or input_from_user >10:
        print("Thanks for playing")
        break
    if input_from_user > number:
        print("Too high")
    elif input_from_user <number:
        print("Too low")
    else:
        break

if input_from_user >0 and input_from_user <11:
    print("It is a match: ", input_from_user, "Number of guesses", guesses)
    
