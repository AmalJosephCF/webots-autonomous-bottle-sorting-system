"""
=========================================================
UR5 Bottle Sorting Robot
Configuration File
=========================================================
"""


# ========================================================
# CAMERA
# ========================================================

CAMERA_NAME = "camera"

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480


CONFIDENCE_THRESHOLD = 0.80



# ========================================================
# YOLO MODEL
# ========================================================

MODEL_PATH = "best.pt"


CLASS_NAMES = [

    "red_bottle",
    "green_bottle",
    "blue_bottle",
    "yellow_bottle",
    "pink_bottle"

]



# ========================================================
# UR5 JOINTS
# ========================================================


JOINT_NAMES = [

    "shoulder_pan_joint",

    "shoulder_lift_joint",

    "elbow_joint",

    "wrist_1_joint",

    "wrist_2_joint",

    "wrist_3_joint"

]



# ========================================================
# UR5 POSITION SENSORS
# ========================================================


SENSOR_NAMES = [

    "shoulder_pan_joint_sensor",

    "shoulder_lift_joint_sensor",

    "elbow_joint_sensor",

    "wrist_1_joint_sensor",

    "wrist_2_joint_sensor",

    "wrist_3_joint_sensor"

]



# ========================================================
# ROBOTIQ 3F GRIPPER MOTORS
# ========================================================


GRIPPER_MOTORS = [

    # Palm joints

    "palm_finger_1_joint",

    "palm_finger_2_joint",


    # Finger 1

    "finger_1_joint_1",

    "finger_1_joint_2",

    "finger_1_joint_3",


    # Finger 2

    "finger_2_joint_1",

    "finger_2_joint_2",

    "finger_2_joint_3",


    # Middle finger

    "finger_middle_joint_1",

    "finger_middle_joint_2",

    "finger_middle_joint_3"

]



# ========================================================
# GRIPPER CONTROL
# ========================================================


GRIPPER_OPEN = 0.0

GRIPPER_CLOSED = 0.8

GRIPPER_SPEED = 0.8


DISTANCE_SENSOR_NAME = "distance sensor"
DISTANCE_THRESHOLD = 50


BOTTLE_RADIUS = 0.035




# ========================================================
# ROBOT SPEED
# ========================================================


ARM_SPEED = 1.2


POSITION_TOLERANCE = 0.02




# ========================================================
# TIMINGS
# ========================================================


WAIT_AFTER_GRIP = 1.0


WAIT_AFTER_RELEASE = 1.0


WAIT_AFTER_MOVE = 0.5




# ========================================================
# CONVEYOR
# ========================================================


CONVEYOR_SPEED = 0.1




# ========================================================
# PICKUP DETECTION
# ========================================================


PICKUP_LINE_X = 320



# Bottle size when close enough

MIN_BOTTLE_WIDTH = 80



CENTER_TOLERANCE = 70



PICKUP_TIMEOUT = 5.0




# ========================================================
# VISION TRACKING
# ========================================================


TRACK_MEMORY = 10


MIN_DETECTION_AREA = 200




# ========================================================
# STATE MACHINE
# ========================================================


STATE_SEARCH = 0


STATE_WAIT_PICKUP = 1


STATE_GRIP = 2


STATE_MOVE = 3


STATE_RELEASE = 4


STATE_HOME = 5




# ========================================================
# COLOURS
# ========================================================


RED = "red_bottle"


GREEN = "green_bottle"


BLUE = "blue_bottle"


YELLOW = "yellow_bottle"


PINK = "pink_bottle"