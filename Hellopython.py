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

#리스트 다중 리스트
list1 = [1,2,3,4,5,[1,2,3,4,5]]
print(list1[5][0])
list2 = [1,2,3,4,5]
print(1 in list2)
print(1 not in list1)



