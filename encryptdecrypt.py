#!/usr/bin/env python
import hashlib
import binascii
import random


def appendKeyMapList():
    KeyMapList = []

    mCaesar1 = {
        'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D',
        'F': 'E', 'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I',
        'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'O': 'N',
        'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S',
        'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X',
        'Z': 'Y'
    }

    mCaesar2 = {
        'A': 'Y', 'B': 'Z', 'C': 'A', 'D': 'B', 'E': 'C',
        'F': 'D', 'G': 'E', 'H': 'F', 'I': 'G', 'J': 'H',
        'K': 'I', 'L': 'J', 'M': 'K', 'N': 'L', 'O': 'M',
        'P': 'N', 'Q': 'O', 'R': 'P', 'S': 'Q', 'T': 'R',
        'U': 'S', 'V': 'T', 'W': 'U', 'X': 'V', 'Y': 'W',
        'Z': 'X'
    }

    mCaesar3 = {
        'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B',
        'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G',
        'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L',
        'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q',
        'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V',
        'Z': 'W'
    }

    pCaesar3 = {
        'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H',
        'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M',
        'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R',
        'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W',
        'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B',
        'Z': 'C'
    }

    emoticon = {
        'A': ':)', 'B': ':(', 'C': ':D', 'D': ';)', 'E': ';(',
        'F': ':(', 'G': '>:)', 'H': '>:(', 'I': '>:D', 'J': '>:P',
        'K': ':|', 'L': '>:|', 'M': '>:o', 'N': ';o', 'O': ':o',
        'P': '<3', 'Q': ';|', 'R': ':3', 'S': '8)', 'T': '8(',
        'U': '>8(', 'V': '>8)', 'W': '>8|', 'X': '8==D', 'Y': '8D',
        'Z': '?!'
    }

    KeyMapList.append(mCaesar1)
    KeyMapList.append(mCaesar2)
    KeyMapList.append(mCaesar3)
    KeyMapList.append(pCaesar3)
    KeyMapList.append(emoticon)

    return KeyMapList


def appendReverseKeyMapList():
    ReverseKeyMapList = []

    mReverseCaesar1 = {

        'Z': 'A', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E',
        'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J',
        'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O',
        'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T',
        'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
        'Y': 'Z'

    }

    mReverseCaesar2 = {

        'Y': 'A', 'Z': 'B', 'A': 'C', 'B': 'D', 'C': 'E',
        'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J',
        'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O',
        'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T',
        'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y',
        'X': 'Z'

    }

    mReverseCaesar3 = {

        'X': 'A', 'Y': 'B', 'Z': 'C', 'A': 'D', 'B': 'E',
        'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J',
        'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O',
        'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T',
        'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y',
        'W': 'Z'
    }

    pReverseCaesar3 = {

        'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E',
        'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J',
        'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O',
        'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T',
        'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y',
        'C': 'Z'

    }

    ReverseEmoticon = {

        ':)': 'A', ':(': 'B', ':D': 'C', ';)': 'D', ';(': 'E',
        ';D': 'F', '>:)': 'G', '>:(': 'H', '>:D': 'I', '>:P': 'J',
        ':|': 'K', '>:|': 'L', '>:o': 'M', ';o': 'N', ':o': 'O',
        '<3': 'P', ';|': 'Q', ':3': 'R', '8)': 'S', '8(': 'T',
        '>8(': 'U', '>8)': 'V', '>8|': 'W', '8==D': 'X', '8D': 'Y',
        '?!': 'Z'

    }

    ReverseKeyMapList.append(mReverseCaesar1)
    ReverseKeyMapList.append(mReverseCaesar2)
    ReverseKeyMapList.append(mReverseCaesar3)
    ReverseKeyMapList.append(pReverseCaesar3)
    ReverseKeyMapList.append(ReverseEmoticon)

    return ReverseKeyMapList


# PAUL = <3 :) >8( >:|

def encryptText(KeyMapList, choice, plainText):
    i = 0
    encryptedText = ''
    if choice > -1 and choice < 5:

        while i < len(plainText):
            if plainText[i] in KeyMapList[choice]:  # if key exists with dictionary
                encryptedText += KeyMapList[choice].get(plainText[i])
                i += 1

            else:
                encryptedText += plainText[i]
                i += 1

        return encryptedText

    elif choice == 5:
        return False

def decryptText(ReverseKeyMapList, choice, encryptedText):

    i = 0
    miniText = ""
    plainText = ""

    # ABC = :):(:D

    if choice == 4: #meaning emoticon

        while i < len(encryptedText):

            miniText += encryptedText[i]

            if len(miniText) <= len(encryptedText):

                if miniText in ReverseKeyMapList[choice].keys():

                    if len(plainText) == 0:
                        plainText = ReverseKeyMapList[choice].get(miniText)
                        miniText = ""

                    elif len(plainText) > 0:
                        plainText += ReverseKeyMapList[choice].get(miniText)
                        miniText = ""

            i += 1

        if len(miniText) == 0:
            return plainText

    elif choice < 4:
        decryptSentinel = True
        while i < len(encryptedText):

            if encryptedText[i] in ReverseKeyMapList[choice]:
                plainText += ReverseKeyMapList[choice].get(encryptedText[i])
                i+=1
            else:
                i = len(encryptedText)
                decryptSentinel = False

        if decryptSentinel:
            return plainText

    elif choice == 5:
        return False

def encryptTextRandom(plainText):


    encryptedText = ""
    miniText = ""
    i = 0


    isascii = lambda plainText: len(plainText) == len(plainText.encode())

    if isascii:

        minuscode = 4
        pluscode = 2

        alternate = 0

        while i < len(plainText):
            if alternate % 2 == 0:
                hex = format(ord(plainText[i]) - minuscode, "x") #-4,-3,2
                minuscode -= 1

            elif alternate % 2 == 1:
                hex = format(ord(plainText[i]) + pluscode, "x") #+2,+3,+4
                pluscode += 1


            byte = binascii.unhexlify(hex)
            AsciiChar = byte.decode("utf-8")
            miniText += AsciiChar


            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890" #add random char in between
            N = len(alphabet)
            miniText += alphabet[random.randrange(N)]
            i += 1
            alternate +=1

            #reset code
            if minuscode == 2:
                minuscode = 4

            if pluscode == 4:
                pluscode = 2


        encryptedText += miniText

        return encryptedText

    else:
        print("Not an ascii value!")


def decryptTextRandom(encryptedText):


    plainText = ""
    miniText = ""
    i = 0




    isascii = lambda encryptedText: len(encryptedText) == len(encryptedText.encode())

    if isascii:

        minuscode = 2
        pluscode = 4

        alternate = 0

        while i < len(encryptedText):

            if alternate % 2 == 0: #meaning even
                hex = format(ord(encryptedText[i]) + pluscode, "x") #+4,+3,+2
                pluscode -= 1

            elif alternate % 2 == 1: #meaning odd
                hex = format(ord(encryptedText[i]) - minuscode, "x") #-2,-3,-4
                minuscode += 1

            byte = binascii.unhexlify(hex)
            AsciiChar = byte.decode("utf-8")
            miniText += AsciiChar
            i += 2
            alternate +=1

            # reset code
            if minuscode == 4:
                minuscode = 2

            if pluscode == 2:
                pluscode = 4


        plainText += miniText
        return plainText

    else:
        print("Not an ascii value!")


def sha512Hash(encryptedText):

    return hashlib.sha512(encryptedText.encode('utf-8')).hexdigest()


def md5Hash(encryptedText):

    return hashlib.md5(encryptedText.encode('utf-8')).hexdigest()
