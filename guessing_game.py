"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random


def start_game(high_score):
    answer = random.randint(1, 100)
    guess_count = 1
    
    print("\nWelcome to The Number Guessing Game!!! Here's how it works:\n1. You guess a number between 1-100.\n2. I'll tell you if the number is higher or lower than your guess.\n3. Rinse & repeat. Keep guessing until you find the answer. I'll tell you how many guesses you took.")
    # Prevents high_score from being displayed until after first game
    if high_score < 100:
        print("The best so far is {} guesses. Can you do it in less?".format(high_score))
    
    
    while True:
        guess = input("\nWhat's your guess? ")
        
        
        try:
            guess = int(guess)
            # Handles gueeses outside 1-100
            if guess > 100 or guess < 1:
                raise ValueError()
        # Handles guesses that aren't numbers
        except ValueError:
            print("Sorry, you have to type digits between 1-100. ")
            continue
        else:
            if guess == answer:
                print("Got it! It took you {} guesses.".format(guess_count))
                # Checks for new high_score
                if guess_count < high_score:
                    high_score = guess_count
                break
            elif guess > answer:
                print("It's lower")
                guess_count += 1
                continue
            else:
                print("It's higher")
                guess_count += 1
                continue
    
    
    print("\nThank you for playing!")
    
    # Checks whether to keep playing or not.
    keep_playing = input("Would you like to play again? Yes/No ")
    if keep_playing.lower() == "yes" or keep_playing.lower() == "y":
        start_game(high_score)
    else:
        print("See you next time!")

# High score starts at 100, it should never take more than 100 guesses to get the right answer.
if __name__ == '__main__':
    start_game(100)
