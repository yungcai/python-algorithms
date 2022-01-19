def generateDocument(chars, doc):
    for char in doc:
        documentFrequency = countCharacterFrequency(char, doc)
        charatersFrequency = countCharacterFrequency(char, chars)
        if documentFrequency > charatersFrequency
            return False

    return True