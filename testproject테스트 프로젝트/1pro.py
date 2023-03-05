## 계산기 만들기
numbers = []
num1 = int(input("숫자1: "))
PL = input("연산자 입력: ")
num2 = int(input("숫자2: "))

while True:
    if PL == '+':
        print("{} {} {} = {}".format(num1, PL, num2, num1 + num2))
    elif PL == '*':
        print("{} {} {} = {}".format(num1, PL, num2, num1 * num2))
    elif PL == '/':
        print("{} {} {} = {}".format(num1, PL, num2, num1 / num2))
    elif PL == '-':
        print("{} {} {} = {}".format(num1, PL, num2, num1 - num2))
    else:
        print("잘못적었어")

    commend = input("다른 연산까지 ㄲ?: (y/n)")
    if commend.lower() == 'y':
        num1 = int(input("숫자1: "))
        PL = input("연산자 입력: ")
        num2 = int(input("숫자2: "))
    else:
        break

