import random
words = ["가위", "향수", "자동차", "총기거치대", "수입도구"]
name = random.choice(words)
total_score = 0
limit_score = 10

print("끝말잇기를 시작하겠습니다.")
print("규칙은 간단합니다. 가장 마지막으로 끝나는 단어의 마지막 글자로 새로운 단어를 말하시면 됩니다.")
print("시작 단어는 {}입니다.".format(name))


while True:
    answer = input("(name)>>")
    words.append(name)
    if name[-1] == answer[0]:
        print("다음단어를 입력해주세요: ")
        name = answer
        total_score += 1
    elif name[-1] != answer[0]:
        print("잘못된 단어를 입력했습니다. \n게임을 종료합니다:(")
        break

if total_score >= limit_score:
    print("=" * 10)
    print("점수:      {}    ".format(total_score))
    print("=" * 10)
    print("승리")

else:
    print("=" * 10)
    print("점수:      {}    ".format(total_score))
    print("=" * 10)
    print("패배")
