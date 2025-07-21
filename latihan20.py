import random

komputer = random.randint(1, 10)

taruhan = int(input("taruhan: "))
player = int(input("tebak: "))

while (player != komputer):
    taruhan = taruhan - komputer
    print(f"taruhan: {taruhan}")
    print(f"komputer: {komputer}")
    print(f"tebak: {player}")
    print("Player Lose!")
    if taruhan < 1:
        break
    player = int(input("tebak: "))

if taruhan > 0:
    taruhan = taruhan + komputer
    print(f"taruhan: {taruhan}")
    print(f"komputer: {komputer}")
    print(f"teabk: {player}")
    print("Player Win!")
else:
    print("tidak cukup taruhan!")