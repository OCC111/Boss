class house():
    def __init__(self):
        self.name = "绿野别墅"
        self.area = 2000
        self.list = []

    def __str__(self):
        msg = "我住在%s,面积:%d"%(self.name,self.area)
        return msg

class beds(house):
    def __init__(self):
        self.name = "海斯创品"
        self.size = 0

    def abed(self):
        a = 0
        while True:
            a+=1
            super().__init__()
            #print("-------------1------------")
            self.size += 10

            self.list.append(self.size)#保存床的大小到列表
            if self.size >= self.area:#如果床的大小，大于房子的面积打印床位已满
                print("床位已满,总共放置了%d张床"%a)
                break

lyxz = house()
#print(lyxz.name)
#print(lyxz.area)
print(lyxz)
hscp = beds()
hscp.abed()

for i in hscp.list:
    print("总面积是:%d"%i)

