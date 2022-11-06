# 놀이 기구 중에서 둘리, 도우너, 마이콜이 모두 탈 수 있는 것을 출력합니다.
# Ex) 120 110 179
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

set_list = []

def allowrides(height):
    assert type(height) == int, "int 가 아닌 값이 들어가 있습니다."
    result = []
    set_result = set()
    for i in rides:
        get_rides = ridename.read(i)
        result.append(get_rides)
        
    for j in range(len(result)):
        if result[j][1] == None or result[j][1] <= height :
            if result[j][2] == None or height > result[j][2]:
                set_result.add(result[j][0])

    return set_result

height_list = [120,110,179]
if __name__ == "__main__":
    for i in height_list :
        a = allowrides(i)
        set_list.append(a)
    
    print(set_list[0] & set_list[1] & set_list[2])



# -----------------------------------------------------------
# 정답으로 올라 온 것

import park

setlist = []

for height in input().split():
    setlist.append(set(park.allowedrides(int(height))))

for ride in set.intersection(*setlist):
    print(ride)