# Capstone Project: Flashcard App


# Feature Tasks
1. Create the User Interface with Tkinter
1. Create new flash cards
   1. Read the data from the `french_words.csv` file in the data folder.
   1. Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ 
      buttons, it should generate a new random word to display.
1. Flip the cards
   1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
   1. The card image should change to the `card_back.png` and the text color should change to white. 
      The title of the card should change to "English" from "French".
1. Save the user's progress
   1. If the user selects the checkmark, they know the card.
   1. Remove that card from the list of possible options
