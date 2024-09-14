#task1 почтовый адрес
from turtle import width

print('Name: Laziza')
print('Email: lazizaaloudinova@gmail.com')



#task2 greeting

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')



#task3 room area
room_length = float(input('Enter room length: '))
room_width = float(input('Enter room width: '))

room_area = room_length * room_width

print(f'Room area: {room_area}')




#task3 garden area
garden_length = float(input('Enter garden length in pounds: '))
garden_width = float(input('Enter garden width in pounds: '))

garden_area_pounds = room_length * room_width
garden_area_acres = garden_area_pounds % 43560

print(f'Room area in acres: {garden_area_acres}')
