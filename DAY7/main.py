# hangman game :)))))

# i use random library for choose the word
import random
import check_letter # if u cannot find it go to the github
from master import master_list #this is for choose random from a huge list


# 1:: first we should choose randomly a word

# 2:: get a letter from user and macth it with letters of that word we choosed

# 3:: tell to the user are the letter correct or not
#     and if it is that is macth with which element of our geuss


# choose a random word
choosen_word = random.choice(master_list)
print(choosen_word)

check_letter.check(choosen_word)
