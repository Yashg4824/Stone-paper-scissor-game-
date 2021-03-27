# Import random module
import random
print( 'Welcome to Stone - Paper - Scissor  Game')


# Input no. of rounds
n = int(input('Enter number of rounds: '))


# List containing option
options = ['st', 'p', 'sc']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0


# There will be n rounds of game
while rounds <= n:

	# Display round
	print(f"Round :{rounds}\nStone - 'st'\nPaper - 'p'\nScissor - 'sc'")

	# Exception handling
	try:
		player = input("Chose your option: ")
	except EOFError as e:
		print(e)

	# Control of bad inputs
	if player != 'st' and player != 'p' and player != 'sc':
		print("Invalid input, try again\n")
		continue

	# random.choice() will randomly chose
	# item from list- options
	computer = random.choice(options)

	# Conditions based on the game rule
	if computer == 'st':
		if player == 'sc':
			comp_win += 1
		elif player == 'p':
			user_win += 1

	elif computer == 'p':
		if player == 'st':
			comp_win += 1
		elif player == 'sc':
			user_win += 1

	elif computer == 'sc':
		if player == 'p':
			comp_win += 1
		elif player == 'st':
			user_win += 1

	# Announce winner of every round
	if user_win > comp_win:
		print(f"You Won round {rounds}\n")
	elif comp_win > user_win:
		print(f"Computer Won round {rounds}\n")
	else:
		print("Draw!!\n")

	rounds += 1


# Final winner based on the number of wons
if user_win > comp_win:
	print("Congratulations!! You Won")
elif comp_win > user_win:
	print("You lose!!")
else:
	print("Match Draw!!")
