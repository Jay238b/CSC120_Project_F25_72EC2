import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 100
        self.coin = 0

    def move(self, direction, map_size):
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
        

class GameMap:
    def __init__(self, size=9):
        self.size = size
    
    def draw(self, player):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if i == player.x and j == player.y:
                    row += "P "
                elif i == self.size - 1 and j == self.size - 1:
                    row += "M "
                elif i == 0 and j == 0:
                    row += "C "
                else:
                    row += ". "
            print(row)
        print(f"Health: {player.health} Coin: {player.coin}")

class Game:
    def __init__(self):
        self.game_name = "Treasure Hunt"
        self.player = Player()
        self.map_size = 9
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.map = GameMap(self.map_size)

    def check_event(self):
        event = random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
            print("You found a coin!")
        elif event == "meet a monster":
            self.player.health -= 10
            print("A monster attacked you!")
        elif event == "do nothing":
            print("Nothing happens.")
    
    def play(self):
        print("Welcome!")
        self.player.name = input("Enter your name: ")

        while True:
            self.map.draw(self.player)
            move = input("Move (w/a/s/d or quit): ").strip().lower()
            if move == "quit":
                print("Game over. Thanks for playing!")
                break
            self.player.move(move, self.map_size)
            self.check_event()

            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("You reached the exit!")
                break
            if self.player.health <= 0:
                print("You lost all health. Game Over!")

            
            

if __name__ == "__main__":
    Game().play()