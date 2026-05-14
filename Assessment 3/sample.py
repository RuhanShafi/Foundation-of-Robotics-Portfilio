import math
import roboticstoolbox as rtb # load the robotics toolbox

# the robot model can be defined using the the robotics toolbox
# The DHRobot object stores the joint information for the robot
# RevoluteDH objects can be used to represent each revolute joint in the robot model
# DH parameters are used to define the robot joint relationships
robot_2dof = rtb.DHRobot(
    [
        # the RevoluteDH class represents a revolute joint using DH parameters
        # this is a list of 2 joints representing 2 degrees of freedom (DOF)
        rtb.RevoluteDH(
            d = 0,
            alpha = 0,
            a = 1, # note that the dimensions are in m instead of mm
            # offset = math.radians(0)
        ),
        rtb.RevoluteDH(
            d = 0,
            alpha = 0,
            a = 1,
            # offset = math.radians(0)
        )
    ],
    name = "Two-Link Manipulator"
)

# this will print the robot model details
print(robot_2dof)

# this will plot the robot model graphically
q = [math.radians(40), math.radians(10)]
#robot_2dof.plot(q, limits=[-2.0, 2.0, -2.0, 2.0, 0.0, 0.5])

'''
Find the end effector pose given the measured joint angles
'''

# create an array of joint angles
# for example:
#
# joint_angles = np.array([0,0,0,0,0,0])

# plot the robot model
robot_2dof.plot(q, limits=[-2.0, 2.0, -2.0, 2.0, 0.0, 0.5])

# get the end effector pose
pose_2 = robot_2dof.fkine(q)

# print the end effector pose
print(pose_2.t)
