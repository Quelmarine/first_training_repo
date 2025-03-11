import random

print("Hi! Lets play Rock Paper Scissors! ")
print("")
pick = (str(input("Choose your option! (Rock, Paper, Scissors) :   ")))
print("")

game = [ "rock", "paper", "scissors"]
computer_guess = random.choice(game)
game_image = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,  # Rock

    """
    _______
---'   ____)____
          _______)
          ________)
         ________)
---.__________)
    """,  # Paper

    """
    _______
---'    ____)____
           ______)
       __________)
      (____)
---.__(___)
    """  # Scissors
]



if  computer_guess == "rock":

  print(f"I've picked Rock, {game_image[0]}")

elif  computer_guess == "paper":

    print(f"I have picked a Paper, {game_image[1]} ")

else:
    print(f"I have picked a Scissors, {game_image[2]} ")

if  pick.lower() == "rock":
   
   print(f"You've picked Rock, {game_image[0]}")


elif  pick.lower() == "paper":

   print(f"You've picked Rock, {game_image[1]}")


else:
  print(f"You've picked Rock, {game_image[2]}")

print("")


if pick.lower() == computer_guess:
   print(" It's a tie!")
elif (pick.lower() == "rock") and (computer_guess == "paper"):
   print("haha I won! ")
elif (pick.lower() == "paper") and (computer_guess == "scisors"):
   print("haha I won! ")
elif (pick.lower() == "scissors") and (computer_guess == "rock"):
   print("haha I won! ")
else:
   print("Congrats, You win this time!")

