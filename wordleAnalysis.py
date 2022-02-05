import wordleAI


# def buildLetterDictionary(word):
#     dictionary = {}
#     for letter in word:
#         if letter not in dictionary.keys():
#             dictionary[letter] = 1
#         else:
#             dictionary[letter] += 1
#     return dictionary


# load word list
gameWordLength = 5
gameWords = wordleAI.initializeWordList(gameWordLength)

# generate letter histograms
letterHistogram = {}
for word in gameWords:
    for letter in word:
        if letter not in letterHistogram.keys():
            letterHistogram[letter] = 1
        else:
            letterHistogram[letter] += 1

# get the largest letters for the game size
letterHistogram = sorted(letterHistogram, key=letterHistogram.get, reverse=True)
print(letterHistogram[:5])