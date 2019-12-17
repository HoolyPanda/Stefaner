import dictionary
from random import randint as rand

class Cryptor:
    def __init__(self):
        
        pass

    def getDictionary(self):
        # self.dictionary = []
        self.dictionary = 4*dictionary.dictionary
        pass

    def _getLetterNumber(self, letter: str):
        return self.dictionary.index(letter)

    def Encrypt(self, text1:str, text2:str, text3:str):
        texts= [text1, text2, text3]
        encryptedText = ""
        text1: str
        text2: str
        text3: str
        iterator = 0
        decryptKey1 = ""
        decryptKey2 = ""
        decryptKey3 = ""
        cup = 0
        noize = 0
        text1 = text1.lower()
        text2 = text2.lower()
        text3 = text3.lower()

        if len(text1) > len(text2):
            if len(text3) >= len(text1):
                cup = len(text3)
            else:
                cup = len(text1)
        else:
            cup = len(text2)

        for letter in range(cup):
            m = len(text1)
            if letter >= len(text1):
                text1Letter = self._getLetterNumber(letter = ' ')
            else:
                n = self._getLetterNumber(text1[letter])
                text1Letter = self._getLetterNumber(letter= text1[letter])

            if letter >= len(text2):
                text2Letter = self._getLetterNumber(letter = ' ')
            else:
                text2Letter = self._getLetterNumber(letter= text2[letter])

            if letter >= len(text3):
                text3Letter = self._getLetterNumber(letter = ' ')
            else:
                text3Letter = self._getLetterNumber(letter= text3[letter])

            a = len(self.dictionary) / 2 - 1

            noizeCupLetter = 0
            if text1Letter > text2Letter:
                if text3Letter > text1Letter:
                    noizeCupLetter = text3Letter
                else:
                    noizeCupLetter = text1Letter
            else:
                noizeCupLetter = text2Letter
            # noizeCupLetter -= 2
            # noize = rand(1, (len(self.dictionary) / 3) - noizeCupLetter )
            # noize = 24
            encryptedLetter = (text1Letter + text2Letter + text3Letter + noize) # index 1 + index 2 + noize rand(1,len(self.dictionary))
            
            if text1Letter != None:
                if (text2Letter + text3Letter + noize) >= len(self.dictionary):
                        decryptKey1 += self.dictionary[(text2Letter + text3Letter + noize - (len(self.dictionary) + 1))]
                else:
                    decryptKey1 += self.dictionary[(text2Letter + text3Letter + noize)]

            if text2Letter != None:
                a = self.dictionary[text3Letter]
                if (text1Letter + text3Letter + noize) >= len(self.dictionary):
                        decryptKey2 += self.dictionary[(text1Letter + text3Letter + noize - (len(self.dictionary) + 1))]
                else:
                    decryptKey2 += self.dictionary[(text1Letter + text3Letter + noize)]
            
            if text3Letter != None:
                if (text1Letter + text2Letter + noize) >= len(self.dictionary):
                        decryptKey3 += self.dictionary[(text1Letter + text2Letter +noize - (len(self.dictionary) + 1))]
                else:
                    decryptKey3 += self.dictionary[(text1Letter + text2Letter + noize)]

            if encryptedLetter >= len(self.dictionary):
                encryptedLetter -= (len(self.dictionary) + 1)
            encryptedText += self.dictionary[encryptedLetter]
            
        self.keys = []
        self.et = encryptedText
        self.k = decryptKey1
        self.k2 = decryptKey2
        self.k3 = decryptKey3

        self.keys = [decryptKey1, decryptKey2, decryptKey3]
        print(noize)
        print(chr(noize))
        print("text: |", encryptedText, "|")
        print("key1: |", decryptKey1, "|")
        print("key2: |", decryptKey2, "|")
        print("key3: |", decryptKey3, "|\n")
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


