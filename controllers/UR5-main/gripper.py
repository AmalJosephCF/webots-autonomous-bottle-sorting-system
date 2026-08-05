"""
=========================================================
UR5 Bottle Sorting Robot
Robotiq 3F Gripper Controller
=========================================================
"""


from config import (

    GRIPPER_MOTORS,

    GRIPPER_OPEN,

    GRIPPER_CLOSED,

    GRIPPER_SPEED

)



class Gripper:


    def __init__(self, robot):


        self.robot = robot


        self.motors = {}



        print("==============================")
        print("Initializing Robotiq 3F Gripper")
        print("==============================")




        # ================================================
        # LOAD MOTORS
        # ================================================


        for name in GRIPPER_MOTORS:


            motor = robot.getDevice(name)



            if motor is None:


                print(
                    "Missing motor:",
                    name
                )


            else:


                print(
                    "Connected:",
                    name
                )


                motor.setVelocity(
                    GRIPPER_SPEED
                )


                self.motors[name] = motor




        print(
            "Total motors:",
            len(self.motors)
        )



        self.open()



        for i in range(40):

            robot.step(
                int(robot.getBasicTimeStep())
            )



        print(
            "Robotiq 3F Ready"
        )





    def _set_motor_position(self, motor, target_pos):
        min_p = motor.getMinPosition()
        max_p = motor.getMaxPosition()
        if min_p < max_p:
            target_pos = max(min_p, min(target_pos, max_p))
        motor.setPosition(target_pos)


    # =====================================================
    # OPEN GRIPPER
    # =====================================================


    def open(self):


        print(
            "Opening 3F gripper"
        )



        for name, motor in self.motors.items():



            # palm joints
            if "palm" in name:


                self._set_motor_position(
                    motor,
                    0.0
                )



            # first and second finger joints

            elif (
                "joint_1" in name
                or
                "joint_2" in name
            ):


                self._set_motor_position(
                    motor,
                    GRIPPER_OPEN
                )



            # finger tips have negative range

            elif "joint_3" in name:


                self._set_motor_position(
                    motor,
                    -0.0523
                )








    # =====================================================
    # CLOSE GRIPPER
    # =====================================================


    def close(self):


        print(
            "Closing 3F gripper"
        )



        for name, motor in self.motors.items():



            # palm stays fixed

            if "palm" in name:


                self._set_motor_position(
                    motor,
                    0.0
                )



            elif (
                "joint_1" in name
                or
                "joint_2" in name
            ):


                self._set_motor_position(
                    motor,
                    GRIPPER_CLOSED
                )



            elif "joint_3" in name:


                self._set_motor_position(
                    motor,
                    -0.4
                )







    # =====================================================
    # HOLD BOTTLE
    # =====================================================


    def hold(self):


        print(
            "Holding bottle"
        )



        for name, motor in self.motors.items():



            if "palm" in name:


                self._set_motor_position(
                    motor,
                    0.0
                )



            elif (
                "joint_1" in name
                or
                "joint_2" in name
            ):


                self._set_motor_position(
                    motor,
                    0.45
                )



            elif "joint_3" in name:


                self._set_motor_position(
                    motor,
                    -0.25
                )