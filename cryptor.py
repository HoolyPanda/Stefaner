import dictionary as dictionary
from random import randint as rand


class Cryptor:
    def __init__(self):
        
        pass

    def getDictionary(self):
        self.dictionary = []
        self.dictionary = dictionary.dictionary
        self.dictionary += dictionary.dictionary
        pass

    def _getLetterNumber(self, letter: str):
        return self.dictionary.index(letter)

    def Encrypt(self, text1:str, text2:str):
        texts= [text1.lower(), text2.lower()]
        encryptedText = ""
        text1: str
        text2: str
        iterator = 0
        decryptKey1 = ""
        decryptKey2 = ""
        cup = 0

        if len(text1) >= len(text2):
            cup = len(text1)
        else:
            cup = len(text2)

        for letter in range(cup):

            if letter >= len(text1):
                text1Letter = 0
            else:
                text1Letter = self._getLetterNumber(letter= text1[letter].lower())

            if letter >= len(text2):
                text2Letter = 0
            else:
                text2Letter = self._getLetterNumber(letter= text2[letter].lower())

            a = len(self.dictionary) / 2 -1

            noizeCupLetter = 0
            if text1Letter > text2Letter:
                noizeCupLetter = text1Letter
            else:
                noizeCupLetter = text2Letter

            noize = rand(1, (len(self.dictionary) / 2) - noizeCupLetter)  #TODO bug if noize > 2
            encryptedLetter = (text1Letter + text2Letter + noize) # index 1 + index 2 + noize rand(1,len(self.dictionary))
            
            if text1Letter != None:
                if (text2Letter + noize) >= len(self.dictionary):
                        decryptKey1 += self.dictionary[(text2Letter + noize - (len(self.dictionary) + 1))]
                else:
                    decryptKey1 += self.dictionary[(text2Letter + noize)]

            if text2Letter != 0:
                if (text1Letter + noize) >= len(self.dictionary):
                        decryptKey2 += self.dictionary[(text1Letter + noize - len(self.dictionary) + 1)]
                else:
                    decryptKey2 += self.dictionary[(text1Letter + noize)]
            
            if encryptedLetter >= len(self.dictionary):
                encryptedLetter -= (len(self.dictionary) + 1)
            encryptedText += self.dictionary[encryptedLetter]
            

        self.et = encryptedText
        self.k = decryptKey1
        self.k2 = decryptKey2

        print("text: |", encryptedText, "|")
        print("key1: |", decryptKey1, "|")
        print("key2: |", decryptKey2, "|\n")
        pass
        

    def Decrypt(self, encryptedText: str, key: str):
        decryptedText = ""
        for letter in range(len(key)):
            encryptedTextLetter = self._getLetterNumber(encryptedText[letter])
            keyLetter = self._getLetterNumber(key[letter])
            if encryptedTextLetter - keyLetter >= 0:
                decryptedText += self.dictionary[encryptedTextLetter - keyLetter]

            else:
                a = len(self.dictionary)
                decryptedText += self.dictionary[(len(self.dictionary) - keyLetter) + encryptedTextLetter]

        print("text: ", decryptedText)
        pass


