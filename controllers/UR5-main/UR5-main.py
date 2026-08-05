"""
=========================================================
UR5 Autonomous Bottle Sorting Robot
Main Controller - Robotiq 3F Version
=========================================================
"""


from controller import Robot


from config import (

    STATE_SEARCH,
    STATE_WAIT_PICKUP,
    STATE_GRIP,
    STATE_MOVE,
    STATE_RELEASE,
    STATE_HOME,

    CENTER_TOLERANCE,
    MIN_BOTTLE_WIDTH,
    DISTANCE_SENSOR_NAME,
    DISTANCE_THRESHOLD

)


from poses import (

    HOME_POSE,
    HOME_HOVER_POSE,
    get_pose

)


from motion import UR5Motion

from gripper import Gripper

from vision import Vision




# ========================================================
# INITIALIZE
# ========================================================


robot = Robot()


timestep = int(
    robot.getBasicTimeStep()
)



print("==============================")
print(" UR5 SORTING ROBOT STARTED ")
print("==============================")




# ========================================================
# MODULES
# ========================================================


motion = UR5Motion(robot)

gripper = Gripper(robot)

vision = Vision(robot)




# ========================================================
# SENSORS
# ========================================================

distance_sensor = robot.getDevice(DISTANCE_SENSOR_NAME)
if distance_sensor:
    distance_sensor.enable(timestep)
    print("Distance sensor enabled")
else:
    print("Warning: Distance sensor not found")


# ========================================================
# HOME
# ========================================================


print(
    "Moving to home position"
)


motion.move_to(
    HOME_POSE
)



gripper.open()



for i in range(50):

    robot.step(timestep)



print(
    "System Ready"
)




# ========================================================
# VARIABLES
# ========================================================


state = STATE_SEARCH


detected_colour = None


detection_data = None





# ========================================================
# MAIN LOOP
# ========================================================


while robot.step(timestep) != -1:



    # ====================================================
    # SEARCH
    # ====================================================


    if state == STATE_SEARCH:


        detection_data = (
            vision.detect_bottle()
        )


        if detection_data:


            detected_colour = (
                detection_data["colour"]
                .strip()
                .lower()
            )


            print("======================")
            print(
                "Bottle detected:",
                detected_colour
            )
            print("======================")


            state = STATE_WAIT_PICKUP





    # ====================================================
    # WAIT PICKUP
    # ====================================================


    elif state == STATE_WAIT_PICKUP:

        # Read distance sensor every step, regardless of vision
        if distance_sensor:
            dist_val = distance_sensor.getValue()
        else:
            dist_val = 1000.0

        new_detection = (
            vision.detect_bottle()
        )

        if new_detection:
            detection_data = new_detection

        x = detection_data["x"]
        width = detection_data["width"]

        print(
            "Waiting...",
            "X:",
            x,
            "Width:",
            width,
            "Dist:",
            dist_val
        )

        if dist_val < DISTANCE_THRESHOLD:



                print("======================")
                print(
                    "Bottle reached gripper"
                )
                print("======================")


                state = STATE_GRIP







    # ====================================================
    # GRIP
    # ====================================================


    elif state == STATE_GRIP:



        print(
            "Closing 3F gripper"
        )


        gripper.close()



        # allow fingers to close fully

        for i in range(60):

            robot.step(timestep)



        print(
            "Bottle secured"
        )


        vision.clear_detection()


        state = STATE_MOVE






    # ====================================================
    # MOVE
    # ====================================================


    elif state == STATE_MOVE:



        print(
            "Moving to:",
            detected_colour
        )



        target_pose = get_pose(
            detected_colour
        )



        if target_pose:



            motion.move_to(
                target_pose
            )


            state = STATE_RELEASE



        else:


            print(
                "Pose not found"
            )







    # ====================================================
    # RELEASE
    # ====================================================


    elif state == STATE_RELEASE:



        print(
            "Opening gripper"
        )


        gripper.open()



        for i in range(40):

            robot.step(timestep)



        state = STATE_HOME






    # ====================================================
    # HOME
    # ====================================================


    elif state == STATE_HOME:



        print(
            "Returning home"
        )



        motion.move_to(
            HOME_HOVER_POSE
        )

        motion.move_to(
            HOME_POSE
        )



        detected_colour = None

        detection_data = None



        state = STATE_SEARCH