import random

class Card:
    def __init__(self, card_number = 0, role = 'Unknow yet.'):
        self.card_number = card_number
        self.role = role
        
    def get_role(self):
        if self.card_number == 0:
            return 'You haven\'t draw any card yet!'
        if self.card_number == 1:
            self.role = 'Sheriff'
            return 'This card role is \'{role}\'.'.format(role = self.role)
        
        if self.card_number == 2:
            self.role = 'Outlaw'
            return 'This card role is \'{role}\'.'.format(role = self.role)
        
        if self.card_number == 3:
            self.role = 'Bailliff'
            return 'This card role is \'{role}\'.'.format(role = self.role)
        
        if self.card_number == 4:
            self.role = 'Renegade'
            return 'This card role is \'{role}\'.'.format(role = self.role)
    
    def __repr__(self):
        if self.card_number == 0:
            return 'No card has been drawn yet.'
        return 'This card number is {number} and \'{role}\' role.'.format(number = self.card_number, role = self.role)
        
card1 = Card()
i = 0
while i == 0:
    print('Welcome to \'BANG!\'')
    print('Please, type 1 to draw a card.')
    print('Type 2 to exit the game.')
    option = int(input())
    if option == 1:
        random_num = random.randint(1, 4)
        card1.card_number = random_num
        print(card1.get_role())
    elif option == 2:
        exit()
    else:
        print('Invalid option!')
        
        
            
    