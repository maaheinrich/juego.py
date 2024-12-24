import random

class Card:
    def __init__(self, card_number = 0, role='Unknown yet.'):
        self.card_number = card_number
        self.role = role
        
    def set_role(self, role):
        self.role = role

    def __repr__(self):
        if self.card_number == 0:
            return 'No card has been drawn yet.'
        return f"Card role: {self.role}"

# Request number of players // Solicitar número de jugadores 
while True:
    try:
        num_players = int(input("Enter the number of players (4-7): "))
        if 4 <= num_players <= 7:
            break
        else:
            print("The number of players must be between 4 and 7.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Define role distributions // Definir distribuciones de roles 
roles_by_players = {
    4: ['Sheriff', 'Renegade', 'Outlaw', 'Outlaw'],
    5: ['Sheriff', 'Renegade', 'Outlaw', 'Outlaw', 'Bailliff'],
    6: ['Sheriff', 'Renegade', 'Outlaw', 'Outlaw', 'Outlaw', 'Bailliff'],
    7: ['Sheriff', 'Renegade', 'Outlaw', 'Outlaw', 'Outlaw', 'Bailliff', 'Bailliff']
}

# Assign roles to players // Asignar roles a los jugadores
roles = roles_by_players[num_players]
random.shuffle(roles)  # Mix roles randomly // Mezclar los roles aleatoriamente
players = [Card() for _ in range(num_players)]

for i, player in enumerate(players):
    player.set_role(roles[i])

# Reveal roles privately // Revelar roles de forma privada
for i, player in enumerate(players, start=1):
    print(f"\nPlayer {i}, it's your turn to see your card.")
    input("Press Enter to reveal your role (make sure others aren't looking!)...")
    print(f"Your role is: {player.role}")
    input("Press Enter to hide your role and pass to the next player...")
    print("\n" + "-" * 50)

# End of the distribution // Finalización del reparto
print("All players have drawn their cards. Let the game begin!")

