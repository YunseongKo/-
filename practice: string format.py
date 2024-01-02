# # print("a"+"b")
# # print("a", "b")

# # 방법 1
# print("나는 %d살입니다." % 20) # D : 정수
# print("나는 %s을 좋아해요" % "파이썬") # string : 문자열
# print("Apple 은 %c로 시작해요" %"A") # Character : 한 글자만 받겠다
# # %s : 그냥 모두 %s로 써도 출력이 된다. 단, ""는 해놔야함(문자열이므로)
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

# # 방법 2 : Format 이용, 2개 이상의 값을 넣고 싶
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간")) # 인덱스에 맞는 변수 가져옴

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

# 방법 4 (v3.6 이상~)
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
# 사실상 방법 3의 변수 지정을 미리 해놓는 것