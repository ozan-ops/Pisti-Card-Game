Pişti Card Game
This Python program simulates the traditional Turkish card game "Pişti." The game involves two players who compete to capture cards from a central pile by matching the rank of the cards they play with the top card in the pile. The program handles card dealing, player moves, and determines the winner based on the number of cards captured.

Description
The Pişti card game is played with a standard deck of 52 cards. The game includes the following components:

Card Class: Represents individual cards.
Deck Class: Creates and shuffles the deck.
Player Class: Manages player actions and card hands.
MiddlePile Class: Manages cards in the middle.
CapturedCards Class: Keeps track of captured cards.
Game Functions: Deal cards, show cards, play cards to the middle pile, and check for captures.
Usage
To use this program, run the script and follow the on-screen prompts to play the game. Players will be asked to input the cards they wish to play.

Example
python
Kodu kopyala
import random

# Importing random module and defining card suits and ranks
...

# Main game loop
while True:
    print("WELCOME TO PİŞTİ CARD GAME!!!")
    ...

    # Game loop
    game = True
    while game:
        print("Cards in the middle: ")
        ...
Acknowledgments
This program was inspired by the traditional Turkish card game "Pişti."
