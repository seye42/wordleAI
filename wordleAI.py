import re


def loadWordList(fileName):
    fileDesc = open(fileName, 'r')
    words = fileDesc.read().splitlines()
    fileDesc.close()
    return words


def filterByLength(allWords, length):
    filteredWords = []
    for word in allWords:
        if len(word) == length:
            filteredWords.append(word)
    return filteredWords


def filterByExcludedLetters(allWords, excludedLetters):
    pattern = re.compile('^[^' + excludedLetters + ']+$')
    filteredWords = []
    for word in allWords:
        if pattern.match(word):
            filteredWords.append(word)
    return filteredWords


def filterByIncludedLetters(allWords, includedLetters):
    patternString = ''
    for letter in includedLetters:
        patternString += '(?=.*' + letter + ')'
    pattern = re.compile(patternString)
    filteredWords = []
    for word in allWords:
        if pattern.match(word):
            filteredWords.append(word)
    return filteredWords


def filterByMispositionedLetters(allWords, mispositionedLetters):
    patternString = '^'
    for letter in mispositionedLetters:
        if letter == '?':
            patternString += '.'
        else:
            patternString += '[^' + letter + ']'
    pattern = re.compile(patternString)
    filteredWords = []
    for word in allWords:
        if pattern.match(word):
            filteredWords.append(word)
    return filteredWords


def filterByPositionedLetters(allWords, positionedLetters):
    pattern = re.compile(positionedLetters.replace('?', '[A-Z]'))
    filteredWords = []
    for word in allWords:
        if pattern.match(word):
            filteredWords.append(word)
    return filteredWords


def initializeWordList(gameWordLength=5):
    # load the dictionary of all valid words
    allWords = loadWordList(r'dictionary.txt')

    # filter down to only the five letter long words
    return filterByLength(allWords, gameWordLength)


def play():
    gameWordLength = 5
    gameWords = initializeWordList(gameWordLength)
    initWordCount = len(gameWords)

    while True:
        # prompt for game state elements
        excLetters = input('excluded:      ')
        misLetters = input('mispositioned: ')
        posLetters = input('positioned:    ')

        # condition inputs
        excLetters = ''.join(sorted(excLetters.upper()))  # sort and uppercase
        misLetters = misLetters.upper()
        if len(misLetters) != gameWordLength:  # malformed, prompt again
            continue
        incLetters = misLetters.replace('?', '')
        posLetters = posLetters.upper()
        if len(posLetters) != gameWordLength:  # malformed, prompt again
            continue

        # TODO: consider cross-validating inputs for consistency:
        #       * non-empty intersection of include and exclude sets
        #       * non-? in positional string are consistent with include and exclude sets

        # apply filters for excluded letters, included letters, and position-fixed letters
        prevWordCount = len(gameWords)
        gameWords = filterByExcludedLetters(gameWords, excLetters)
        gameWords = filterByIncludedLetters(gameWords, incLetters)
        gameWords = filterByMispositionedLetters(gameWords, misLetters)
        gameWords = filterByPositionedLetters(gameWords, posLetters)
        print(gameWords)
        print('%d/%d words left, %0.1f%% reduction in last play' \
              % (len(gameWords), initWordCount, float(prevWordCount - len(gameWords)) / prevWordCount * 100.0))

    return