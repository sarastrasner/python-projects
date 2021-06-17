PLACEHOLDER = "[name]"

# TODO: Create a letter using starting_letter.txt
with open('./Input/Letters/starting_letter.txt', mode="r") as letter:
    contents = letter.read()

# TODO: Replace the [name] placeholder with the actual name.
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()
    # TODO: for each name in invited_names.txt
    for name in names:
        stripped_name = name.strip()
        file_name = stripped_name.replace(" ", "_")
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        # TODO: Save the letters in the folder "ReadyToSend" with a filename of "letter_for_[person's name]".
        if file_name:
            with open(f"./Output/ReadyToSend/letter_for_{file_name}.txt", mode="w") as new_file:
                new_file.write(f"{new_letter}")
        else:
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_file:
                new_file.write(f"{new_letter}")
