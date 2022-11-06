# 다음은 놀이 기구의 목록입니다. 사용자가 키(신장)를 입력하면, 탈 수 있는 놀이 기구 목록을 출력하는 프로그램을 작성하세요.
import ridename

rides = [
"와일드 윙: 110cm 이상",
"드림보트: 120cm 이상",
"자이안트 루프: 120cm 이상",
"툼 오브 호러: -",
"플라이벤처: 140cm~195cm",
"회전목마: 100cm 이상",
"매직 붕붕카: 110cm~140cm"
]



def allowrides(height):
    assert type(height) == int, "int 가 아닌 값이 들어가 있습니다."
    result = []

    for i in rides:
        get_rides = ridename.read(i)
        result.append(get_rides)
        
    for j in range(len(result)):
        if result[j][1] == None or result[j][1] <= height :
            if result[j][2] == None or height > result[j][2]:
                print(result[j][0])

if __name__ == "__main__":
    allowrides(200)


# -------------------------------------------------------
# 정답으로 올라 온 것

import sys

sys.path.append("../ch03")
import ridename


rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''


def allowedrides(height):
    assert type(height) == int

    result = [] 
    for ride in rides.splitlines():
        ridename, cmmin, cmmax = ridename.read(ride)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
    
    return result


if __name__ == "__main__":
    height = int(input())
    for x in allowedrides(height):
        print(x)