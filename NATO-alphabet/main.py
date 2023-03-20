import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(result)


def generate_phonetic():
    word = input("Enter a word: ")
    word = word.upper()
    try:
        nato_list = [result[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
