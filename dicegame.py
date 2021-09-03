from random import randint
import time
welcome = input("hi,ur welcome in dice_game , do u wanna play with me?  ")
roll_again = "yes"
while roll_again == "yes" or roll_again =="Yes" or roll_again =="YES":
	if welcome == "yes" or welcomme =="Yes" or welcome == "YES":
		print ("Let's go!")
		print("bot's turn")
		time.sleep (2)
		bot_result = randint(1,6)
		print(f"bot's result is: {bot_result}")
		time.sleep (1)
		roll_dice = input("Now it's ur turn \nWrite \'throw\' or \'go\' to start roll dice : ")
		if roll_dice == "throw" or roll_dice == "Throw" or roll_dice == "THROW" or roll_dice == "go":
			player_result = randint(1,6)
			time.sleep (2)
			print(player_result)
			if player_result > bot_result:
				print("u win")
			if player_result < bot_result:
				print("U loose")
			if player_result == bot_result :
				print("Tie")
			roll_again= input("do u wanna play again?")
			if roll_again == "no" or roll_again =="NO" or roll_again == "No":
				print("Good bye:3")