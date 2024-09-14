#class Dress:
    #def __init__(self, designer, color, size):
      #self.designer = designer
      #self.color = color
      #self.size = size

    #def wash(self):
      #print('The dress is being washed')

#lily = Dress('Dolce', 'white', 'M')
#print(vars(lily))
#lily.wash()


#class Comment:
      #def __init__(self, username, text, likes=0):
            #self.username = username
            #self.text = text
            #self.likes = likes



# one = Comment('Lily', 'that video is fun', 3)
#
#
# print(vars(one))



#class BankAccount:
    #def __init__(self, client_name, balance=0):
        #self.client_name = client_name
        #self.balance = balance

    #def deposit(self):
        #deposit = int(input('Enter amount you wish to add to your account balance: '))
        #self.balance += deposit
        #print(f'Your current balance is {self.balance}')

    #def cash(self):
        #cash = int(input('Enter the amount you wish to withdraw: '))
        #self.balance -= cash
        #print(f'Your current balance is {self.balance}')

    #def my_balance(self):
        #print(f'You current balance is {self.balance}')


#Anne = BankAccount('Anne', 3000)

#print(vars(Anne))
#Anne.deposit()


class User:
    def __init__(self, name, email, age, number):
        self.name = name
        self.email = email
        self.age = age
        self.number = number

    def change_username(self, new_name):
        self.name = new_name

    def change_number(self, new_number):
        self.number = new_number

    def change_mail(self, new_email):
        self.email = new_email


Anna = User('anna', 'anna@gmail.com', 45, '998943445656')
print(vars(Anna))




