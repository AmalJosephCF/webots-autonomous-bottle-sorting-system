from controller import Robot, Keyboard


robot = Robot()

timestep = int(robot.getBasicTimeStep())


# ============================
# Keyboard
# ============================

keyboard = Keyboard()
keyboard.enable(timestep)



# ============================
# UR5e joints
# ============================

joint_names = [
    "shoulder_pan_joint",
    "shoulder_lift_joint",
    "elbow_joint",
    "wrist_1_joint",
    "wrist_2_joint",
    "wrist_3_joint"
]


motors = []
sensors = []
positions = []



# ============================
# Initialize joints
# ============================

for name in joint_names:

    motor = robot.getDevice(name)

    if motor is None:
        print("ERROR: Joint not found:", name)
        continue


    # Enable position sensor

    sensor = motor.getPositionSensor()
    sensor.enable(timestep)

    # wait for sensor initialization
    for _ in range(10):
        robot.step(timestep)


    # Set motor speed

    motor.setVelocity(1.5)


    motors.append(motor)
    sensors.append(sensor)


    # Store initial position safely

    value = sensor.getValue()

    if value != value:   # checks NaN
        value = 0.0

    positions.append(value)



print("""
========================================

        UR5e MANUAL POSE CONTROLLER

Controls:

Shoulder Pan
    1  increase
    2  decrease


Shoulder Lift
    3  increase
    4  decrease


Elbow
    5  increase
    6  decrease


Wrist 1
    7  increase
    8  decrease


Wrist 2
    9  increase
    0  decrease


Wrist 3
    -  increase
    =  decrease


P : Print REAL joint pose


========================================
""")



# Movement amount

step = 0.05



while robot.step(timestep) != -1:


    key = keyboard.getKey()



    if key != -1:

        print("Key pressed:", key)



    # ========================
    # Manual movement
    # ========================


    if key == ord('1'):
        positions[0] += step


    elif key == ord('2'):
        positions[0] -= step



    elif key == ord('3'):
        positions[1] += step


    elif key == ord('4'):
        positions[1] -= step



    elif key == ord('5'):
        positions[2] += step


    elif key == ord('6'):
        positions[2] -= step



    elif key == ord('7'):
        positions[3] += step


    elif key == ord('8'):
        positions[3] -= step



    elif key == ord('9'):
        positions[4] += step


    elif key == ord('0'):
        positions[4] -= step



    elif key == ord('-'):
        positions[5] += step


    elif key == ord('='):
        positions[5] -= step



    # ========================
    # Print REAL pose
    # ========================

    elif key == ord('P'):


        print("\n======================")
        print("REAL UR5 JOINT POSE")
        print("======================")


        for i,name in enumerate(joint_names):

            real_value = sensors[i].getValue()

            print(
                name,
                ":",
                round(real_value,5)
            )


        print("======================\n")



    # Apply target positions

    for i, motor in enumerate(motors):

        if positions[i] != positions[i]:   # NaN check
            positions[i] = 0.0

        motor.setPosition(
            positions[i]
        )