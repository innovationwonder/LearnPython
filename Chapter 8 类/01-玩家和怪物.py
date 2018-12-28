class Player():
    def __init__(self, name, hp, occu):
        self.__name = name # 类的封装
        self.hp= hp
        self.occu = occu

    def print_role(self):
        print('%s %s %s' %(self.__name, self.hp, self.occu))

    def updateName(self, new_name):
        self.__name = new_name


class Monster():
    '定义怪物类'
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def who(self):
        print('父类方法')


class Animals(Monster):
    def __init__(self, hp=10):
        super().__init__(hp) # 避免引用子类时再次初始化


class Boss(Monster):
    def who(self): # 多态
        print('子类方法')


a1 = Monster(122)
# print(a1.hp)
# print(a1.run())

a2 = Animals()
print(a2.hp)
print(a2.run())

a3 = Boss()
print(a3.who())

print(type(a3))
print(type(a1))
print(type(a2))

print(isinstance(a2, Monster))
print(isinstance(a1, Monster))

# user1 = Player('tom',100,'Night')
# user1.print_role()
#
# user1.updateName('Mike')
# user1.print_role()
# user1.__name = ('asf')
# user1.print_role()