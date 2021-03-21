import string
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
        if i == '000000':
            characters.append('/')
        elif i == '000001':
            characters.append(' ')
        elif i == '000010':
            characters.append('9')
        elif i == '000011':
            characters.append('8')
        elif i == '000100':
            characters.append('7')
        elif i == '000101':
            characters.append('6')
        elif i == '000110':
            characters.append('5')
        elif i == '000111':
            characters.append('4')
        elif i == '001000':
            characters.append('3')
        elif i == '001001':
            characters.append('2')
        elif i == '001010':
            characters.append('1')
        elif i == '001011':
            characters.append('0')
        elif i == '001100':
            characters.append('Z')
        elif i == '001101':
            characters.append('Y')
        elif i == '001110':
            characters.append('X')
        elif i == '001111':
            characters.append('W')
        elif i == '010000':
            characters.append('V')
        elif i == '010001':
            characters.append('U')
        elif i == '010010':
            characters.append('T')
        elif i == '010011':
            characters.append('S')
        elif i == '010100':
            characters.append('R')
        elif i == '010101':
            characters.append('Q')
        elif i == '010110':
            characters.append('P')
        elif i == '010111':
            characters.append('O')
        elif i == '011000':
            characters.append('N')
        elif i == '011001':
            characters.append('M')
        elif i == '011010':
            characters.append('L')
        elif i == '011011':
            characters.append('K')
        elif i == '011100':
            characters.append('J')
        elif i == '011101':
            characters.append('I')
        elif i == '011110':
            characters.append('H')
        elif i == '011111':
            characters.append('G')
        elif i == '100000':
            characters.append('F')
        elif i == '100001':
            characters.append('E')
        elif i == '100010':
            characters.append('D')
        elif i == '100011':
            characters.append('C')
        elif i == '100100':
            characters.append('B')
        elif i == '100101':
            characters.append('A')
        elif i == '100110':
            characters.append('z')
        elif i == '100111':
            characters.append('y')
        elif i == '101000':
            characters.append('x')
        elif i == '101001':
            characters.append('w')
        elif i == '101010':
            characters.append('v')
        elif i == '101011':
            characters.append('u')
        elif i == '101100':
            characters.append('t')
        elif i == '101101':
            characters.append('s')
        elif i == '101110':
            characters.append('r')
        elif i == '101111':
            characters.append('q')
        elif i == '110000':
            characters.append('p')
        elif i == '110001':
            characters.append('o')
        elif i == '110010':
            characters.append('n')
        elif i == '110011':
            characters.append('m')
        elif i == '110100':
            characters.append('l')
        elif i == '110101':
            characters.append('k')
        elif i == '110110':
            characters.append('j')
        elif i == '110111':
            characters.append('i')
        elif i == '111000':
            characters.append('h')
        elif i == '111001':
            characters.append('g')
        elif i == '111010':
            characters.append('f')
        elif i == '111011':
            characters.append('e')
        elif i == '111100':
            characters.append('d')
        elif i == '111101':
            characters.append('c')
        elif i == '111110':
            characters.append('b')
        elif i == '111111':
            characters.append('a')
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
            try:
                current += i
            except TypeError:
                pass
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
    keyIndex2 = None
    altIndex2 = None
    out = ''
    conversion = string.ascii_letters + '0123456789 ' + string.ascii_letters + '0123456789 '
    keyIndex = conversion.index(keyAlt[0])
    altIndex = conversion.index(alt[0])
    if keyIndex > altIndex:
        altIndex = conversion.rindex(alt[0])



    out += conversion[altIndex - keyIndex]

    return out

def makeChar(alt):
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 <-- characters (remember space at end)
    decision = ''
    counter = 0
    for i in alt:
        if counter < 2:
            if i is '/':
                decision += '000000'
            elif i is ' ':
                decision += '000001'
            elif i is '9':
                decision += '000010'
            elif i is '8':
                decision += '000011'
            elif i is '7':
                decision += '000100'
            elif i is '6':
                decision += '000101'
            elif i is '5':
                decision += '000110'
            elif i is '4':
                decision += '000111'
            elif i is '3':
                decision += '001000'
            elif i is '2':
                decision += '001001'
            elif i is '1':
                decision += '001010'
            elif i is '0':
                decision += '001011'
            elif i is 'Z':
                decision += '001100'
            elif i is 'Y':
                decision += '001101'
            elif i is 'X':
                decision += '001110'
            elif i is 'W':
                decision += '001111'
            elif i is 'V':
                decision += '010000'
            elif i is 'U':
                decision += '010001'
            elif i is 'T':
                decision += '010010'
            elif i is 'S':
                decision += '010011'
            elif i is 'R':
                decision += '010100'
            elif i is 'Q':
                decision += '010101'
            elif i is 'P':
                decision += '010110'
            elif i is 'O':
                decision += '010111'
            elif i is 'N':
                decision += '011000'
            elif i is 'M':
                decision += '011001'
            elif i is 'L':
                decision += '011010'
            elif i is 'K':
                decision += '011011'
            elif i is 'J':
                decision += '011100'
            elif i is 'I':
                decision += '011101'
            elif i is 'H':
                decision += '011110'
            elif i is 'G':
                decision += '011111'
            elif i is 'F':
                decision += '100000'
            elif i is 'E':
                decision += '100001'
            elif i is 'D':
                decision += '100010'
            elif i is 'C':
                decision += '100011'
            elif i is 'B':
                decision += '100100'
            elif i is 'A':
                decision += '100101'
            elif i is 'z':
                decision += '100110'
            elif i is 'y':
                decision += '100111'
            elif i is 'x':
                decision += '101000'
            elif i is 'w':
                decision += '101001'
            elif i is 'v':
                decision += '101010'
            elif i is 'u':
                decision += '101011'
            elif i is 't':
                decision += '101100'
            elif i is 's':
                decision += '101101'
            elif i is 'r':
                decision += '101110'
            elif i is 'q':
                decision += '101111'
            elif i is 'p':
                decision += '110000'
            elif i is 'o':
                decision += '110001'
            elif i is 'n':
                decision += '110010'
            elif i is 'm':
                decision += '110011'
            elif i is 'l':
                decision += '110100'
            elif i is 'k':
                decision += '110101'
            elif i is 'j':
                decision += '110110'
            elif i is 'i':
                decision += '110111'
            elif i is 'h':
                decision += '111000'
            elif i is 'g':
                decision += '111001'
            elif i is 'f':
                decision += '111010'
            elif i is 'e':
                decision += '111011'
            elif i is 'd':
                decision += '111100'
            elif i is 'c':
                decision += '111101'
            elif i is 'b':
                decision += '111110'
            elif i is 'a':
                decision += '111111'
        counter += 1
    return decision


if choice == "0":
    print(encrypt(orgText, orgKey))
elif choice == "1":
    print(decrypt(cipherText, key))