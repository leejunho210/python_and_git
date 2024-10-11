# 사용자 클래스를 정의합니다.
class User:
    # 초기화 메서드: 이름, 나이, 연락처를 입력받아 객체를 생성합니다.
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    # info() 메서드: 사용자 정보를 출력합니다.
    def info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.contact} 입니다.")

# 사용자 객체 생성 예시
user1 = User("홍길동", 25, "010-1234-1234")

# info() 함수 호출
user1.info()
