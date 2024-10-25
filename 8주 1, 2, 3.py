# 퀴즈 1번
import random

def random_lotto():
    result = []
    while len(result) < 6:
            num = random.randint(1,45)
            if num not in result:
                result.append(num)
    return result
print(random_lotto())

#퀴즈 2번
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1,10):
            print(f"{self.num} X {i} = {self.num * i}")

two_dan = Gugudan(2)
two_dan.output()

#퀴즈 3번

강아지가 배고플 때 먹이통을 건드리는 기능으로 급식 해주는 코드를 짧게 작성해보겠습니다.

# Dog 클래스는 강아지의 정보를 나타냄
class Dog:
    def __init__(self, name, age):
        """
        강아지의 이름과 나이를 초기화
        :param name: 강아지 이름
        :param age: 강아지 나이
        """
        self.name = name
        self.age = age
        self.is_hungry = True  # 기본적으로 배고픔

    def eat(self):
        """강아지에게 먹이를 주는 함수"""
        if self.is_hungry:
            print(f"{self.name}가 먹이를 먹습니다.")
            self.is_hungry = False
        else:
            print(f"{self.name}는 이미 배가 부릅니다.")

    def nudge_food_bowl(self):
        """강아지가 배고플 때 먹이통을 건드리는 함수"""
        if self.is_hungry:
            print(f"{self.name}가 먹이통을 건드리며 배고픔을 알립니다.")
        else:
            print(f"{self.name}는 배가 불러 먹이통을 건드리지 않습니다.")

    def check_hunger(self):
        """강아지의 배고픔 상태를 확인하는 함수"""
        return f"{self.name}는 배고픕니다." if self.is_hungry else f"{self.name}는 배가 부릅니다."


# 프로그램 실행 예시
dog = Dog("바둑이", 3)

dog.check_hunger()  # 배고픔 확인
dog.nudge_food_bowl()  # 배고플 때 먹이통 건드리기
dog.eat()  # 먹이 주기
dog.nudge_food_bowl()  # 다시 시도
dog.check_hunger()  # 배고픔 상태 다시 확인


