text1 = "тест."
text2 = "тесть"
text3 = "трест"

d = {1:" ", 2:"а", 3:"б", 4:"в", 5:"г", 6:"д", 7:"е", 8:"ж", 9:"з", 10:"и", 11:"й", 12:"к", 13:"л", 14:"м", 15:"н", 16:"о", 17:"п", 18:"р", 19:"с", 20:"т", 21:"у", 22:"ф", 23:"х", 24:"ц", 25:"ч", 26:"ш", 27:"щ", 28:"ъ", 29:"ы", 30:"ь", 31:"э", 32:"ю", 33:"я", 34:"."}
len_d = 33

shifr_123 = []
key1 = []

text1_list = [i for i in text1]
text2_list = [i for i in text2]
text3_list = [i for i in text3]

for i in range (0, max (len(text1), len(text2), len(text3))):
    sh_symb = 0
    key_s1 = 0
    for k, v in d.items():
        if text1_list[i] in v:
            sh_symb += k
        if text2_list[i] in v:
            key_s1 += k
            sh_symb += k
        if text3_list[i] in v:
            key_s1 += k
            sh_symb += k
    shifr_123.append (sh_symb)
    key1.append (key_s1)

for i in range (0, len(shifr_123)):
    if shifr_123[i] > 34:
        shifr_123[i] -= 33
    if shifr_123[i] > 34:
        shifr_123[i] -= 33        
    shifr_123[i] = d[shifr_123[i]]

for i in range (0, len(key1)):
    if key1[i] > 34:
        key1[i] -= 33
    key1[i] = d[key1[i]]

print (shifr_123)
print (key1)
