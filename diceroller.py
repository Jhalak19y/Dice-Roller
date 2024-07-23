 #import random module that will generate random numbers
import random

# Define a function to roll the dice
def roll_dice():
  return random.randint(1,6)

# Define a function to display the dice image
def display_dice_image(value):
  dice_faces = {
    1: ("+-------+",
        "|       |",
        "|   *   |",
        "|       |",
        "+-------+"),
    2: ("+-------+",
        "| *     |",
        "|       |",
        "|     * |",
        "+-------+"),
    3: ("+-------+",
        "| *     |",
        "|   *   |",
        "|     * |",
        "+-------+"),
    4: ("+-------+",
        "| *   * |",
        "|       |",
        "| *   * |",
        "+-------+"),
    5: ("+-------+",
        "| *   * |",
        "|   *   |",
        "| *   * |",
        "+-------+"),
    6: ("+-------+",
        "| *   * |",
        "| *   * |",
        "| *   * |",
        "+-------+")
  }
  for line in dice_faces[value]:
    print(line)

# Define a function to start the game
def start_rolling():
  # Ask user if they want to roll the dice
  start_rolling = input("Roll the dice? (y/n):")
  # If user enters "y", roll the dice and display the image 
  if start_rolling == "y":
    print("Rolling the dice...")
    value = roll_dice()
    print(f"The value is: {value}")
    display_dice_image(value)
    # Ask user if they want to roll the dice again
    start_rolling = input("Roll the dice again? (y/n):")
      # If user enters "n", end the game
      if start_rolling == "n":
        print("Thanks for playing!")
