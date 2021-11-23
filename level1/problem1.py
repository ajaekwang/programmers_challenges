# "신규 아이디 추천"
# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    # 1단계 : 소문자로 치환
    new_id = new_id.lower()
    # print("1단계", new_id)

    # 2단계 : 소문자, 숫자, '-', '_', '.' 외 모든 문자 제거
    new_id = list(new_id)
    for i in range(len(new_id)):
        if not (new_id[i].isalnum() or new_id[i] == "-" or new_id[i] == "_" or new_id[i] == "."):
            new_id[i] = ''

    new_id = ''.join(new_id)
    # print("2단계", new_id)

    # 3단계 : '.' 2번 이상 -> 1번
    new_id = list(new_id)
    prev = ""
    for i in range(len(new_id)):
        if new_id[i] == prev == ".":
            new_id[i] = ""
        else:
            prev = new_id[i]
    new_id = ''.join(new_id)
    # print("3단계", new_id)

    # 4단계 : '.' 처음이나 끝에 위치 -> 제거
    new_id = list(new_id)
    if new_id[0] == '.':
        new_id[0] = ''
    if new_id[-1] == '.':
        new_id[-1] = ''
    new_id = ''.join(new_id)
    # print("4단계", new_id)

    # 5단계 : 빈 문자열 -> 'a' 대입
    if not new_id:
        new_id = "a"
    # print("5단계", new_id)

    # 6단계 : 16자 이상 -> 15자 이하. 끝에 "." 제거
    new_id = list(new_id)
    if len(new_id) >= 16:
        new_id = new_id[:15]

    while new_id[-1] == ".":
        new_id[-1] = ''
    new_id = ''.join(new_id)
    # print("6단계", new_id)

    # 7단계 : 2자 이하 -> 마지막 문자 길이 3 될 때까지 반복 붙임
    while len(new_id) <= 2:
        new_id += new_id[-1]

    # print("7단계", new_id)

    answer = str(new_id)

    return answer


if __name__ == '__main__':
    input_list = ["...!@BaT#*..y.abcdefghijklm",
                  "z-+.^.",
                  "=.=",
                  "123_.def",
                  "abcdefghijklmn.p"]

    result_list = ["bat.y.abcdefghi",
                   "z--",
                   "aaa",
                   "123_.def",
                   "abcdefghijklmn"]

    for i in range(len(input_list)):
        if result_list[i] != solution(input_list[i]):
            # print(f"Wrong at {i}")
            # print(f"result = {result_list[i]}")
            # print(f"solution = {solution(input_list[i])}")
            break
    else:
        print("All pass!")
