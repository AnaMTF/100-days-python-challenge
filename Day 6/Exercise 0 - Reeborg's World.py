def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
#for i in range(6):
#    jump()
#for the hurdle 1  
nr_herdles = 6
while nr_herdles > 0:
    jump()
    nr_herdles -=1
#hurdle 2
while not at_goal():
    jump()
#hurdle 3
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump() #note that i erased the first move() from jump() so it doesnt crash in a wall
