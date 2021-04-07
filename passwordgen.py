import random, string
print('this is a password generator')
print('ik its bad its meant for stronger passwords')
print('i am not responsible for any illegal activity you do with this program')
print(' as it is for educational purposes only')
amount = int(input('how many passwords do u wanna generate: '))
value = 1
while value <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
    f = open('Passwords.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{code}')
    value += 1