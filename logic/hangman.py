import random

class HangmanGame:
		"""
		HangmanGame class encapsulates the core logic for a game of Hangman.
		"""

		def __init__(self):
				"""
				Initialize game variables.
				"""
				self.phrases = [
						'Hard Pill to Swallow',
						'Hit Below The Belt',
						'A Cold Day in July',
						'Drive Me Nuts',
						'There\'s No I in Team',
						'Poke Fun At',
						'I Smell a Rat',
						'A Busy Body',
						'Wouldn\'t Harm a Fly',
						'Break The Ice'
				]
				self.current_phrase = ''
				self.guessed_letters = set()
				self.max_attempts = 6
				self.attempts = 0
				self.status = 'not_started'

		def startNewGame(self):
				"""
				Start a new game by randomly selecting a phrase and resetting variables.
				"""
				self.current_phrase = random.choice(self.phrases).upper()
				self.guessed_letters.clear()
				self.attempts = 0
				self.status = 'in_progress'

		def makeGuess(self, letter):
				"""
				Make a guess with the given letter.

				:param letter: The letter being guessed.
				:type letter: str
				"""
				if self.status != 'in_progress':
						return 'Game not in progress.'

				if len(letter) != 1 or not letter.isalpha():
					return 'Invalid guess. Please enter a single letter.'

				letter = letter.upper()

				if letter in self.guessed_letters:
						return 'Letter already guessed.'

				self.guessed_letters.add(letter)

				if letter not in self.current_phrase:
						self.attempts += 1
						if self.attempts >= self.max_attempts:
								self.status = 'lost'

				if all(char in self.guessed_letters or char == ' ' for char in self.current_phrase):
						self.status = 'won'

		def getGameStatus(self):
				"""
				Return the current status of the game.

				:return: The current status ('not_started', 'in_progress', 'won', 'lost').
				:rtype: str
				"""
				return self.status

		def getMaskedPhrase(self):
				"""
				Return the phrase with unguessed letters replaced by underscores.

				:return: The masked phrase.
				:rtype: str
				"""
				return ''.join([char if char in self.guessed_letters or char == ' ' else '_' for char in self.current_phrase])

def runHangmanCLI():
		"""
		Run the Hangman game with a Command Line Interface (CLI).
		"""
		game = HangmanGame()
		game.startNewGame()

		print("\n\033[92m\033[1mWelcome to Hangman CLI!\033[0m\n")  # Green bold
		print(f"\033[93mPhrase to guess: {game.getMaskedPhrase()}\033[0m\n")  # Yellow

		while game.getGameStatus() == 'in_progress':
				guess = input("\033[96mEnter your guess (single letter): \033[0m")  # Cyan

				feedback = game.makeGuess(guess)
				if feedback:
						print(f"\t\033[91m{feedback}\033[0m")  # Red

				print(f"\033[93m\nPhrase to guess: {game.getMaskedPhrase()}\033[0m")  # Yellow
				print(f"\t\033[95mGuessed letters: {', '.join(game.guessed_letters)}\033[0m")  # Magenta
				print(f"\t\033[94mRemaining attempts: {game.max_attempts - game.attempts}\033[0m\n")  # Blue

				if game.getGameStatus() == 'won':
						print("\033[92m\033[1mCongratulations, you won!\033[0m")  # Green bold
						break
				elif game.getGameStatus() == 'lost':
						print("\033[91m\033[1mYou lost. Better luck next time!\033[0m")  # Red bold
						print(f"\033[91mThe phrase was: {game.current_phrase}\033[0m")  # Red
						break

if __name__ == '__main__':
		runHangmanCLI()
