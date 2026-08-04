# Foundations of Robotics — Student Portfolio

**Ruhan Shafi** · University of Canberra

This repository collects my lab reports and code for the *Foundations of Robotics* unit. Each assessment tackles a different layer of the robotics stack, moving from reactive control on a physical robot, through navigation and sensing theory, to the kinematics that describe how a manipulator's joints relate to its end-effector pose.

## Contents

### Assessment 1 — Sense-Think-Act Control on the Sphero RVR
A light-reactive control loop built with ROS 2 and `rclpy` for the Sphero RVR mobile robot. The robot subscribes to its ambient light sensor, compares the reading (in Lux) against a calibrated threshold, and publishes angular velocity commands over `/cmd_vel` to spin in place when triggered. Covers the ROS 2 topic/software stack, threshold calibration, algorithm design, and an analysis of the STA loop's performance.

 [`Assessment 1/report.tex`](./Assessment%201/report.tex) · [`report.pdf`](./Assessment%201/report.pdf)

### Assessment 2 — Localisation, Navigation & Path Planning
**Primary focus area:** Localisation, Navigation & Mapping

- **Task 1** — Localisation, mapping, and SLAM examples, plus an A* path-planning visualiser.
- **Task 2** — Line-following robot control: a basic two-sensor IR algorithm, then a PD controller driving a 5-channel sensor array, including tuning Kp and Kd.
- **Task 3** — Sensor probability.

📄 [`Assessment 2/report.tex`](./Assessment%202/report.tex) · [`report.pdf`](./Assessment%202/report.pdf)

### Assessment 3 — Manipulator Kinematics
- **Task 1** — Physical build and simulation of a manipulator.
- **Task 2** — Forward kinematics of a two-link manipulator, worked out manually and as pseudocode.
- **Task 3** — Forward kinematics implemented in Python with the [Robotics Toolbox](https://petercorke.github.io/robotics-toolbox-python/) using Denavit–Hartenberg (DH) parameters, including a 6-DOF robot model.

 [`Assessment 3/report.tex`](./Assessment%203/report.tex) · [`report.pdf`](./Assessment%203/report.pdf)
 [`task3.py`](./Assessment%203/task3.py) · [`six-link-noff.py`](./Assessment%203/six-link-noff.py) · [`sample.py`](./Assessment%203/sample.py)

## Repository structure

```
.
├── Assessment 1/   # Sense-Think-Act control (Sphero RVR, ROS 2)
├── Assessment 2/   # Localisation, navigation, mapping & line following
├── Assessment 3/   # Manipulator kinematics (DH parameters, forward kinematics)
└── README.md
```

Each assessment folder contains the LaTeX source (`report.tex`) and compiled PDF for the write-up, alongside any supporting code, diagrams, and figures used in that report.

## Tooling

- **ROS 2** / `rclpy` — robot control (Assessment 1)
- **Python** — control algorithms and kinematics (`roboticstoolbox-python`, Assessment 3)
- **LaTeX** — report typesetting
