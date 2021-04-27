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

    print(price[0]) # 정수값으로는 인덱싱이 안됨
    print(prices['BTC']) # key를 통해서만 value에 접근가능

