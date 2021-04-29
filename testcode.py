# 리스트 []
hold=["a","b","c"]
print(hold[0:2])

# append: port 뒤에 삽입
portfolio=[]
portfolio.append("BTC")
portfolio.append("ETH")
portfolio.append("XRP")

# insert : port 중간에 삽입
portfolio.insert(1,"DASH")

# del : 중간 부분 삭제
del portfolio[1]


# tuple () : 수정x, 메모리 적게 차지
portfolio2=("aa","bb","cc")
del portfolio2[0] # 에러남


# dictionary {} : 두 값의 관계를 저장하는데 용이
prices={'BTC':83000, 'XRP':514}
prices2={}
prices2['BTC']=830000
prices2['XRP']=5122
print(prices2)

print(prices[0]) # 정수값으로는 인덱싱이 안됨
print(prices['BTC']) # key를 통해서만 value에 접근가능


# if문
bitcoin=840000
if bitcoin> 1:  # 비교연산자로는 == 사용, 논리연산자로는 and, or, not 사용
    print("bitcoin long")
elif bitcoin<0:
    print("bitcoin short")
else:
    print("bitcoin stay")

# for문
ripple=range(1,10) # 1~9까지 나옴
for num in ripple:
    print(num)
for value in portfolio:
    print(value)
for ticker in prices: # key가 나옴
    print(ticker)
for ticker, price in prices.items(): # 1. key, item을 같이 출력할때 사용
    print(ticker, price)
for ticker in prices:                # 2. key, item을 같이 출력
    print(ticker, prices[ticker])

# while문
num=1
while True: # 조건문이 True일때까지 계속 돌아감
    if num==10:
        break # 조건만족시 while문 빠져나감
    print(num)
    num=num+1

# function
def hap(a,b):
    ret=a+b
    return ret

hap(1,2)

# module : 파이썬 파일을 의미함
import grammer  # r에서 source와 동일함
grammer.get_open_price("BTC")
grammer.get_close_price("BTC")

import datetime
now=datetime.datetime.now()
print(now)

import requests
resp=requests.get("https://api.bithumb.com/public/ticker/BTC")
print(resp)
print(resp.content)

# 클래스 : 데이터 + 함수를 묶어놓은것
a=3
print(type(a))
print(a.bit_length())