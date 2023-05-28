import random
from generateWordsList import generateWordsList
from choose_word import choose_word
from play import play

specList = generateWordsList(3,8)
words_num = int(input("Please enter words count: "))
words = []
for i in range(0,words_num):
  words.append(specList[random.randint(0,len(specList))])


# print(words)


# List of words to choose from
# words = ["python", "programming", "computer", "science", "mathematics", "data", "code","shinetech"]

# Driver code
word = choose_word(words)
play(word)

