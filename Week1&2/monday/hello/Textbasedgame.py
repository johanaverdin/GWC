def level3():
    print("Type 'left' to go left or 'right' to go right.")
    level3=input()
    if level3=="left":
        print("You take a left turn and you are at the graveyard exit. You will be home soon>")
    elif level3=="right":
        print("You lost")
def level2():
    print("Type 'left' to go left or 'right' to go right.")
    level2=input()
    if level2== "left":
        print("You go left. You keep walking foward half a mile a new path comes up.")
        level3()
    elif level2=="right":
        print("You are walking and a cop catches you. Thats the end of you")

start=("You wake up in the middle of the night to the howling sound of a wolf. You find yourself at a grave yeard. You must find the way home without getting caught, no one is suppose to be at the grave yard.")
print(start)
print("Type 'left' to go left or 'right' to go right.")
level1=input()
if level1=="left":
    print("You decide to go left. You come aross two hungry wolfs. They eat you alive")
elif level1=="right":
    print("You turn right and you keep walking. You fall in to a mud puddle you must get up and keep moving.")
    level2()


