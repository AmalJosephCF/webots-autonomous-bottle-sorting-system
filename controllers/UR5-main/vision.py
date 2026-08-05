"""
=========================================================
UR5 Bottle Sorting Robot
YOLO Vision Controller
=========================================================
"""


import numpy as np
import cv2


from ultralytics import YOLO


from config import (

    CAMERA_NAME,

    CAMERA_WIDTH,
    CAMERA_HEIGHT,

    MODEL_PATH,

    CONFIDENCE_THRESHOLD,

    MIN_BOTTLE_WIDTH,

    CENTER_TOLERANCE

)



class Vision:



    def __init__(self, robot):


        print("Initializing camera...")


        self.camera = robot.getDevice(
            CAMERA_NAME
        )


        if self.camera is None:

            raise Exception(
                "Camera not found"
            )



        timestep = int(
            robot.getBasicTimeStep()
        )


        self.camera.enable(
            timestep
        )


        print(
            "Camera enabled"
        )



        print(
            "Loading YOLO model..."
        )


        self.model = YOLO(
            MODEL_PATH
        )


        print(
            "YOLO model loaded"
        )


        self.last_detection = None





    # ==================================================
    # GET CAMERA IMAGE
    # ==================================================


    def get_image(self):


        image = self.camera.getImage()



        if image is None:

            return None



        # Webots BGRA -> numpy

        img = np.frombuffer(

            image,

            np.uint8

        )



        img = img.reshape(

            (
                CAMERA_HEIGHT,
                CAMERA_WIDTH,
                4
            )

        )



        # BGRA -> BGR

        img = cv2.cvtColor(

            img,

            cv2.COLOR_BGRA2BGR

        )



        return img





    # ==================================================
    # DETECT BOTTLE
    # ==================================================


    def detect_bottle(self):


        frame = self.get_image()



        if frame is None:

            return None



        results = self.model.predict(

            source=frame,

            imgsz=640,

            conf=CONFIDENCE_THRESHOLD,

            verbose=False

        )

        if len(results) > 0:
            annotated_frame = results[0].plot()
            cv2.imshow("Robot Camera View", annotated_frame)
            cv2.waitKey(1)

        best = None

        best_conf = 0



        for result in results:


            for box in result.boxes:



                confidence = float(
                    box.conf[0]
                )


                if confidence < CONFIDENCE_THRESHOLD:

                    continue



                if confidence < best_conf:

                    continue



                best_conf = confidence



                class_id = int(
                    box.cls[0]
                )



                colour = self.model.names[
                    class_id
                ]



                x1,y1,x2,y2 = box.xyxy[0]



                x1=int(x1)
                x2=int(x2)



                width = x2-x1



                center_x = int(
                    (x1+x2)/2
                )



                best = {


                    "colour": colour,

                    "confidence": confidence,

                    "x": center_x,

                    "width": width

                }



        if best:



            self.last_detection = best



            print(

                "Detected:",

                best["colour"],

                "confidence:",

                round(
                    best["confidence"],
                    3
                ),

                "X:",

                best["x"],

                "width:",

                best["width"]

            )



            return best



        return None





    # ==================================================
    # CHECK PICKUP
    # ==================================================


    def bottle_ready(self):


        if self.last_detection is None:

            return False



        x = self.last_detection["x"]

        width = self.last_detection["width"]



        if width < MIN_BOTTLE_WIDTH:

            return False



        if abs(

            x - CAMERA_WIDTH/2

        ) > CENTER_TOLERANCE:


            return False



        return True





    def clear_detection(self):


        self.last_detection = None