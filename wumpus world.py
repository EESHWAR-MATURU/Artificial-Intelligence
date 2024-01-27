import random

class WumpusWorld:
    def __init__(self, size=4, num_pits=3):
        self.size = size
        self.agent_location = (0, 0)
        self.gold_location = (random.randint(0, size-1), random.randint(0, size-1))
        self.pit_locations = set()
        self.wumpus_location = (random.randint(0, size-1), random.randint(0, size-1))
        self.arrows = 1
        self.game_over = False

        # Randomly place pits
        while len(self.pit_locations) < num_pits:
            row, col = random.randint(0, size-1), random.randint(0, size-1)
            if (row, col) != self.gold_location and (row, col) != self.wumpus_location:
                self.pit_locations.add((row, col))

    def print_percept(self):
        row, col = self.agent_location
        percept = "You are in room ({},{}).".format(row, col)
        if self.agent_location == self.gold_location:
            percept += " You see a glitter."
        if self.agent_location == self.wumpus_location:
            percept += " You smell a terrible stench."
        if self.agent_location in self.pit_locations:
            percept += " You feel a breeze."
        if self.arrows > 0:
            percept += " You have {} arrow(s) left.".format(self.arrows)
        print(percept)

    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.agent_location == self.wumpus_location:
                self.game_over = True
                print("You killed the Wumpus! You win!")
            else:
                print("You missed the Wumpus.")
        else:
            print("You have no arrows left.")

    def move(self, direction):
        row, col = self.agent_location
        if direction == "UP" and row > 0:
            self.agent_location = (row - 1, col)
        elif direction == "DOWN" and row < self.size - 1:
            self.agent_location = (row + 1, col)
        elif direction == "LEFT" and col > 0:
            self.agent_location = (row, col - 1)
        elif direction == "RIGHT" and col < self.size - 1:
            self.agent_location = (row, col + 1)

    def action(self, action):
        if action == "MOVE":
            direction = input("Enter direction (UP, DOWN, LEFT, RIGHT): ").upper()
            self.move(direction)
        elif action == "SHOOT":
            self.shoot()
        elif action == "GRAB" and self.agent_location == self.gold_location:
            print("You grabbed the gold!")
            self.gold_location = None
        elif action == "CLIMB" and self.agent_location == (0, 0):
            if self.gold_location is None:
                print("You climbed out of the cave without gold. You win!")
            else:
                print("You climbed out of the cave with the gold. You win!")
            self.game_over = True

    def play(self):
        print("Welcome to the Wumpus World!")
        while not self.game_over:
            self.print_percept()
            action = input("Enter action (MOVE, SHOOT, GRAB, CLIMB, QUIT): ").upper()

            if action == "QUIT":
                print("You quit the game.")
                break
            elif action in ["MOVE", "SHOOT", "GRAB", "CLIMB"]:
                self.action(action)
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    size = 4  
    wumpus_world = WumpusWorld(size)
    wumpus_world.play()
