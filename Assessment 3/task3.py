import math
import roboticstoolbox as rtb  # load the robotics toolbox

# the robot model can be defined using the the robotics toolbox
# The DHRobot object stores the joint information for the robot
# RevoluteDH objects can be used to represent each revolute joint in the robot model
# DH parameters are used to define the robot joint relationships
q = [
    math.radians(357.016),
    math.radians(21.016),
    math.radians(150.082),
    math.radians(271.999),
    math.radians(319.967),
    math.radians(272.969),
]

robot_2dof = rtb.DHRobot(
    [
        # the RevoluteDH class represents a revolute joint using DH parameters
        # this is a list of 2 joints representing 2 degrees of freedom (DOF)
        rtb.RevoluteDH(
            d=(128.3 + 115.0),
            alpha=(math.pi / 2),
            a=0,  # note that the dimensions are in m instead of mm
            offset=0,
        ),
        rtb.RevoluteDH(d=30.0, alpha=(math.pi), a=280, offset=(math.pi / 2)),
        rtb.RevoluteDH(
            d=20,
            alpha=(math.pi / 2),
            a=0,  # note that the dimensions are in m instead of mm
            offset=(math.pi / 2),
        ),
        rtb.RevoluteDH(
            d=(140.0 + 105.0), alpha=(math.pi / 2), a=0, offset=(math.pi / 2)
        ),
        rtb.RevoluteDH(
            d=(28.5 + 28.5),
            alpha=(math.pi / 2),
            a=0,  # note that the dimensions are in m instead of mm
            offset=math.pi,
        ),
        rtb.RevoluteDH(d=(105.0 + 130.0), alpha=0, a=0, offset=(math.pi / 2)),
    ],
    name="Six-link",
)

# this will print the robot model details
print(robot_2dof)

# this will plot the robot model graphically
# robot_2dof.plot(q, limits=[-2.0, 2.0, -2.0, 2.0, 0.0, 0.5])

"""
Find the end effector pose given the measured joint angles
"""

# create an array of joint angles
# for example:
#
# joint_angles = np.array([0,0,0,0,0,0])

# plot the robot model
robot_2dof.plot(q, limits=[-500, 500, -500, 500, -500, 500])

# get the end effector pose
pose_2 = robot_2dof.fkine(q)

# print the end effector pose
print(pose_2.t)
