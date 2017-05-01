import time

def game():
	state = False

	print("\n"*5)
	print("You stare at a screen")
	#time.sleep(5)
	print("")
	print("Words come at you")
	#time.sleep(7)
	print("\n"*2)
	print("At an alarmingly slow pace")
	#time.sleep(5)
	print("")
	print("You finally get the chance to type some shit into the computer")
	#time.sleep(1)
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


game()