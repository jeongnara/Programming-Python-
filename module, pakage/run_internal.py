#math
import math
print(math.ceil(3.5))   #4 ceil: 천정, 올림
print(math.floor(3.5))  #3 floor: 바닥, 내림
print(round(3.5))   #4 round: 반올림
print(round(3.4))   #3 round: 반올림
print(math.pow(2, 10))  #1024.0
print(math.sin(math.pi/2))  #1.0
# print(math.sin(math.pi))  #0.0  @1.22464^-16

#random
import random
print(random.random())  #java random: 0.0<= r < 1.0
print(random.randrange(1, 10))  #1<= < 10 정수
print(random.randint(1, 10))    #1<= <= 10 정수
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1))     #list1 중 하나

print('before: ', list1)
print(random.shuffle(list1))    #list1 섞기
print('after: ', list1)

print(random.sample(list1, 2))  #랜덤으로 n개 뽑기

#datetime
# print('-'*20)
# import  datetime
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
# birthday = datetime.datetime(2004, 11, 29)
# print(birthday)
# print(now - birthday)

#내가 태어난 날로부터 며칠이 지났는지?
# import  datetime
# now = datetime.datetime.now()
# birthday = datetime.datetime(2004, 1, 26)
# print(now - birthday)

#올해 크리스마스까지 며칠이 남았는지?
# import datetime
# now = datetime.datetime.now()
# 크리스마스 = datetime.datetime(2021, 12, 25)
# print(크리스마스 - now)

# 내 생일이 며칠 남았는지?
# import datetime
# now = datetime.datetime.now()
# my_birthday = datetime.datetime(2022, 1, 26)
# print(my_birthday - now)

#로또 복권 자동 생성기를 만든다면?    (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random
print(random.random())  #java random: 0.0<= r < 1.0
print(random.randrange(1, 45))  #1<= < 10 정수
print(random.randint(1, 45))    #1<= <= 10 정수
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
         41, 42, 43, 44, 45]
print(random.choice(list1))     #list1 중 하나

# print('before: ', list1)
# print(random.shuffle(list1))    #list1 섞기
# print('after: ', list1)

# print(random.sample(list1, 6))
#
# fee = 59827
# print(((fee//100))*100,"원")

# 1번.
# import math
# bill = 62451
# bill = 59827
#
# print(bill//100*100)
# print(bill-bill%100)
# print(math.floor(bill/100)*100)
# print(int(bill/100)*100)

# 2번
# score = 93
# print(round(score/10)*10)
# print(round(score, -1))

# 4번
# list_r = random.sample(range(1, 9+1, 1), 3)
# print(list_r)
# # print(str(list_r))
# print("".join(str(n) for n in list_r))
# print("".join(map(str, list_r)))

# 8번
#마지막 번호 묻자
last_number = input("마지막 번호는?")
#1~마지막 번호까지 숫자 리스트 만들자
list_class = list(range(1, int(last_number) + 1))
print(list_class)
#반복
while True:
    #뺄 번호 묻자
    exclude_number = input("뺄 번호는?(enter치면 그만 빼기)")
    #다 뺐으면 반복 끝내기
    if exclude_number == '':
        break
    #빼자
    list_class.remove(int(exclude_number))
    print(list_class)
#섞기
random.shuffle(list_class)
#출력
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')