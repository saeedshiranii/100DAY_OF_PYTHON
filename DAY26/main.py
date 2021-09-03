import pandas

""" read a csv file a convert it to a dictionary at this format {'A': Alpha}"""
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(phonetic_dict)

""" get a word or letter from user to make it phonetic """
name = input('enter your name: ').upper()
final_list = [phonetic_dict[letter] for letter in name]
print(final_list)
