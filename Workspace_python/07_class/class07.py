class HelloStaticDeco:
    class_var = "class variable"

    def __init__(self):
        self.name = "instance variable"
        
    @staticmethod
    def static_method():
        print(f"static method : {HelloStaticDeco.class_var}")
        # static method 내에서 인스턴스 변수 사용 불가!
        # print(self.name)

    def instance_method(self):
        print(f"self : {self.name} / class : {HelloStaticDeco.class_var}")


if __name__ == "__main__":
    class07 = HelloStaticDeco()
    class07.static_method()
    class07.instance_method()
