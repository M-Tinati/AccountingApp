Creatures = [
    {"name": "Wolf", "age": 7, "health": 80},
    {"name": "Bear", "age": 10, "health": 45},
    {"name": "Fox", "age": 3, "health": 20}
]

def get_creature_status(creature):
    if creature["health"] >= 70:
        return "Healthy"
    elif creature["health"] >= 30:
        return "Weak"
    else:
        return "Critical"

for creature in Creatures:
    status = get_creature_status(creature)
    print(f"{creature['name']} -> {status}")
    
    
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age!")
    
try:
    health = int(input("Health: "))
except ValueError:
    print("Invalid health.")
finally:
    print("Input process finished.") 

with open("world.txt","a") as file:
    file.write("\nRead")
    
with open("world.txt", "r") as file:
    content = file.read()

print(content)

import json

creatures = [
    {"name": "Wolf", "health": 80},
    {"name": "Bear", "health": 25},
    {"name": "Fox", "health": 60}
]

with open("creatures.json", "w") as file:
    json.dump(creatures, file)  
    
with open("creatures.json", "r") as file:
    creatures = json.load(file)

print(creatures)