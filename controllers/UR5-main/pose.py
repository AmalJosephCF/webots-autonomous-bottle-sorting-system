"""
=========================================================
UR5 Bottle Sorting Robot
Robot Joint Poses
=========================================================

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

    0.00011,
    0.00025,
    0.00008,
    0.00001,
    0.0,
    0.0

]



# ========================================================
# BASKET POSITIONS
# ========================================================


RED_POSE = [

    0.9501,
    -0.34975,
    0.00008,
    0.00001,
    0.0,
    0.0

]


GREEN_POSE = [

    1.6001,
    -0.34975,
    0.00008,
    0.00001,
    0.0,
    0.0

]


BLUE_POSE = [

    2.6001,
    -0.34975,
    0.00008,
    0.00001,
    0.0,
    0.0

]


YELLOW_POSE = [

    3.7001,
    -0.34975,
    0.00008,
    0.00001,
    0.0,
    0.0

]


PINK_POSE = [

    4.4001,
    -0.34975,
    0.00008,
    0.00001,
    0.0,
    0.0

]



# ========================================================
# YOLO CLASS NAME MAPPING
# ========================================================

SORTING_POSES = {


    "red_bottle": RED_POSE,

    "green_bottle": GREEN_POSE,

    "blue_bottle": BLUE_POSE,

    "yellow_bottle": YELLOW_POSE,

    "pink_bottle": PINK_POSE

}




# ========================================================
# GET POSE
# ========================================================

def get_pose(color):


    color = color.strip().lower()


    print(
        "Looking for pose:",
        repr(color)
    )


    if color in SORTING_POSES:


        print(
            "Pose found for:",
            color
        )


        return SORTING_POSES[color]



    else:


        print("======================")
        print(
            "Unknown colour:",
            repr(color)
        )
        print("======================")


        return None