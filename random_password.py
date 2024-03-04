# import the necessary modules
import random
import string

all_characters=string.ascii_letters+string.digits+string.punctuation


print("hello, Welcome to password generator!\n")
# input legnth of password 
legnth=int(input("legnth of password:"))   

# create the password 
Password="".join(random.choices(all_characters,k=legnth))

# print the password
print("Auto generated Random Password is:",Password)
