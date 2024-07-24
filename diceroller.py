import random

# Define a function to roll the dice
def roll_dice():
    return random.randint(1, 6)

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
    while True:
        start_rolling = input("Roll the dice? (y/n): ")
        if start_rolling.lower() == "y":
            print("Rolling the dice...")
            value = roll_dice()
            print(f"The value is: {value}")
            display_dice_image(value)
        elif start_rolling.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Start the game
start_rolling()
