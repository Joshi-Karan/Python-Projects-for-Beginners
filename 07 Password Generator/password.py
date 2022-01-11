import string
import random

def password_generator():
    # Getting all our characters ready
    char = string.printable.replace(' \t\n\r\v\f', '')      # To replace whitespace character
    
    password = ''   # Will add our random choice in it
    pass_length = int(input('Enter the length of password required: '))
    for _ in range(pass_length):
        password += random.choice(char)
    print(password)

if __name__ == "__main__":
    password_generator()