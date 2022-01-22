def generateDocument(chars, doc):
    for char in doc:
        documentFrequency = countCharacterFrequency(char, doc)
        charatersFrequency = countCharacterFrequency(char, chars)
        if documentFrequency > charatersFrequency
            return False

    return True

    def countCharacterFrequency(character, target):
        freq = 0
        for char in target:
             if char == character:
                 freq += 1

        return freq 
         