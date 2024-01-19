#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from guessnumber_logo import logo

print (logo)

# Global Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to guess the pkayer's number
def guess_number(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high")
    return turns -1
    
  elif guess < answer:
    print("Too low")
    return turns -1
    
  else:
    print(f"You got it! The answer was {answer}")

# Function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS
  else:
    print("Invalide level input! \n Try again.")

def guess_game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100. ")
  answer = random.randint(1,100)
  print(answer)
  turns = set_difficulty()
 
  
  # Allow the player to submit a guess for a number between 1 and       100.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the              number.")
    guess = int(input("Guess a number between 1 and 100: "))
    turns = guess_number(guess, answer, turns)

    if turns == 0:
      print("You run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

guess_game()


