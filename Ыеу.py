text1 = "����."
text2 = "�����"
text3 = "�����"

d = {1:" ", 2:"�", 3:"�", 4:"�", 5:"�", 6:"�", 7:"�", 8:"�", 9:"�", 10:"�", 11:"�", 12:"�", 13:"�", 14:"�", 15:"�", 16:"�", 17:"�", 18:"�", 19:"�", 20:"�", 21:"�", 22:"�", 23:"�", 24:"�", 25:"�", 26:"�", 27:"�", 28:"�", 29:"�", 30:"�", 31:"�", 32:"�", 33:"�", 34:"."}
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
