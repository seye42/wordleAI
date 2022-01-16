import re

def loadDictionary(fileName):
    fileDesc = open(fileName, 'r')
    words = fileDesc.read().splitlines()
    fileDesc.close()
    return words


def buildLetterDictionary(word):
    dictionary = {}
    for letter in word:
        if letter not in dictionary.keys():
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    return dictionary


# load the dictionary of all valid words
allWords = loadDictionary(r'dictionary.txt')

while True:
    # get the level's letter set
    levelLetters = input('letter set: ')
    levelLetters = ''.join(sorted(levelLetters.upper()))
    levelDict = buildLetterDictionary(levelLetters)
    numLevelLetters = len(levelLetters)

    # build the level's word list
    levelWords = []
    for word in allWords:
        # bail early if there are more letters than are available
        if len(word) > numLevelLetters:
            continue

        # compare letter dictionaries and add it to the list
        wordDict = buildLetterDictionary(word)
        canBuild = True
        for key in wordDict.keys():
            if key not in levelDict.keys() or wordDict[key] > levelDict[key]:
                canBuild = False
                break
        if canBuild:
            levelWords.append(word)

    # sort by length and print them out
    levelWords = sorted(levelWords, key=len)
    for word in levelWords:
        print(word)

    # repeatedly prompt for patterns
    while True:
        # get the pattern string
        patternStr = input('pattern: ').upper()
        if len(patternStr) == 0:
            break

        # build the regular expression for matching
        pattern = re.compile('\A' + patternStr.replace('?', '[A-Z]') + '\Z')

        # test each level word against the pattern and print matches
        for word in levelWords:
            if pattern.match(word):
                print(word)