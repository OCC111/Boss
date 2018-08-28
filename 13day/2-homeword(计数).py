class Student():
    def __init__(self,name):
        self.name = name
        self.list = []
        self.count = 0
    def school(self):
        a = 0
        while True:
            self.name = input("输入名字:")
            self.count += 1
            self.list.append(self.name)
            a += 1
            if a >= 10:
                print("您已经进入24小时360度无死角监控位置!")
                break



xm = Student("小名")
xm.school()
print("已经录取了%d个学生"%xm.count)
print(xm.list)
