# Higher or Lower Game for celebritie's followers on instagram
# Imports
import random
from art import logo
from game_data import data
from replit import clear

# Functions
def random_celebrity():
  """Returns a random celebrity from the list of celebrities"""
  return random.choice(data)

def compare_followers(celebrity_a, celebrity_b):
  """Compares the followers of two celebrities and returns the celebrity with more followers"""
  if celebrity_a['follower_count'] > celebrity_b['follower_count']:
    return celebrity_a
  else:
    return celebrity_b

def game():
  """The main game function"""
  # Print logo
  print(logo)
  # Initialize score
  score = 0
  # Initialize game_over
  game_over = False
  # Initialize celebrity_a
  celebrity_a = random_celebrity()
  # While loop to keep playing the game until the user loses
  while not game_over:
    # Print celebrity A
    print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}")
    # Print vs
    print("vs")
    # Initialize celebrity_b
    celebrity_b = random_celebrity()
    # While loop to make sure celebrity_b is not the same as celebrity_a
    while celebrity_b == celebrity_a:
      celebrity_b = random_celebrity()

    # Print celebrity B
    print(f"Against B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']}")
    # Ask user to guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Compare followers of celebrity_a and celebrity_b 
    winner = compare_followers(celebrity_a, celebrity_b)
    # If user guesses correctly, increase score by 1 and make celebrity_a the winner
    if guess == 'a' and winner == celebrity_a:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
      celebrity_a = winner

    # If user guesses correctly, increase score by 1 and make celebrity_a the winner
    elif guess == 'b' and winner == celebrity_b:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
      celebrity_a = winner
    # If user guesses incorrectly, end game and print final score
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True

# Call game function
game()
