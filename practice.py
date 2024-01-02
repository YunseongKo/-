# 변수 : 애완동물을 소개
animal = "강아지"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이" # 이 문장 밑에서는 hobby=공놀이, 위에서는 낮잠
# +는 str(age)로 써야하지만, ,는 str을 안쓰고 int도 문자열로 처리되어 쭉 적을 수 있다
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
# command + / 하면 일괄 주석 처리가 됨

# 연산자들 : 사칙연산 및 참거짓
print(1+1) # 합
print(3-2) # 차
print(5*2) # 곱
print(6/3) # 실수단위 몫
print(2**3) # 제곱
print(5%3) # 나머지
print(10%3)
print(5//3) # 정수단위 몫
print(10//3)
print(10>3) # True/False
print(3==3)
print(1!=3)
print(not(1!=3))
print((3>0)and(3<5)) # True
print((3>0)or(3>5)) # True
print((3>0)|(3>5)) # True

# 축약된 변수 계산
number=2+3*4
print(number)
number=number+2 # 16 : 변수가 달라짐
print(number)
number += 2 # 위의 문장과 동치
print (number)
number*=2
print(number)
number/=2
print(number)
number-=2
print(number)
number%=2
print(number)