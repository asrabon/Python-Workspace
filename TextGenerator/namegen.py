import random
import string
import pandas

alphabet = string.ascii_lowercase
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def generator(userChoice):
    if(userChoice == 'a'):
        return random.choice(alphabet)
    elif(userChoice == 'c'):
        return random.choice(consonants)
    elif(userChoice == 'v'):
        return random.choice(vowels)
    else:
        return userChoice

def main():
        userChoice1 = input("Enter a for any letter, c for a consonant, or v for a vowel: ")
        userChoice2 = input("Enter a for any letter, c for a consonant, or v for a vowel: ")
        userChoice3 = input("Enter a for any letter, c for a consonant, or v for a vowel: ")
        for i in range(10):
            name = ""
            name += generator(userChoice1)
            name += generator(userChoice2)
            name += generator(userChoice3)
            print(name)

if __name__== "__main__":
  main()
