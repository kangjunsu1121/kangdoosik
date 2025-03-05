def open_acount() :
    print('계좌가 생성되었습니다.')

def deposit(balance,money) : # 입금
    print(f'입금이 완료 되었습니다. 잔액은 {balance+money}원 입니다.')
    return balance + money

def withdraw(balance,money) : # 출금
    if balance >= money :
        print(f'출금이 완료되었습니다. 남은 잔액은 {balance-money}원 입니다.')
        return balance - money
    else :
        print(f'출금이 불가능 합니다. 남은 잔액은 {balance}원 입니다.')
        return balance
    
def withdraw_night(balance,money) : # 저녁에 출금
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance,1000)
balance = withdraw(balance,2000) 
commission,balance = withdraw_night(balance,500)
print(f'수수료는 {commission}원이고 잔액은 {balance}원 입니다')

# 기본값

def profile(name,age,main_lang) :
   print(f'이름 : {name}\t나이 : {age}\t사용하는 언어 : {main_lang}')

profile('박준성',21,'파이썬')
profile('홍성주',25,'자바')

def profile(name,age=17,main_lang='파이썬') :
   print(f'이름 : {name}\t나이 : {age}\t사용하는 언어 : {main_lang}')

profile('김두강')
profile('박태차')