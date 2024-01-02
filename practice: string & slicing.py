# String
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# Slicing : 필요한 정보만을 잘라 와서 사용하는 것 
jumin = "010205-3456789"
print("성별 : " + jumin[7])
print("연 : "+ jumin[0:2]) # 0번째부터 2-1번째 까지의 영역을 가져옴, [0:2:1]과 같은 의미
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # [a:b:c] 각 자리에서 하나를 비우면 a는 0부터, b는 끝까지, c는 한칸씩을 생각
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨뒤에서 끝까지