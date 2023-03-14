import pandas
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(result)

word = input("Enter a word: ")
word = word.upper()

nato_list = [result[letter] for letter in word]

print(nato_list)
