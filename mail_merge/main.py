# TODO: Create a letter using starting_letter.txt
# TODO: for each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend".
# letter_for_[person's name]

# TODO: Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# TODO: Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# TODO: Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt', mode="r") as letter:
    contents = letter.read()
    # TODO: Do the replacing here
    with open('./Input/Names/invited_names.txt') as file:
        names = file.readlines()
        for name in names:
            stripped_name = name.strip()
            file_name = stripped_name.replace(" ", "_")
            new_letter = contents.replace("[name]", f"{stripped_name}")
            if file_name:
                with open(f"letter_for_{file_name}.txt", mode="w") as new_file:
                    new_file.write(f"{new_letter}")
            else:
                with open(f"letter_for_{stripped_name}.txt", mode="w") as new_file:
                    new_file.write(f"{new_letter}")