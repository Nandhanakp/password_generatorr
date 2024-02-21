import random
import string

def generate_password(length,uppercase,lowercase,numbers,symbols):
    characters=''
    if uppercase:
        characters+=string.ascii_uppercase
    if lowercase:
        characters+=string.ascii_lowercase
    if numbers:
        characters+=string.digits
    if symbols:
        characters+=string.punctuation

    if not characters:
        print("error, no characters found")

    password=''.join(random.choice(characters)for ln in range(length))
    return password


length=int(input("Enter the password length: "))
uppercase=input("Include Uppercase yes/no : ").lower()=='yes'
lowercase=input("Include Lowercase yes/no : ").lower()=='yes'
numbers=input("Include numbers yes/no : ").lower()=='yes'
symbols=input("Include symbols yes/no : ").lower()=='yes'

password=generate_password(length,uppercase,lowercase,numbers,symbols)

print(password)
