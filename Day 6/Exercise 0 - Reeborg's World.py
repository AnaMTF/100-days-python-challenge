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
#for the herdles marathon    
nr_herdles = 6
while nr_herdles > 0:
    jump()
    nr_herdles -=1
