"""
=========================================================
UR5 Bottle Sorting Robot
Robot Joint Poses
=========================================================

All values are in radians.

Joint order:

0 - shoulder_pan_joint
1 - shoulder_lift_joint
2 - elbow_joint
3 - wrist_1_joint
4 - wrist_2_joint
5 - wrist_3_joint

=========================================================
"""


# ========================================================
# HOME / PICKUP POSITION
# ========================================================

HOME_POSE = [

    0.00011,     # shoulder_pan_joint
    0.00025,     # shoulder_lift_joint
    0.00008,     # elbow_joint
    0.00001,     # wrist_1_joint
    0.0,         # wrist_2_joint
    0.0          # wrist_3_joint

]


# ========================================================
# SAFE HOVER POSITION
# ========================================================

HOME_HOVER_POSE = [

    0.00011,     # shoulder_pan_joint
    -0.6,        # shoulder_lift_joint (high up to avoid baskets)
    0.00008,     # elbow_joint
    0.00001,     # wrist_1_joint
    0.0,         # wrist_2_joint
    0.0          # wrist_3_joint

]


# ========================================================
# SORTING BIN POSES
# ========================================================


RED_POSE = [

    0.9501,
    -0.6,
    0.00008,
    0.00001,
    0.0,
    0.0

]


GREEN_POSE = [

    1.6001,
    -0.6,
    0.00008,
    0.00001,
    0.0,
    0.0

]


BLUE_POSE = [

    2.6001,
    -0.6,
    0.00008,
    0.00001,
    0.0,
    0.0

]


YELLOW_POSE = [

    3.7001,
    -0.6,
    0.00008,
    0.00001,
    0.0,
    0.0

]


PINK_POSE = [

    4.4001,
    -0.6,
    0.00008,
    0.00001,
    0.0,
    0.0

]


# ========================================================
# POSE DICTIONARY
# ========================================================

SORTING_POSES = {


    "red_bottle": RED_POSE,

    "green_bottle": GREEN_POSE,

    "blue_bottle": BLUE_POSE,

    "yellow_bottle": YELLOW_POSE,

    "pink_bottle": PINK_POSE

}


# ========================================================
# Function
# ========================================================

def get_pose(color):

    """
    Returns the joint pose for detected bottle colour
    """

    if color in SORTING_POSES:

        return SORTING_POSES[color]


    else:

        print("Unknown colour:", color)

        return HOME_POSE