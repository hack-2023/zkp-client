#!/usr/bin/python

import bcrypt
import time
import random
import string


def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(10):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


passwd = get_random_password()
print("Your Random Password is ", get_random_password())

start = time.time()
salt = bcrypt.gensalt(rounds=16)
hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt)
end = time.time()

print("Time taken: ", end - start)

print("Hashed: ", hashed)
print("Hashed hex: ", hashed.hex())