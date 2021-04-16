# Made the imports more readable
import random
import string

# Removed unencessary print statements as any information should be in the projects readme file, not the actual script.

# Changed text to be more concise
def main():
    amount = int(input('Amount of Passwords: '))
    value = 1
    while value <= amount:
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
        f = open('Passwords.txt', "a+")
        # Removed f-string as its un-neccessary in this scenario. (should only be used when attempting to merge two pieces of text in a clean way.)
        f.write(code + '\n')
        f.close()
        # Same thing as above, removing un-neccessary f-string
        print(code)
        value += 1

# Created a main function. Get into a habit of doing this as it will help you create code that is more modular and easier to rad rather than a chunk of code that you have to take in all at once.
if __name__ == '__main__':
    main()
