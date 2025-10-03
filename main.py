game_name = "Escaping" #TODO, name your game project
print(f"Welcome to {game_name}!")
print("====================")

# Ask for the character name
name = input("Before we begin, what is your character's name? \n> ")

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

player = {
    'name': name,
    'health': 100,
    'coin': 0
}
import random

events = ["find a coin", "meet a monster", "do nothing"]
event = random.choice(events)

print("While exploring, you {event}!")

if event == "find a coin":
    player['coin'] += 1
    print(f"After finding a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player['health'] -= 10
    print(f"After meeting a monster, {player['name']} now has {player['health']} health.")
elif event == "do nothing":
    print(f"{player['name']} did nothing")    