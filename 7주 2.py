# 문자 메시지 길이를 판별하여 요금을 산출하는 함수
def check_length_of_message(message):
    # 메시지 길이가 20자 이하일 경우 요금은 50원
    if len(message) <= 20:
        return 50
    # 메시지 길이가 20자를 초과할 경우 요금은 100원
    else:
        return 100

# 사용자로부터 문자 메시지를 입력 받음
message = input("문자 메시지를 입력하세요: ")

# 요금을 계산하고 출력
charge = check_length_of_message(message)
print(f"문자 요금은 {charge}원입니다.")
