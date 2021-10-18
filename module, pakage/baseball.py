from baseball_game_engine import make_answer, check
def save_history(answer, count, name):
        with open('baseball_history.txt', 'w', encoding='utf-8') as f:
            f.write(f'{answer}:{count}:{name}\n')


def load_history():
    count_name = {}
    with open('baseball_history.txt', 'r', encoding='utf-8') as f:
        print('----history----')
        while True:
            line = f.readline()
            if line == '':
                break
            print(line.rstrip())
            line = line.rstrip()
            data = line.split(':')
            count_name[data[1]] = data[2]
            print(count_name)
        #top3
        count_name = sorted(count_name.items()) #정렬하기
        return count_name[:3] #top3

answer = make_answer()
# print(answer)
count = 0

#무한반복
while True:
#   숫자 묻자
    guess = input("뭘까?")
    #t를 입력하면, 불러오자, top3
    if guess == 't':
        top3 = load_history()
        print(top3)
    #숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue

    if len(guess) != len(answer):
        # raise InvalidLengthError('정답의 길이와 다른 숫자를 입력했습니다.')
        print(f'정답의 길이와 다른 숫자를 입력했습니다. {len(answer)} 문자')
        continue

    # strike, ball 판정하기
    strike, ball = check(guess, answer)
    count += 1

    # 출력하기
    print(f'{guess}\tstrike : {strike}\tball : {ball}\t{count} try')

    # 정답과 숫자가 같다면 끝내기
    if answer == guess:
        print('삐빅 정답입니다!')
        # 정답과 시도횟수 저장하기
        name = input('이름 : ')
        save_history(answer, count, name)
        # Top3 불러오기
        break