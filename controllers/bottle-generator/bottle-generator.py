from controller import Supervisor
import random


robot = Supervisor()


timestep = int(robot.getBasicTimeStep())


# Root world node
root = robot.getRoot()

children = root.getField("children")


# Bottle counter
counter = 0


# Timer
spawn_timer = 0


# Bottle colors
colors = [
    {
        "name": "red",
        "rgb": "1 0 0"
    },
    {
        "name": "green",
        "rgb": "0 1 0"
    },
    {
        "name": "blue",
        "rgb": "0 0 1"
    },
    {
        "name": "yellow",
        "rgb": "1 1 0"
    },
    {
        "name": "pink",
        "rgb": "1 0 1"
    }
]



def create_bottle():

    global counter


    # Conveyor starting position
    x =1.32731
    y = -0.0171027
    z =0.671927

    bottle_color = random.choice(colors)


    bottle = f"""
    Bottle {{
        translation {x} {y} {z}

        name "{bottle_color['name']}_bottle_{counter}"

        color {bottle_color['rgb']}
    }}
    """


    children.importMFNodeFromString(
        -1,
        bottle
    )


    print(
        "Created bottle:",
        bottle_color["name"]
    )


    counter += 1





while robot.step(timestep) != -1:


    spawn_timer += timestep / 1000


    # Create bottle every 5 seconds

    if spawn_timer >= 15:


        create_bottle()

        spawn_timer = 0