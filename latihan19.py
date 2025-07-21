import random

komputer = random.randint(1, 10)

player = int(input("tebak: "))

while player != komputer:
    print(f"komputer: {komputer}")
    print(f"tebak: {player}")
    print("Player Lose!")
    player = int(input("tebak: "))

print(f"komputer: {komputer}")
print(f"teabk: {player}")
print("Player Win!")