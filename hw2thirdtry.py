user1 = 0
user2 = 0

max_score = int(input('Enter number of rounds: '))
user_one_choice = input('User1, Enter rock, paper or scissors: ')
user_two_choice = input('User2, Enter rock, paper or scissors: ')

def game():
    global user1, user2
    if user_one_choice == 'rock' and user_two_choice == 'scissors':
        user1 += 1
        print('User1 wins1')
    elif user_one_choice == 'scissors' and user_two_choice == 'paper':
        user1 += 1
        print('User1 wins1')
    elif user_one_choice == 'paper' and user_two_choice == 'rock':
        user1 += 1
        print('User1 wins1')
    else:
        user2 += 1
        print('User2 wins!')

game()

while True:
    user_one_choice = input('User1, Enter rock, paper or scissors: ')
    user_two_choice = input('User2, Enter rock, paper or scissors: ')
    game()

    if user1 == max_score or user2 == max_score:
        break

