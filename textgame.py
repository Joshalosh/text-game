import time

def intro():
	state = False

	print("\n"*5)
	print("You stare at a screen")
	time.sleep(5)
	print("")
	print("Words come at you")
	time.sleep(7)
	print("\n"*2)
	print("At an alarmingly slow pace")
	time.sleep(5)
	print("")
	print("You finally get the chance to type some shit into the computer")
	time.sleep(1)
	while state != True:
		inp = input("\nSo you type 'Begin': ").lower()
		greetings = ['hey', 'hi', 'hello', 'sup', 'yo',
					'howdy', 'hay', 'hey there']
		rude = ['poo', 'shit', 'fuck', 'fuck you', 'tit', 'tits',
				'cunt', 'boob', 'boobs', 'no', 'die']
		number = ['1', '2', '3', '4',' 5', '6', '7', '8', '9', '0']
		vowels = ['a', 'e', 'i', 'o', 'u','y']

		if not inp:
			print('\nWell you have to type something')
		elif inp == 'begin':
			state = True
		elif inp in greetings:
			print("{} back at you!".format(inp.capitalize()))
		elif inp in rude:
			time.sleep(1)
			print("\n...")
			time.sleep(1)
			print("\n...That wasn't a very nice thing to say")
		elif inp[0] in number:
			print("So you're a maths nerd huh?")
		elif any(char in vowels for char in list(inp)):
			print("{} has nothing to do with this".format(inp.capitalize()))
		else:
			print("Well that isn't even a word")


def game():
	time.sleep(1)
	print("\n...")
	time.sleep(1)
	print("\n...")
	time.sleep(1)
	print("\n...")
	time.sleep(2)
	print("\nThe computer seems to be initialising something")
	time.sleep(1)
	print("\nQuick say the first thing that pops into your head!")
	time.sleep(5)
	print("\nYou have to physically say it into the laptop microphone")
	time.sleep(8)
	print("\nWow that's a really weird thing to be thinking")
	time.sleep(2)
	print("\nAlso this program can't actually register your voice or anything")
	time.sleep(2)
	print("\nI just made you say something random and look like a weirdo")
	time.sleep(2)
	print("\nin fact that was really what all this was about")
	time.sleep(2)
	print("\nCongratulations! You win the game")
	time.sleep(2)
	print("\nBut at what cost?\n")
	time.sleep(100000000)

intro()
game()
