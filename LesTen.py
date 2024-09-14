#class Animal:
    #def make_sound(self, s):
        #print(s)



#class Horse(Animal):
    #def galop(self):
        #print('bejit galopom')


#lion = Animal()
#pony = Horse()
#pony.make_sound('Igogo')


#class Celebrity:
    #def post_content(self, how_often):
        #print(how_often)


#class Singer(Celebrity):
    #def sing(self, live, autotune):
        #print(live, autotune)


#jazz_singer = Singer()

# class Car:
#     def __init__(self, model, color, year): #for each class create a function and define the parameters
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)#instead of writing three lines of parameters take them from parent class
#         self.sponsor = sponsor
#
# clk = SuperCar('CLK GTR', 'Silver', 1989, 'Mercedes')
# print(vars(clk))

#  NOT SOLVED       class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def from_string(cls, string):
#         return cls(int(string))
#
#
# my_obj = MyClass.from_string('6')
# print(my_obj.value)

# #
#
#
# rectangle.width = 6
# print(rectangle.area)

#

class Player:
    def __int__(self, strength, accuracy, speed, endurance):
        self.strength = strength
        self.accuracy = accuracy
        self.speed = speed
        self.endurance = endurance

class Attacker(Player):
    def __int__(self, strength, accuracy, speed, endurance):
        super().__init__(self, strength, accuracy, speed, endurance)

    def attack(self):
        print('Attacked')


class Defense(Player):
    def __int__(self, strength, accuracy, speed, endurance, reliable):
        super().__init__(self, strength, accuracy, speed, endurance)
        self.reliable = reliable


class SemiDefense(Player):
    def __int__(self, strength, accuracy, speed, endurance, reaction):
        super.__init__(self, strength, accuracy, speed, endurance)
        self.reaction = reaction





#git control version system , local mashine
# vs hithub platform, server