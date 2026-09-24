import random
import string
def random_num():
    print("Random Number:",random.randint(1,100))
def random_list():
    l =[]
    for i in range(10):
        n =random.randint(1,100)
        l.append(n)
    print("Random List:",l)
def password():
    length = int(input("Enter password length:"))
    pwd = ""
    char = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        pwd += random.choice(char)
    print("Generated Password:",pwd)
def otp():
    Otp = random.randint(100000,999999)
    print("Genrated OTP:",Otp)
