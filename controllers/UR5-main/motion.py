"""
=========================================================
UR5 Bottle Sorting Robot
UR5 Motion Controller
=========================================================
"""


from controller import Robot


from config import (
    JOINT_NAMES,
    ARM_SPEED,
    POSITION_TOLERANCE
)



class UR5Motion:


    def __init__(self, robot):

        """
        Initialize UR5 joints
        """


        self.robot = robot


        self.joints = []

        self.sensors = []



        timestep = int(
            robot.getBasicTimeStep()
        )



        print("==============================")
        print("Initializing UR5 joints")
        print("==============================")



        # =================================================
        # LOAD JOINT MOTORS
        # =================================================


        for name in JOINT_NAMES:


            motor = robot.getDevice(name)



            if motor is None:

                print(
                    "ERROR: Motor not found:",
                    name
                )


            else:

                print(
                    "Connected motor:",
                    name
                )


                motor.setVelocity(
                    ARM_SPEED
                )



            self.joints.append(
                motor
            )





        # =================================================
        # LOAD POSITION SENSORS
        # =================================================


        print("==============================")
        print("Initializing position sensors")
        print("==============================")



        for i, joint in enumerate(self.joints):


            if joint is None:


                self.sensors.append(
                    None
                )

                continue




            sensor = (
                joint.getPositionSensor()
            )



            if sensor is None:


                print(
                    "ERROR: Sensor missing for:",
                    JOINT_NAMES[i]
                )



            else:


                print(
                    "Sensor connected:",
                    JOINT_NAMES[i]
                )


                sensor.enable(
                    timestep
                )



            self.sensors.append(
                sensor
            )



        print("==============================")
        print("UR5 Motion Ready")
        print("==============================")






    # =====================================================
    # MOVE ROBOT
    # =====================================================


    def move_to(self, pose):


        print("----------------")
        print("Moving robot")
        print("----------------")



        for i in range(6):


            if self.joints[i] is not None:


                self.joints[i].setPosition(
                    pose[i]
                )



        self.wait_until_reached(
            pose
        )



        print(
            "Reached target pose"
        )






    # =====================================================
    # WAIT UNTIL TARGET REACHED
    # =====================================================


    def wait_until_reached(self, target):


        timestep = int(
            self.robot.getBasicTimeStep()
        )



        timeout = 0



        while True:



            if self.robot.step(timestep) == -1:

                break




            reached = True



            for i in range(6):


                sensor = self.sensors[i]



                if sensor is None:


                    continue




                current = (
                    sensor.getValue()
                )



                error = abs(
                    current - target[i]
                )



                if error > POSITION_TOLERANCE:


                    reached = False





            if reached:


                break




            timeout += 1




            if timeout > 300:


                print("====================")
                print("Motion timeout")
                print("====================")

                break







    # =====================================================
    # GET CURRENT POSE
    # =====================================================


    def get_current_pose(self):


        pose = []



        for sensor in self.sensors:


            if sensor is not None:


                pose.append(
                    sensor.getValue()
                )


            else:


                pose.append(
                    0.0
                )



        return pose






    # =====================================================
    # PRINT CURRENT POSE
    # =====================================================


    def print_pose(self):


        print("====================")
        print("CURRENT UR5 POSE")
        print("====================")



        for i in range(6):


            if self.sensors[i] is not None:


                print(

                    JOINT_NAMES[i],

                    ":",

                    round(
                        self.sensors[i].getValue(),
                        5
                    )

                )


        print("====================")