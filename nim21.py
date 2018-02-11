# Nim 21 Two Player Game With Function of Starting
coins=21
start = None
while start not in ("F", "S","f","s"):
    print("\n----------------------------------------------------------------------------")
    print("START GAME")
    start = str(input("FIRST PLAYER PRESS F" "\n" "SECOND PLAYER PRESS S"))
if start.upper() == "F":
    player = 1
elif start.upper() == "S":
    player = 2

while True:
    print("player",player)
    while True:
        pick_up=int(input("choose 1 or 2 or 3:\n"))
        if pick_up in [1,2,3] and (pick_up<coins or pick_up<=coins):
            break
        print("out of possible range")
    coins=coins-pick_up
    print("the remain coins are ",coins)
    if coins==0 or coins<0:
        print("player",player,"won")
        break
    if player==1:
        player=2
    else:
        player=1
print("Game Over!")
