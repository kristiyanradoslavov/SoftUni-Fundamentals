import random

win = False
draw = False
loose = False
game_is_won = False

game_counter = 1
win_counter = 0
loose_counter = 0
draw_counter = 0

computer_result_options = ["rock", "paper", "scissors"]
computer_result = random.choice(computer_result_options)

# game rules
print()
print("Game of rock, paper and scissors, choose one and type it in the field bellow !")
print("Rules: You will play 5 games and if you win 3 points you will win the entire game. "
      "Else the game will be lost. Each win will earn you 1 point.\n")

# start of 1st game
print(f"Game {game_counter}")
player_input = input("Type in your selection: ")
player_choice = player_input.lower()

# This while cycle is supposed to print to the player an Error message\
# when the player enters an input different from the computer result options.
while player_choice not in computer_result_options:
    print("Unknown selection, you must choose from: 'rock', 'paper' or 'scissors'.")
    player_input = input("Type in your selection: ")
    player_choice = player_input.lower()

# Here is the whole information of every possible outcome of the game
for count_of_games in range(1, 6):
    if player_choice == computer_result:
        draw = True
        draw_counter += 1
    elif player_choice == "rock" and computer_result == "paper":
        loose = True
        loose_counter += 1
    elif player_choice == "rock" and computer_result == "scissors":
        win = True
        win_counter += 1
    elif player_choice == "paper" and computer_result == "rock":
        win = True
        win_counter += 1
    elif player_choice == "paper" and computer_result == "scissors":
        loose = True
        loose_counter += 1
    elif player_choice == "scissors" and computer_result == "rock":
        loose = True
        loose_counter += 1
    elif player_choice == "scissors" and computer_result == "paper":
        win = True
        win_counter += 1

    if win:
        print(f"Computer`s choice is: {computer_result}")
        print(f"You Win!")
        print(f"Win counter: {win_counter}  Loose counter: {loose_counter}  Draw counter: {draw_counter}\n")
    elif loose:
        print(f"Computer`s choice is: {computer_result}")
        print(f"You Loose!")
        print(f"Win counter: {win_counter}  Loose counter: {loose_counter}  Draw counter: {draw_counter}\n")
    elif draw:
        print(f"Computer`s choice is: {computer_result}")
        print(f"It`s a draw!")
        print(f"Win counter: {win_counter}  Loose counter: {loose_counter}  Draw counter: {draw_counter}\n")

    game_counter += 1
    win = False
    draw = False
    loose = False

    if win_counter == 3:
        game_is_won = True
        break
    # this if statements are supposed to break the outcome if the game all 5 games have been successfully played
    # also it is supposed to break if a player has played 3 games with no win, or  4 games with 1 win.
    if game_counter == 6:
        break
    elif game_counter == 4 and win_counter < 1:
        break
    elif game_counter == 5 and win_counter < 2:
        break

# Start of the next game
    print(f"Game {game_counter}")
    player_input = input("Type in your selection: ")
    player_choice = player_input.lower()
    computer_result = random.choice(computer_result_options)
    while player_choice not in computer_result_options:
        print("Unknown selection, you must choose from: 'rock', 'paper' or 'scissors'.")
        player_input = input("Type in your selection: ")
        player_choice = player_input.lower()
    # End of the start

if game_is_won:
    print(f"You won {win_counter} points. You win the entire game! Congratulations.")
else:
    print("You didn`t manage to win 3 points. You loose! Good luck next time.")