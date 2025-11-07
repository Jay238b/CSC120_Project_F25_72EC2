import random

game_name = "Escaping" #TODO, name your game project
print(f"Welcome to {game_name}!")
print("====================")

# Ask for the character name
name = "Tester"

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

player = {
    'name': name,
    'health': 100,
    'coin': 0,
    'x': 0,
    'y': 0
}



def check_event():
    global player, events
    event = random.choice(events)
    events = ["find a coin", "meet a monster", "do nothing"]
    if event == "find a coin":
        player['coin'] += 1
    elif event == "meet a monster":
        player['health'] -= 10

map_size = 9

def draw_ui(x, y):
    print("=========================")
    for i in range(map_size):
        for j in range(map_size):
            if i == player['x'] and j == player['y']:
                print("C", end = "  ") # Two spaces
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end = "  ")
            else:
                print(".", end = "  ")
    print("=========================")
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coin: {player['coin']}")
    print("=========================")

def move(direction):
    global player
    if direction == 'w' and player['x'] > 0:
        player['x'] -= 1
    elif direction == 'a' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 's' and player['x'] < map_size - 1:
        player['x'] += 1
    elif direction == 'd' and player['y'] < map_size - 1:
        player['y'] += 1
        ...
    else:
        print("You cannot move that way")

def main():
    draw_ui(0,0)
    direction = input("Your next move (w/a/s/d/q)")
    while direction != 'q':
        move(direction)

        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break
        
        check_event()
        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q)")

if __name__ == '__main__':
    main()