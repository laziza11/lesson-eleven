usernames = []
while True:
    x = input('Enter a username: ')
    if x in usernames:
        print('Username exists in the database, enter another: ')
    else:
        print('Username successfully added to the database!')
        usernames.append(x)
        print(usernames)
    