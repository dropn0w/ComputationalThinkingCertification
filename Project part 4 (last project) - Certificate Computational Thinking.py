# For this exercice, we wneed to count the amount of time the words "happy" and "sad"
# and their synonyms appear in several documents

# here I will create an object with all words and its synonyms
class Entry :
  def __init__(self, word, synonyms) :
    self.word = word
    self.synonyms = synonyms

# Here I will start the fonction that I will need to use to print the keywords that
# I want to count

def search(keyword) :
  All_words = [keyword]

  # here I will create a list containing the keyword and its synonyms

  for Entry in Thesaurus:
    if keyword == Entry.word:
      for word in Entry.synonyms:
        All_words.append(word)
                
  # here I will count the number of times that the word and it synonyms appear and
  # stock the result in store

  store = []
  for search_word in All_words:
    count = 0
    for Doc in Corpus:
      for word in Doc:
        if search_word == word:
          count = count + 1
    store.append((search_word, count))
  return store # This is the return of my fonction. Example, if we are looking for word happy, the output will be: [('happy', 8)]

# Here are the inputs for this exercices: We need to count how many times happy, sad and their synonyms
# appear in the documents.

input = "happy"
output1 = search(input)
print(output1)

input = "sad"
output2 = search(input)
print(output2)
