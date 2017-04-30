import time

def game():
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

	inp = input("So you type some shit in: ").lower()
	greetings = ['hey', 'hi', 'hello', 'sup', 'yo',
				'howdy', 'hay']
	rude = ['poo', 'shit', 'fuck', 'fuck you', 'tit', 'tits',
			'cunt', 'boob', 'boobs', 'no', 'die']

	if inp in greetings:
		print("{} back at you!".format(inp.capitalize()))
	elif inp in rude:
		time.sleep(1)
		print("\n...")
		time.sleep(1)
		print("\n...That wasn't a very nice thing to say")
	else:
		print("You fucked up Josh")

game()