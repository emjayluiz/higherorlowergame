from game_data import data
import random
from art import logo, vs

win_streak = 0
game_continue = True

def choice1(data):
  choice = random.choice(data)
  return choice

def choice2(data):
  choice = random.choice(data)
  return choice

for key, value in choice1(data).items():
  if key == 'name':
    name = value
  elif key == 'follower_count':
    followers_choice1 = value

for key, value in choice2(data).items():
  if key == 'name':
    name = value
  elif key == 'follower_count':
    followers_choice2 = value

print(logo)


while game_continue:
    choice1_data = choice1(data)
    choice2_data = choice2(data)

    followers_choice1 = choice1_data['follower_count']
    followers_choice2 = choice2_data['follower_count']

    print(f"Who has a higher follower count \nA: {choice1_data['name']} {vs}B: {choice2_data['name']}: \n")
    guess = input().lower()

    if (guess == "a" and followers_choice1 > followers_choice2) or (guess == "b" and followers_choice2 > followers_choice1):
        print("You got it right")
        win_streak += 1
        print("Win streak:", win_streak)
    else:
        print("You got it wrong")
        print("Your score:", win_streak)
        game_continue = False
        win_streak = 0
