# Vision-Based Autonomous Bottle Sorting System

An intelligent robotic bottle sorting system developed using **Webots**, **YOLOv8**, **Python**, and **Computer Vision**. The system detects bottles moving through a simulated warehouse environment, classifies them according to their colour, and uses a robotic manipulator to place them into the corresponding storage crates.

## Project Overview

This project demonstrates how artificial intelligence, computer vision, and robotic manipulation can be integrated to automate warehouse sorting operations.

Bottles are generated inside the Webots simulation and transported through the environment using a conveyor belt. A vision system detects and classifies each bottle into one of five colour categories. The robotic arm then performs an autonomous pick-and-place operation and transfers the bottle into the correct colour-coded crate.



## Main Features

* Real-time bottle detection using YOLOv8
* Five bottle colour categories
* Autonomous robotic pick-and-place operation
* Conveyor-based bottle transportation
* Random bottle generation
* Colour-specific sorting crates
* Integration of computer vision and Webots controllers
* Python-based modular controller architecture
* Simulated warehouse automation environment

## Bottle Classes

| Class ID | Bottle Class  |
| -------- | ------------- |
| 0        | Blue Bottle   |
| 1        | Green Bottle  |
| 2        | Pink Bottle   |
| 3        | Red Bottle    |
| 4        | Yellow Bottle |

## Dataset

The object detection dataset contains approximately 1,200 annotated images captured from the Webots simulation.

| Dataset Property          | Value |
| ------------------------- | ----- |
| Total images checked      | 1,201 |
| Corrupted images          | 0     |
| Duplicate images          | 0     |
| Total bounding boxes      | 4,603 |
| Average objects per image | 3.83  |
| Number of classes         | 5     |

### Class Distribution

| Bottle Class  | Bounding Boxes |
| ------------- | -------------- |
| Red bottle    | 995            |
| Green bottle  | 899            |
| Blue bottle   | 927            |
| Yellow bottle | 913            |
| Pink bottle   | 869            |

### Dataset Split

| Split      | Images |
| ---------- | ------ |
| Training   | 846    |
| Validation | 237    |
| Testing    | 118    |

## Model Training

The bottle detection model was trained using the YOLOv8s architecture.

### Main Training Parameters

| Parameter               | Value      |
| ----------------------- | ---------- |
| Model                   | YOLOv8s    |
| Epochs                  | 100        |
| Image size              | 640 × 640  |
| Batch size              | 16         |
| Optimizer               | AdamW      |
| Device                  | NVIDIA GPU |
| Early-stopping patience | 20         |

## System Workflow

```text
Bottle Generator
       ↓
Conveyor Belt
       ↓
Camera Captures Image
       ↓
YOLOv8 Detects Bottle
       ↓
Bottle Colour Is Identified
       ↓
Robot Calculates Sorting Action
       ↓
Gripper Picks the Bottle
       ↓
Robot Moves to the Matching Crate
       ↓
Bottle Is Released
```

## Technologies Used

* Webots R2025a
* Python
* YOLOv8
* Ultralytics
* OpenCV
* Computer Vision
* Deep Learning
* Robotic Manipulation
* Supervisor Controllers

## Project Structure

```text
webots-autonomous-bottle-sorting-system/
│
├── controllers/
│   ├── bottle_generator/
│   ├── robot_controller/
│   └── additional_controllers/
│
├── worlds/
│   └── bottle_sorting_world.wbt
│
├── protos/
│   └── Bottle.proto
│
├── models/
│   └── best.pt
│
├── assets/
│   ├── project_preview.png
│   └── bottle_sorting_demo.gif
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### 1. Install Webots

Download and install Webots R2025a or a compatible version.

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/webots-autonomous-bottle-sorting-system.git
```

### 3. Enter the Project Directory

```bash
cd webots-autonomous-bottle-sorting-system
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Open the Webots World

Open Webots and load:

```text
worlds/bottle_sorting_world.wbt
```

### 6. Run the Simulation

Press the Webots **Run** button to start the bottle generator, detection system, and robotic sorting process.

## How the System Works

### Bottle Generation

A Webots Supervisor controller creates bottles at scheduled intervals. Each generated bottle is randomly assigned one of the five supported colours.

### Object Detection

The camera captures images from the simulation. The trained YOLOv8 model processes the camera frames and returns the detected bottle class, confidence score, and bounding-box coordinates.

### Robotic Manipulation

After detecting the bottle, the robotic controller performs a predefined pick-and-place sequence. The robotic arm moves towards the bottle, closes the gripper, transports the bottle, and releases it into the appropriate crate.

### Sorting

Each detected class is mapped to a target crate:

```python
SORTING_TARGETS = {
    "blue_bottle": "blue_crate",
    "green_bottle": "green_crate",
    "pink_bottle": "pink_crate",
    "red_bottle": "red_crate",
    "yellow_bottle": "yellow_crate",
}
```

## Applications

* Warehouse automation
* Recycling facilities
* Manufacturing quality control
* Product classification
* Automated packaging systems
* Intelligent material handling

## Future Improvements

* Dynamic inverse kinematics
* Depth-camera-based distance estimation
* Tracking multiple bottles simultaneously
* Collision avoidance
* Sorting bottles according to shape and size
* Physical robot deployment
* Real-time performance monitoring dashboard

## Author

**Amal Joseph Chooreparambil Francis**

MSc Artificial Intelligence Technologies and Applications
MCAST – Malta College of Arts, Science and Technology

## License

This project is available for academic and educational purposes. See the `LICENSE` file for additional information.
