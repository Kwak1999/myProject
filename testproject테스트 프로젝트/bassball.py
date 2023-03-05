from  random import randint
def baseballnumber():
    bass = []
    i = 0
    new_number = 0
    while i < 3:
        new_number = randint(0, 9)
        if new_number not in bass:
            bass.append(new_number)
            i += 1
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return bass
def base_ball():
    numbers_ = []
    i = 0
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while i < 3:
        num = int(input("{}번째 숫자를 입력하세요: ".format(i+1)))
        if num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if num in numbers_:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            numbers_.append(num)
            i += 1
    return numbers_
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    i = 0
    while i <len(guess):
        if guess[i] == solution[i]:
            strike_count += 1
            i += 1
        elif guess[i] in solution:
            ball_count += 1
            i += 1
        else:
            i += 1
    return strike_count, ball_count

ANSWER = baseballnumber()
tries = 0

while 1:
    mynum = base_ball()
    strike, ball = get_score(mynum, ANSWER)
    print("{}S {}B ".format(strike, ball))

    if strike == 3:
        tries += 1
        break
    else:
        tries += 1
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
