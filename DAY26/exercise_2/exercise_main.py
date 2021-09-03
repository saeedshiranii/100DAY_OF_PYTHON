sentence = input('enter your sentence: ')
split_sentence = sentence.split()
name_dict = {word: len(word) for word in split_sentence}
print(name_dict)
