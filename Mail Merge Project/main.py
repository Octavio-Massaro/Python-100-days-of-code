# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_names = []
text_names = ""

with open("./input/Names/invited_names.txt") as file:
    text_names = file.read()
    list_names = text_names.split("\n")

text_sample = ""

for names in list_names:
    with open("./input/Letters/starting_letter.txt") as file2:
        text_sample = file2.read()
    with open(f"./Output/ReadyToSend/letter_for_{names}.txt", "w") as file3:
        text_sample = text_sample.replace("[name]", f"{names}")
        file3.write(text_sample)
