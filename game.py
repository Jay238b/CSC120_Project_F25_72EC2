import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 100
        self.coin = 0

    def move(self, direction, map_size):
        old_x, old_y = self.x, self.y

        if direction == "s": 
            if self.x < map_size - 1:
                self.x += 1
            else:
                print("You cannot move that way!")
        elif direction == "w":
            if self.x > 0:
                self.x -= 1
            else:
                print("You cannot move that way!")
        elif direction == "d":
            if self.y < map_size - 1:
                self.y += 1
            else:
                print("You cannot move that way!")
        elif direction == "a":
            if self.y > 0:
                self.y -= 1
            else: print("You cannot move that way!")
        else: 
            print("You cannot move that way!")
        
        if (old_x, old_y) == (self.x, self.y) and direction in "wasd":
            if not(
                (direction == "s" and old_x < map_size - 1) or
                (direction == "w" and old_x > 0) or
                (direction == "d" and old_y < map_size - 1) or
                (direction == "a" and old_y > 0)
            ):
                pass

class GameMap:
    def __init__(self):
        self.size = 9
    
    def draw(self, player):
        for j in range(self.size):
            row = ""
            for i in range(self.size):
                if i == player.x and j == player.y:
                    row += "C "
                elif i == self.size - 1 and j == self.size - 1:
                    row += "M "
                else:
                    row += ". "
            print(row)
        print(f"Health: {player.health} Coin: {player.coin}")

class Game:
    def __init__(self):
        self.game_name = "Treasure Hunt"
        self.name = ""
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.player = Player()
        self.map = GameMap()

    def check_event(self):
        event = random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
            print("You found a coin!")
        elif event == "meet a monster":
            self.player.health -= 10
            print("A monster attacked you!")
        else: 
            print("Nothing happens...")
    
    def play(self):
        print("Welcome!")
        self.player.name = input("Enter your name: ")

        while True:
            self.map.draw(self.player)

            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("You reached the exit!")
                break

            move = input("Move (w/a/s/d): ")
            self.player.move(move, self.map_size)
            self.check_event()

if __name__ == "__main__":
    Game().play()