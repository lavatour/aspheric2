""" This will approimate lens shappe for aspheric lens to focus at a single point."""

min = 0
max = 300
step = 1
goal = 19243

def function(x):
    r = x**2
    return r



def increment(min, max, goal):
    """ Define a function. Enter min max and goal.
    Incrementally approach a desired solution. """
    x = min
    dx = (max - min)/10
    for i in range(0,11):
        # function goes here
        if function(x + dx) < goal:
            x = x + dx
        if function(x + dx) > goal:
            break
    min = x
    max = x + dx
    return (min, max)

i = 0
min = 0
max = 300
while (max - min) > 0.0000001:
    i+= 1
    (min, max) = increment(min, max, 19243)
print(f"ave = {(min+max)/2, i}")







