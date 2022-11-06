import string
import random

a = string.ascii_uppercase
print(a)

b = string.ascii_lowercase
print(b)

c = string.ascii_letters
print(c)

d = string.digits
print(d)

g = list(c+d)+ ['_']

print(g)




# 비밀번호 만들기
stSample = string.ascii_letters
dgSample = string.digits 
chars = stSample+ dgSample + '!@#$%^&*'

# for i in range(16):
#     pwd = random.choice(chars)
#     password += pwd

pwd_chars_list = []

def make_pwd():
    password = ""
    num = 0
    for i in chars:
        pwd_chars_list.append(i)
    
    while num != 16:
        num+=1
        tem_pwd = random.choice(pwd_chars_list)
        password += tem_pwd
    return password

print(make_pwd())

