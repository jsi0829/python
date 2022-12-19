#문자형 자료형 나타내기 #은 한줄주석임
# ''' '''는 두줄주석
# -uhm-
# print("helloworld")
# print("hi"*7)
# print("hi \nbye")

#숫자형 자료형
# 정수형
# print("1")
# print("-1")
# 실수형
# print("1.1")
# print("-1.1")
# print("1 + -1")

# boolean 자료형
# print(3 > 4) # 거짓
# print(3 < 4) # 참
# print(not(3 > 4))# 거짓의 거짓이므로 참

########### 변수
# name = 'honggil'
# print(name)
# name1, name2 = 'chang','sik'
# print(name1, name2)
# name1 = name2 = 'java n c sharp'
# print(name1, name2)
############ 문자열
# print(1 + 1)  플러스
# print(1 - 2)  마이너스
# print(2**3)  제곱
# print(2*3)  곱
# print(2/4)  나누기
# print(2//4) 몫 구하기

# print(1 > 2) and print(2 < 3)
# print(1 > 2 & 2 < 3)
# print(1 > 2) or print(2 < 3)
# print(1 > 2 | 2 < 3)


#맴버연산 숫자값이 맴버안에 들어있는지 확인하는 연산
# print(1 in (1,2,3,4,5))
# print(6 not in (1,2,3,4,5))

#간단한 함수 위에서 부터 최소 최대 절댓값 반올림
# print(min(7,9))
# print(max(7,9))
# print(abs(-7))
# print(round(3.14))

#랜덤값 구하기
# from random import *
# print(random()) 0.0부터 1.0까지의 랜덤숫자 출력

# #문자열 표현
# sentence = "this is string"
# print(sentence)
# sentence = "this is s"
# print(sentence)

# # 인덱싱
# word = "python"
# print(word[0])
# print(word[-1])
# word = "2021-python"
# print(word[0:2])
# print(word[:4])
# print(word[4:])
# word = "1234567"
# #print(word[이상:미만:간격])
# print(word[::2])
# print(word[1:6:3]) 1부터시작해 5까지 3칸씩 띄워서

# #포멧
# a = "파이썬 님의 무게는 20.5kg입니다."
# name = "파이썬"
# weight = 70.544
# print(name + "님의 무게는" + str(weight) + "kg입니다.")
# print("%s님의 무게는 %0.1f입니다"%(name, weight))
# print("{}님의 무게는 {:0.1f}kg 입니다.".format(name,weight))
# print("{name}님의 무게는 {weight}kg 입니다.".format(name="자바",weight=60.8))

#간단한 함수
# word = 'apple'
# print(word.find('p')) p자리 찿기
# print(word.count('p')) p개수 세기
# print(word.index('p')) 단어를 보다가 제일 먼저 찿는 글자 인덱스 출력
# print(len(word)) 값의 길이를 나타내주는것
# print(word.upper()) 소문자를 대문자로
# print(word[0].upper()) 0번째 인덱스의 글자를 대문자로
# word = '    apple   '
# print(word.lower()) 대문자를 소문자로
# print(word.strip()) 공백 삭제
# word = 'my name is python' 
# print(word.replace('python', 'java')) 파이썬을 자바로
# print(word.split()) 문자열을 단어 단위로 쪼갬 
# ex) ['my', 'name', 'is', 'python']

#리스트와 튜플

#리스트는 안의 값 변경 가능 하지만 튜플은 불가능
# list1 = [1,2,3,4,5]
# print(list1)
# print(list1[0])
# print(list1[0]+list1[1])

#리스트 슬라이싱
# list1 = [1,2,3,4,5]
#print(list1[0:4])
#print(list1[0:4:2])

# 리스트 많이 쓰는 연산자
# len(), +, *, 
# in, not in, 포함, 포함안함 
# [], min, max 최대 최소
# len([list])

#리스트 많이쓰는 함수
# append() 리스트 끝에 값넣기
# insert(index,값) 인덱스 넘버에 값 추가
# pop(index) 인덱스 넘버의 값을 가져온 후 삭제
# remove(값) 리스트에서 값을 찿아 삭제
# clear() 리스트에서 모든 값 삭제
# count() 리스트에 일치하는 값의 수 카운팅
# index()리스트에서 일치하는 값의 인덱스 출력
# reverse() 리스트 뒤에서 부터 출력
# sort() 리스트 오름차순 출력

# #리스트 다중 리스트
# list1 = [1,2,3,4,5,[1,2,3,4,5]]
# print(list1[5][0])
# list2 = [1,2,3,4,5]
# print(1 in list2)
# print(1 not in list1)


