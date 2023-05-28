
import nltk
from nltk.corpus import words




def generateWordsList(lowerLen,upperLen):
  nltk.download("words")
  # Load the list of English words
  word_list = words.words()

  specList = [item for item in word_list if lowerLen <= len(item) <=upperLen]
  return specList