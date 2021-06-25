import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# TODO: Address the error that would occur if the user enters non-letter characters


def generate_phonetic():
    word_to_translate = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word_to_translate]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
