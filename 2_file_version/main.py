import string
file = open("dictionary.txt", "r")
fil = []
for i in file:
    this = ""
    if i.endswith("\n"):
        for e in i[0:-1]:
            this += e
    else:
        fil.append(i)
    if this is not "":
        fil.append(this)
file.close()

choice = input("Encrypt(0) or Decrypt(1): ")
if choice == "0":
    orgText = input('Enter text to encrypt: ')
    orgKey = input('Enter key: ')
elif choice == "1":
    cipherText = input("Input ciphertext: ")
    key = input("Enter key: ")

def encrypt(text, key):
    textAlt = []
    keyAlt = []
    combinedAlt = []
    counter = 0
    counter2 = 0
    cipherText = []
    # get alternates
    for i in text:
        textAlt.append(alternate(i, counter, len(text)))
        counter += 1
    for i in key:
        keyAlt.append(alternate(i, counter2, len(key)))
        counter2 += 1
    # combine alternates
    if len(textAlt) > len(keyAlt):
        for i in range(len(keyAlt)):
            combinedAlt.append(specialAdd(textAlt[i], keyAlt[i]))
        for i in range(len(keyAlt), len(textAlt)):
            combinedAlt.append(textAlt[i])
    elif len(textAlt) < len(keyAlt):
        for i in range(len(textAlt)):
            combinedAlt.append(specialAdd(textAlt[i], keyAlt[i]))
        for i in range(len(textAlt), len(keyAlt)):
            combinedAlt.append(keyAlt[i])
    elif len(textAlt) == len(keyAlt):
        for i in range(len(textAlt)):
            combinedAlt.append(specialAdd(textAlt[i], keyAlt[i]))
    # get ciphertext
    for i in combinedAlt:
        cipherText.append(makeChar(i))
    return ''.join(cipherText)

def decrypt(text, key):
    keyAlt = []
    textAlt = []
    combinedAlt = []
    split = []
    characters = []
    out = ''
    a = len(text)
    for i in range(a - 1):
        if i % 6 == 0 and i != 0:
            split.append(text[i-6:i])
    split.append(text[len(text) - 6: len(text)])
    for i in split:
        for j in fil:
            if j[2:] == i:
                characters.append(j[0])
    characters.append(" ")
    current = ""
    counter = 0
    for i in characters:
        if counter < 2:
            current += i
        elif counter == 2:
            combinedAlt.append(current)
            current = ""
            counter = 0
            current += i
        counter += 1
    counter = 0
    for i in key:
        keyAlt.append(alternate(i, counter, len(key)))
        counter += 1
    if len(combinedAlt) >= len(keyAlt):
        for i in range(len(combinedAlt)):
            try:
                textAlt.append(specialSub(combinedAlt[i], keyAlt[i]))
            except IndexError:
                textAlt.append(combinedAlt[i][0])
    elif len(combinedAlt) < len(keyAlt):
        for i in range(len(combinedAlt)):
            textAlt.append(specialSub(combinedAlt[i], keyAlt[i]))
    for i in textAlt:
        out += unAlternate(i)
    return out



def unAlternate(alt):
    conversion = string.ascii_letters + '0123456789 '
    out = ''
    if alt in conversion:
        out += conversion[len(conversion) - 1 - conversion.index(alt)]
    return out

def alternate(char, index, length):
    conversion = string.ascii_letters + '0123456789 '
    out = ''
    if char in conversion:
        out += conversion[len(conversion) - 1 - conversion.index(char)]
    out += str(length - index)
    return out

def specialAdd(text, key):
    conversion = string.ascii_letters + '0123456789 ' + string.ascii_letters + '0123456789 '
    textIndex = conversion.index(text[0])
    keyIndex = conversion.index(key[0])
    numNum = int(text[1:]) + int(key[1:])
    extra = ''
    if numNum >= len(conversion):
        extra += '/'
    else:
        extra += conversion[numNum]
    out = conversion[textIndex + keyIndex] + extra
    return out

def specialSub(alt, keyAlt):
    out = ''
    conversion = string.ascii_letters + '0123456789 ' + string.ascii_letters + '0123456789 '
    keyIndex = conversion.index(keyAlt[0])
    altIndex = conversion.index(alt[0])
    if keyIndex > altIndex:
        altIndex = conversion.rindex(alt[0])
    out += conversion[altIndex - keyIndex]

    return out

def makeChar(alt):
    decision = ''
    counter = 0
    for i in alt:
        if counter < 2:
            for j in fil:
                if j[0] == i:
                    decision += j[2:]
        counter += 1
    return decision
# to make this script standalone. remove to import.
if __name__ == '__main__':
    if choice == "0":
        print(encrypt(orgText, orgKey))
    elif choice == "1":
        print(decrypt(cipherText, key))
    # for this to work in exe
    x = input("Press enter to exit")