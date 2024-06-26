"""
Author: Fathy Abdelshahid
Student ID: 32491328
Date Modified: 2024-06-07

Features:
- A welcome message and a prompt to start the game.
- Input validation for responses and guessed numbers.
- Hint system to guide the player towards the correct guess.
- Option to play again after guessing the correct number.

To play the game, simply run this script.

"""
import random


class luckyGuess:
    def __init__(self):
        """
        Initialize the game instances that might be needed to play the game.
        """
        # initialise the game instances that might be needed to play the game
        self.generated_number = self.randomgenerator()

    def message(self):
        """
        Displays the message at the start of the game and waits for the user to respond.
        If the response is 'Y', it proceeds to the game. If 'N', it keeps asking until 'Y' is received.
        """
        # displays the message at the start of the game
        counter = 0
        while True:
            if counter == 0:
                print(
                    "ARE YOU FEEEEEEELLLLLLINNNNNGGGG LUCKY?? Sounds like you are... why don't we put that to the test,"
                    " shall we? (Y/N) ")
                response = self.userInput()
            if counter == 1:
                print(
                    " well, im a betting man and Sounds like you are too since you have left yet"
                    " so lets begin shall we? (Y/N) ")
                response = self.userInput()

            if response == "Y":
                print("Well then, gather around and let's see how lucky you can be")
                print("Over here we have a number between 1 and 100, so lock in your guess:")
                break
            elif response == "N":
                print("Why are you scared or something? (Y/N)")
                response = self.userInput()
                if response == "Y":
                    print("No shame in that but too bad because you will still have to say yes regardless")
                    counter = 1
            else:
                print("Please enter Y or N.")

    def userInput(self):
        """
        Takes in responses that are words 'Y' or 'N' (case-insensitive) and returns the uppercase version.
        """
        # takes in responses that are words y or n // Y or N
        return input().strip().upper()

    def userNumberInput(self):
        """
        Handles the user input for guessing the number. Ensures the input is a valid integer between 1 and 100.
        """
        # in charge of handling what the user inputs in and returns it to be used
        while True:
            try:
                number = int(input())
                if 1 <= number <= 100:
                    return number
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Please enter a valid number i,e a number")

    def randomgenerator(self):
        """
        Generates and returns a random number between 1 and 100.
        """
        # generates and returns a number between 1 and 100 which is gonna be the number the player is gonna try to guess
        return random.randint(1, 100)

    def checker(self, generatedNumber, guessedNumber):
        """
        Checks if the guessed number is equal to the generated number.
        Provides hints if the guessed number is lower or higher than the generated number.

        Parameters:
        generatedNumber (int): The number generated by the random generator.
        guessedNumber (int): The number guessed by the user.

        Returns:
        bool: True if the guessed number is correct, False otherwise.
        """
        # going to check if the number we guessed is the number we generated if not
        # it will give the olayer a hint lower or higher depending on the values of the numbers ofc
        if guessedNumber < generatedNumber:
            print("Higher!")
        elif guessedNumber > generatedNumber:
            print("Lower!")
        else:
            return True
        return False
    def print_logo(self):
        """
        Prints the logo of the game.
        """

        logo = """Welcome toooooooooo........
        
=============================================================================================================        
        
        ▓██▓    ▓██   ██  ▄████▄   ██ ▄█▀░██   ██▓     ▄████  ▒██   ██▒ ▓█████    ▒█████   ▒█████ 
        ▓██▒    ▓██  ▓██░▒██▀ ▀█   ██▄█▒  ▒██  ██▒    ██▒ ▀█▒ ▒██  ▒██░ ▓█   ▀   ▒██    ▒ ▒██    ▒ 
        ▒██░    ▓██  ▒██░▒▓█    ▄ ░███▄░   ▒██▐██░   ▒██ ▄▄▄  ▒██  ▒██░ ▒███      ▓██▄     ▓██▄   
        ▒██░    ▓▓█  ░██░▒▓▓▄ ▄██ ░██ █▄   ░░▐██░    ░▓█  ██▓ ▐██  ░██░ ▒▓█  ▄   ▐█   ██▒ ▐█   ██▒
        ░██████▒▒▒█████▓ ░░▓███▀  ░██▒ █▄  ░░██▒░    ░▒▓███▀▒ ░▒█████▓  ░▒████▒   █████▒▒  █████▒▒
        ░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒  ░██▒▒░     ░▒    ▒ ░▒▓▒ ▒ ▒░ ░▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒
         ░ ░ ▒  ░░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░  ██▓░▒       ░   ░ ░░▒░ ░ ░   ░░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ░▒
           ░ ░    ░░░ ░ ░ ░        ░ ░░ ░  ░ ░ ░░     ░ ░      ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░   ░░
            ░  ░   ░     ░ ░      ░  ░    ░ ░  ░            ░    ░       ░  ░      ░         ░   ░
                         ░                ░ ░                                                    
=============================================================================================================                               
                     """
        print(logo)



    def run(self):
        """
        Runs the game loop, allowing the player to keep guessing until they get the correct number. If the player
        guesses correctly, it asks if they want to play again. If 'Y', the game restarts. If 'N', the game ends.
        """
        self.message()
        while True:
            guessed_number = self.userNumberInput()
            if self.checker(self.generated_number, guessed_number):
                print("Congratulations! You guessed the right number!")
                play_again = input("...Wanna go again? (Y/N) ").strip().upper()
                if play_again == "Y":
                    self.generated_number = self.randomgenerator()
                    self.message()
                else:
                    print("Thanks for playing! Till next time, Goodbye!")
                    break


# To start the game
if __name__ == "__main__":
    game_instance = luckyGuess()
    game_instance.print_logo()
    game_instance.run()
