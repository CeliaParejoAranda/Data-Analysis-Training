from csv import reader
from random import choice
import time
import termcolor as t
import colorama as col 
col.init()

def ing():
	mode = input('Do you want to spell in English or in Spanish? (E/S)\n')
	while mode.upper() not in ('E', 'S'): 	
		print('Mode must be E or S')
		mode = input('Do you want to spell in English or in Spanish? (E/S)\n')
			
	else:

		if mode.upper() == 'E':

			with open('voc.csv') as file:
				csv_reader = reader(file)
				mydict = {word[0]:word[1] for word in csv_reader}
				esp = [value for value in mydict.keys()]

				words = len(esp)
				points = 0
				lives = 3
				tries = 0
				bonus = 0

				not_guessed = []

#
				while True:
					while words>0 and lives>0:
						question = choice(esp)
						answer = mydict[question]
						user = input(f"What is the word for... '{question}' in English? ({len(answer.split())} words)\n")
						
						if user.lower() == answer:
							which = esp.index(question)
							esp.pop(which)
							points += 1
							words -= 1
							bonus += 1
							t.cprint("Well done!", 'green', None, ['bold'])
							
							
							if points % 10 == 0:
								t.cprint('Great! You are on a roll!', 'green', None, ['bold'])
							elif points % 5 == 0:
								t.cprint("Yay! Let's do five more!", 'green', None, ['bold'])
							
							if bonus == 5:
								lives += 1
								t.cprint("You have one extra life!", 'magenta', None, ['bold'])
								bonus -= 5
								
						elif user.lower() == 'quit':
							t.cprint('\nI hope to see you soon!', 'blue', None, ['bold'])
							t.cprint('\nBefore you go, reread these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')
							time.sleep(12)
							exit()						

						else:
							if tries == 0:
								print(f"Hint: the word you are looking for starts with '{answer[0]}'")
								tries += 1
								question = question
								user = input(f"What is the word for... '{question}' in English?\n")
								
								if user.lower() == answer:
									which = esp.index(question)
									esp.pop(which)
									points += 1
									words -= 1
									tries -= 1
									bonus += 1
									t.cprint("Well done!", 'green', None, ['bold'])
									

									if points % 10 == 0:
										t.cprint('Great! You are on a roll!', 'green', None, ['bold'])
									elif points % 5 == 0:
										t.cprint("Yay! Let's do five more!", 'green', None, ['bold'])

									if bonus == 5:
										lives += 1
										t.cprint("You have one extra life!", 'magenta', None, ['bold'])
										bonus -= 5
										

								else:
									print(f"Ups! Remember: {question} is '{answer}'")
									lives -= 1
									tries -= 1
									bonus -= bonus
									not_guessed.append(question)
									print(f'You have {lives} live(s)!\n')
							
							else:
								print(f"Ups! Remember: {question} is '{answer}'")
								question = choice(esp)
								lives -= 1
								tries -= 1
								bonus -= bonus
								not_guessed.append(question)
								print(f'You have {lives} live(s)!\n')

		
					else:
						if words > 0 and points != 0:
							t.cprint('\n****GAME OVER!***', 'red', None, ['bold'])
							print(f'You have guessed {points} word(s), nice job!')
							t.cprint('\nI encourage you to revise these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')

							newgame = input('\nDo you want to play again? (y/n)\n')
							while newgame.lower() not in ('y', 'n'):
								print("Answer must be 'y' or 'n'")
								newgame = input('\nDo you want to play again? (y/n)\n')
							else:
								if newgame.lower() == 'y':
									mydict = {word[0]:word[1] for word in csv_reader}
									esp = [value for value in mydict.keys()]
									words = len(esp)
									points = 0
									lives = 3
									tries = 0
									bonus = 0
									not_guessed = []
									ing()
								
								elif newgame.lower() == 'n':
									break
								break			
									
						elif words > 0 and points == 0:
							t.cprint('\n***GAME OVER!***', 'red', None, ['bold'])
							print(f'You have guessed {points} word(s)\nKeep on trying! You will do better next time')
							t.cprint('\nI encourage you to revise these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')

							newgame = input('\nDo you want to play again? (y/n)\n')
							while newgame.lower() not in ('y', 'n'):
								print("Answer must be 'y' or 'n'")
								newgame = input('\nDo you want to play again? (y/n)\n')
							else:
								if newgame.lower() == 'y':
									mydict = {word[0]:word[1] for word in csv_reader}
									esp = [value for value in mydict.keys()]
									words = len(esp)
									points = 0
									lives = 3
									tries = 0
									bonus = 0
									not_guessed = []
									ing()
								
								elif newgame.lower() == 'n':
									break
								break

					if words == 0:
						t.cprint('\n***Congratulations! You have learnt all the words I can teach you!***', 'green', None, ['bold'])
						t.cprint('Keep up the great work!', 'green', None, ['bold'])
						break
					break	


		elif mode.upper() == 'S':

			with open('voc.csv') as file:
				csv_reader = reader(file)
				mydict = {word[1]:word[0] for word in csv_reader}
				esp = [value for value in mydict.keys()]

				words = len(esp)
				points = 0
				lives = 3
				tries = 0
				bonus = 0
				
				not_guessed = []

#
				while True:
					while words>0 and lives>0:
						question = choice(esp)
						answer = mydict[question]
						user = input(f"What is the word for... '{question}' in Spanish? ({len(answer.split())} words)\n")
						
						if user.lower() == answer:
							which = esp.index(question)
							esp.pop(which)
							points += 1
							words -= 1
							bonus += 1
							t.cprint("Well done!", 'green', None, ['bold'])

							if points % 10 == 0:
								t.cprint('Great! You are on a roll!', 'green', None, ['bold'])
							elif points % 5 == 0:
								t.cprint("Yay! Let's do five more!", 'green', None, ['bold'])

							if bonus == 5:
								lives += 1
								t.cprint("You have one extra life!", 'magenta', None, ['bold'])
								bonus -= 5

						elif user.lower() == 'quit':
							t.cprint('\nI hope to see you soon!', 'blue', None, ['bold'])
							t.cprint('\nBefore you go, reread these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')
							time.sleep(12)
							exit()

						else:

							if tries == 0:
								print(f"Hint: the word you are looking for starts with '{answer[0]}'")
								tries += 1
								question = question
								user = input(f"What is the word for... '{question}' in Spanish?\n")

								if user.lower() == answer:
									which = esp.index(question)
									esp.pop(which)
									points += 1
									words -= 1
									tries -= 1
									bonus += 1
									t.cprint("Well done!", 'green', None, ['bold'])
									
									if points % 10 == 0:
										t.cprint('Great! You are on a roll!', 'green', None, ['bold'])
									elif points % 5 == 0:
										t.cprint("Yay! Let's do five more!", 'green', None, ['bold'])

									if bonus == 5:
										lives += 1
										t.cprint("You have one extra life!", 'magenta', None, ['bold'])
										bonus -= 5

								else:
									print(f"Ups! Remember: {question} is '{answer}'")
									lives -= 1
									tries -= 1
									bonus -= bonus
									not_guessed.append(question)
									print(f'You have {lives} live(s)!\n')

							else:
								print(f"Ups! Remember: {question} is '{answer}'")
								question = choice(esp)
								lives -= 1
								tries -= 1
								bonus -= bonus
								not_guessed.append(question)
								print(f'You have {lives} live(s)!\n')
		
					else:
						if words > 0 and points != 0:
							t.cprint('\n***GAME OVER!***', 'red', None, ['bold'])
							print(f'You have guessed {points} word(s), nice job!')
							t.cprint('\nI encourage you to revise these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')
									
							newgame = input('\nDo you want to play again? (y/n)\n')
							while newgame.lower() not in ('y', 'n'):
								print("Answer must be 'y' or 'n'")
								newgame = input('\nDo you want to play again? (y/n)\n')
							else:
								if newgame.lower() == 'y':
									mydict = {word[1]:word[0] for word in csv_reader}
									esp = [value for value in mydict.keys()]
									words = len(esp)
									points = 0
									lives = 3
									tries = 0
									bonus = 0
									not_guessed = []
									ing()

								elif newgame.lower() == 'n':
									break
								break
				
						
						elif words > 0 and points == 0:
							t.cprint('\n***GAME OVER!***', 'red', None, ['bold'])
							print(f'You have guessed {points} word(s)\nKeep on trying! You will do better next time')
							t.cprint('\nI encourage you to revise these terms:', 'green', None, ['bold'])
							for word in not_guessed:
								print(f'*{word}: {mydict[word].upper()}')

							newgame = input('\nDo you want to play again? (y/n)\n')
							while newgame.lower() not in ('y', 'n'):
								print("Answer must be 'y' or 'n'")
								newgame = input('\nDo you want to play again? (y/n)\n')
							else:
								if newgame.lower() == 'y':
									mydict = {word[1]:word[0] for word in csv_reader}
									esp = [value for value in mydict.keys()]
									words = len(esp)
									points = 0
									lives = 3
									tries = 0
									bonus = 0
									not_guessed = []
									ing()
									
								elif newgame.lower() == 'n':
									break
								break

					if words == 0:
						t.cprint('\n***You have learnt all the words I can teach you! Congratulations!***', 'green', None, ['bold'])
						t.cprint('Keep up the great work!', 'green', None, ['bold'])
						break
					break
ing()

