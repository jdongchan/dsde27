class Car():
    instance_count = 0

    # 인스턴스 메서드(초기화)
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count += 1
    # 인스턴스 메서드
    def move(self, speed):
        self.speed = speed
        print('자동차({0} & {1})가 '.format(self.size, self.color), end='')
        print('시속 {0}킬로미터로 전진'.format(self.speed))

    def auto_cruise(self):
        print('자율 주행 모드')
        self.move(self.speed) #move() 함수의 인자로 인스턴스 변수를 입력
    # 정적 메서드
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print('이 자동차는 전기차입니다.')
        elif(10 <= model_code < 20):
            print('이 자동차는 가솔린차입니다.')
        else:
            print('이 자동차는 디젤차입니다.')
    # 클래스 메서드
    @classmethod
    def count_instance(cls):
        print('자동차 객체의 개수: {0}'.format(cls.instance_count))

if __name__ == '__main__':
    Car.count_instance()

    car1 = Car('small', 'red')
    Car.count_instance()

    car2 = Car('big', 'green')
    Car.count_instance()