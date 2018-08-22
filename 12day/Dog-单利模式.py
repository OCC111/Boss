class Dog():
    __instance = None
    def __init__(self,name):
        a = 0
        if a == 0:
            a += 1
            print("已经执行了%d次"%a)
            self.name = name
        else:
            print("我还在哦！")
            a > 0
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            print("我来了")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("好久不见爱你哦")
            return cls.__instance
dog = Dog("二哈")
dog1 = Dog("小天全")
print(dog.name)
print(dog1.name)
