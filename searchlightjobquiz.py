# Searchlight Job Quiz -- Luke Ilsley
testCase = "Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country’s done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail."

# can change the case later without needing to alter the test case
stringSICS = testCase


def sortCountChar(chars):
    # Creation a dictionary of characters and how often they are used
    # Doing this via something like a list would be very ineficient.

    # After coming back to this after writing the rest of the code this may not be needed.
    # All we really need is a list of characters from largest to smallest. No dictionary.

    characterDict = {}

    for char in chars:
        if char in characterDict:
            characterDict[char] +=1
        else:
            characterDict[char] = 1

    # sorting function to sort by most common
    # uses a lambda function to make sure the count is selected, not the tuple (as they are all a value of 2)
    characterDictSorted = sorted(characterDict.items(), key=lambda item: item[1], reverse=True)
    return characterDictSorted

# print(characterDictSorted)

def createHexMap(characterDictSorted):
    # creation of a dict that maps each character to a hex value
    hexMap = {}
    counter = 0
    # hexList is 15 instead of 16 long as the f character is reserved for the nibbles
    hexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
    for a in characterDictSorted:
        # find out how many times code has ran to detemine amount of F's to inject
        # uses floor division to return a whole number
        amountToAdd = counter // 15
        hexListPos = counter % 15

        finalHexChar = ('f' * amountToAdd) + (hexList[hexListPos])

        # assign char to dict
        hexMap[a[0]] = finalHexChar

        counter+=1

        # hopefully this will work for a infinite number of different characters in different languages
    return hexMap

def compress(stringSICS, hexMap):
    # compress
    newStringSICS = ""
    # Replaces each character with its assigned hex code
    for a in stringSICS:
        newStringSICS += hexMap.get(a)
    return newStringSICS

# runner function to cleanup code
def runSICS(stringCompress):
    characterDictSorted = sortCountChar(stringCompress)
    hexMap = createHexMap(characterDictSorted)
    compressed = compress(stringCompress, hexMap)

    return compressed

finalCompressed = runSICS(stringSICS)
print(finalCompressed)