#les1 example

developer = 'Laziza'
text = 'created'
social_media = 'Lazizagram'

print(developer, text, social_media)


# #les 2 example if elif else
a = int(input())
if a > 100:
    print('a is bigger than 100')
elif a < 100:
    print('a is smaller than 100')
else:
    print('a is 100')

#les 3 example методы для изменения
name = ['Leyla', 'Katya', 'Anna', 'Kseniya']
name.sort()
print(name)

name = ['Leyla', 'Katya', 'Anna', 'Kseniya']
name.reverse()
print(name)

#les 4 for
my_tuple = (6, 4, '2')
for i in range(1, 100):
    print(f'{my_tuple}')

# while
names = ['Irina', 'Shaykh','Ariana']

while True:
    new = input('Who should be added?')
    names.append(new)
    print(names)


#les 5
nums = [1, 2, 3]
my_list = [i for i in range(1,11) if i in nums]

print(my_list)

#les 6 example
nums = [1, 2, 3]
my_list = [i for i in range(1, 11) if i in mums]

print(my_list)


#les 7 functions example

def create_instructor():
    instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}

    if 'name' in instructor:
        return 'Yes, there is'
    else:
        return 'I do not understand it'

create_instructor()

#les 8 *args example

def my1(*args):
    if 'Jordan' in args:
        print('There is')
    else:
        print('There is not')

my1('Jordan', 'Pasha', 'Pavel')


#les 9 example object oriented programming
class Car:
    def __int__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

cobalt = Car('Chevrolet', 'White', 2022)
gentra = Car('Ravon', 'Black', 2019)

print(cobalt.model, gentra.model)

#les 10 inheritance example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


# Example usage
if __name__ == "__main__":

    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog.speak())
    print(cat.speak())


