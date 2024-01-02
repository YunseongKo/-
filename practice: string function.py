python="Python is amazing"
print(python.lower) # 소문자 출력
print(python.upper) # 대문자 출력
print(python[0].isupper) # 문자열의 [n]번째 글자가 대문자인지 체크해주는 함수
print(len(python)) # 문자열의 길이 확인해주는 함수
print(python.replace("Python", "Java")) # 문자열 내의 특정 글자를 바꿔주는 함수

index=python.index("n") # 'n'이라는 글자가 몇번째 위치에 있는지 확인해주는 함수, 여러개면 제일 앞꺼
print(index)
index=python.index("n", index+1) # 앞에서 찾은 위치 그 이후부터 찾을 수 있음, 여기선 6번부터 두번째 n을 찾게 됨
print(index)

print(python.find("n"))
print(python.find("Java")) # find : 원하는 값이 변수에 포함되어 있지 않으면 -1을 출력
print(python.index("Java")) # index : 원하는 값이 변수에 포함되어 있지 않으면 오류로 출력됨
print(python.count("n")) # count : 원하는 값이 몇번 포함되어 있는지 확인

# 이어 쓰는 방법들
print("a"+"b")
print("a","b")