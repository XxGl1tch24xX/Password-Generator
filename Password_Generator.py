import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

passwd_len = input('Please input the password length: ')
passwd_len = int(passwd_len)

print('\n Here is you password:')

password = ''

for x in range(passwd_len):
    password += random.choice(chars)
print(password)