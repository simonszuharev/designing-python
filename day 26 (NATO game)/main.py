# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_words = {row.letter: row.code for (index, row) in data.iterrows()}
print(letter_words)

name = input("Enter a word: ").upper()
nato_list = [letter_words[letter] for letter in name]
print(nato_list)
