import cryptor as Cryptor

# DEMO
a = Cryptor.Cryptor()
a.getDictionary()
a.Encrypt(text1= "Слово слово волос олово", text2= "Волосов")
a.Decrypt(encryptedText= a.et, key= a.k)
a.Decrypt(encryptedText= a.et, key= a.k2)