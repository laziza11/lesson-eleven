#a = lambda x: x**2
#print(a(10))
#b = lambda y, u: y + u
#print(b(2,3))
#x = lambda e: e
#print(x(9))

#a = int(input('Enter square side: '))
#square = lambda a: 4 * a #параметр это местоб заготовка для каких-либо значений ф аргументы это значения которые мы даем при вызове функции

#print(f'Square Perimeter is: {square(a)}')


#a = int(input('Enter square side: '))

#perimeter = lambda a: 4 * a

#print(f'Square perimeter is: {perimeter(a)}')


#def sum(a, b):

    #return(a + b)

#print(sum(48, 66))

# *args задавать любое количество аргументов
# **kwargs like *args just keeps in pairs like a dictionary

#def spammer(*args):
    #for a in args:
        #print(a)

#spammer(1, 2, 3, 1, 2, 3, '4', 'Hello')

#def spam1(**kwargs):
    #for k,v in kwargs.items():
        #print(k, v)

#print(spam1(name= 'my1', age= 23))



#def odd_or_even(number):
    #if number % 2 == 0:
        #print('The number is even')
    #else:
        #print('The number is odd')

#while True:
#odd_or_even(int(input('Enter a number to check: ')))


client = {}
opened_rooms = [i for i in range(1, 41)]
empty_rooms = [i for i in range(1, 41)]
closed_rooms = []

while True:
    action = input('do you want to add client, delete client or view empty rooms: ')
    if action == 'add client':
        print(empty_rooms)
        new_client = input('Enter client name: ')
        closed_room = input('Enter room number: ')
        if closed_room not in empty_rooms:
            closed_room = input('This room is already taken, select another room: ')
        else:
            closed_rooms.append(closed_room)
    elif action == 'view empty rooms':
        print(empty_rooms)
    elif action == 'delete client':
        name = input('Enter the name you want to delete: ')
        client.remove(name)
        print(client)
    else:
        print('wrong input')


