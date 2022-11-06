# 모듈안에 무엇이 있는지 살펴보는 법

import calendar

print(dir(calendar)) # 모듈안에 무엇이 있는지 확인할 수 있다.

print([x for x in dir(calendar) if 'leap' in x])
# 모듈 안에 "leap" 라는 문자열이 포함된 이름은 무엇이 있는지 조회가 가능하다.
 
print(help(calendar))
# 모듈에 대한 설명서를 출력해준다.
print(calendar.isleap(2077))
# 설명서를 읽고 모듈안에 있는 내장함수를 사용해보자.