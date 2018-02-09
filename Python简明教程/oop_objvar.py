class Robot:
    """表示有一个带有名字的机器人。"""
    # 一个类变量，用来计数机器人的数量
    population = 0
    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候。"""
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

# 输出
# (Initializing R2-D2)
# Greetings, my masters call me R2-D2.
# We have 1 robots.
# (Initializing C-3PO)
# Greetings, my masters call me C-3PO.
# We have 2 robots.
# Robots can do some work here.
# Robots have finished their work. So let's destroy them.
# R2-D2 is being destroyed!
# There are still 1 robots working.
# C-3PO is being destroyed!
# C-3PO was the last one.
# We have 0 robots.
