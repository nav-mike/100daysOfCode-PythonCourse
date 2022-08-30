import pandas
nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
alphabet = {row[1].letter:row[1].code for row in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ')

try:
    result = [alphabet[letter.title()] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet are supported.")
else:
    print(result)
