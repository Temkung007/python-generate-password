import random
import time
import string

random.seed(time.time())

print("2 uppercase letters\n2 lowercase letters\n2 special characters\n2 numbers")

password_list = list()
password_list.append(chr(random.randrange(65, 90)))  # generate uppercase letter
password_list.append(chr(random.randrange(65, 90)))  # generate uppercase letter
password_list.append(chr(random.randrange(97, 122)))  # generate lowercase letter
password_list.append(chr(random.randrange(97, 122)))  # generate lowercase letter
password_list.append(random.choice(string.punctuation))  # generate special character
password_list.append(random.choice(string.punctuation))  # generate special character
password_list.append(str(random.randrange(0, 9)))  # generate number
password_list.append(str(random.randrange(0, 9)))  # generate number

print(password_list)

random.shuffle(password_list)
password = ''.join(password_list)

print("your password from generate is", password)
