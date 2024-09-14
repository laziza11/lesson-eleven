

#words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'wave']
#past_tense = []
#for word in words:
    #if word[-1] != 'e':
        #past_tense.append(word+'ed')
    #else:
        #past_tense.append(word+'d')
#print(past_tense)
#function len counts the length of the list

#spam = 'Hello'

#while spam == 'Hello':
    #print(spam)



#nabor = ('1', 2, 'a')

#while 'a' in nabor:
    #print('it is')

#p = ['m', 'my', 23]
#i = 0
#while     not finished



names = [ 'Lily', 'Jem', 'Oscar']

numbers = [ 123, 234, 456]

services = ['call', 'check', 'text']

while True:
    x = input('Select category: ')
    if x == 'name':
        y = input('Enter the name: ')
        names.append(y)
        print(y +' is added to the names list')
        print(names)
    elif x == 'number':
        y = input('Enter the number: ')
        numbers.append(y)
        print(y + ' is added to the numbers list')
        print(numbers)
    elif x == 'service':
        y = input('Enter the service: ')
        print(y + ' is added to the services list')
        services.append(y)
        print(services)
    elif x == 'Stop':
        print('bye bye')
        break
    else:
        print('Wrong input, try again!')



