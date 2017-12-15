#---------- Main -----------------------


cle = "musique"
flag = 0
temp =""
texte = "j'adore ecouter la radio toute la journee"
code = ""

for car in texte:
    if flag == len(cle):
        flag = 0

    if ord(car) not in range(97, 123):
        temp = temp + car

    else:
        temp = temp + cle[flag]
    flag += 1

print (len(temp))
print (len(texte))

for pos, car in enumerate(texte):
    if ord(car) not in range(97, 122):
        code = code + car

    else:
        code = code + chr((((ord(car)-97) + (ord(temp[pos])-97))% 26) + 97)


print(temp)
print(code)
print(texte)

