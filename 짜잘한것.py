
name = {"Bob", "Jason", "Anna"}
name2 = {"Bob", "Cris", "Sam"}
# 교집합
print(name & name2)

# 합집합
print(name | name2)

list_of_sets = [name, name2]

a = set.union(*list_of_sets)
print(a)

b = set.intersection(*list_of_sets)
print(b)

# 달력을 출력하는 방법
import calendar
calendar.prmonth(2022,11)

"""
두 직각변()의 길이를 입력으로 받아 빗변()의 길이를 구하는 함수 hypotenuse()를 작성하세요. 출력은 소수점 셋째 자리에서 반올림합니다.

>>> hypotenuse(3, 4)
5.0
>>> hypotenuse(10, 20)
22.36
"""
import math

def hypotenuse(num1, num2):
    result = math.sqrt((num1**2) + (num2**2))   
    return round(result, 2)
print(hypotenuse(10,20))


print(ord("█"))
print(chr(9608))

# # 웹부라우저 여는법
# import webbrowser
# url = "http://www.python.org/"
# webbrowser.open(url)

import random

a = random.randrange(1,7)
print(a)

Sample_list = [1,2,3,4,5,6,7,8,9]

b = random.choice(Sample_list)
print(b)
