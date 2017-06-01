#!/usr/bin/python -u
import random,string

    
def decrypt():    
    encryptflag = "BNZQ:1o0yd5jk9h256wdjsu366t10787198h9"
    encflag = ""
    random.seed("random")
    random_numbers = []
    encDict = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789:"
    k = 0
    #Generate all random numbers from the given seed
    for i in range(len(encryptflag)):
        if encryptflag[i].isupper() or encryptflag[i].islower():
            random_numbers.append(random.randrange(0,26))
        elif encryptflag[i].isdigit():
            random_numbers.append(random.randrange(0,10))
        else:
            random_numbers.append(-1)
    print("Random Numbers determined from Seed: ")
    print(random_numbers)
    
    flag = ""
    encListList = []
    for j in range(len(random_numbers)):    #run through all chars in the encrypted flag
        encList = []
        for i in range(len(alphabet)):      #generate encrypted values for every possible entry
            if random_numbers[j] > 0:       #if a digit or alphanumeric
                encryptedChar = encryptOne(alphabet[i],random_numbers[j])
                encList.append(encryptedChar)
                if encryptedChar == encryptflag[k]:     #if encrypted char matches 
                    print("---Match Found---\n" +encryptedChar + " -> "+ alphabet[i])
                    flag+=alphabet[i]       #append matching char to flag
                    k+=1
                    break
            else:
                encryptedChar = encryptflag[k]
                encList.append(encryptflag[k])
                print("---Match Found---\n" +encryptedChar + " -> "+ alphabet[i])
                flag+=encryptedChar
                k+=1
                break
        encListList.append(encList)
    #
    print "Flag = " + flag

def encryptOne(c,rand):
    random.seed("random")
    random_numbers = []
    if c.islower():
        #rotate number around alphabet a random amount
        rand1 = rand
        random_numbers.append(rand1)
        #print("Rand1: " + str(rand1))
        return chr((ord(c)-ord('a')+rand1)%26 + ord('a'))
    elif c.isupper():
        rand2 = rand
        random_numbers.append(rand2)
        #print("Rand2: " + str(rand2))
        return chr((ord(c)-ord('A')+rand2)%26 + ord('A'))
    elif c.isdigit():
        rand3 = rand
        random_numbers.append(rand3)
        #print("Rand3: " + str(rand3))
        return chr((ord(c)-ord('0')+rand3)%10 + ord('0'))
    else:
        random_numbers.append(0)
        encflag += c
        return c

decrypt()


    
