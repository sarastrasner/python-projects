import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_translate = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word_to_translate]
print(output_list)
