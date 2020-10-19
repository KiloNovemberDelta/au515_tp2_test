#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import cv2.aruco as aruco


class Robot:
    def __init__(self):
        self.bridge = CvBridge()
        self.speed = 0.0
        self.angle = 0.0
        self.sonar = 0 #Sonar distance

        '''Listener and publisher'''

        rospy.Subscriber("/raspicam_node/camera/image_raw", Image, self.callback)
        self.cmd_vel_pub = rospy.Publisher("/follower/cmd_vel", Twist, queue_size = 1)

        self.pub_velocity() #Run the publisher once

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

            # Our operations on the frame come here
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
            parameters = aruco.DetectorParameters_create()

            # lists of ids and the corners beloning to each id
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
            #print(corners)

            gray = aruco.drawDetectedMarkers(gray, corners)

            # print(rejectedImgPoints)
            # Display the resulting frame
            cv2.imshow('frame', gray)
            cv2.waitKey(3)

        except CvBridgeError as e:
            pass

        #cv2.imshow("Image window", cv_image)
        #cv2.waitKey(3)

    def set_speed_angle(self,speed,angle):
        self.speed = speed
        self.angle = angle
        self.pub_velocity()

    def pub_velocity(self):
        cmd_vel = Twist()
        cmd_vel.linear.x = self.speed
        cmd_vel.linear.y = 0.0
        cmd_vel.linear.z = 0.0

        cmd_vel.angular.x = 0.0
        cmd_vel.angular.y = 0.0
        cmd_vel.angular.z = self.angle

        self.cmd_vel_pub.publish(cmd_vel)

def run_demo():
    '''Main loop'''
    robot = Robot()
    while True:
        #Write here your strategy..

        velocity = 0
        angle = 0


        #Finishing by publishing the desired speed. DO NOT TOUCH.
        robot.set_speed_angle(velocity,angle)
        rospy.sleep(0.5)

if __name__ == "__main__":
    print("Running ROS..")
    rospy.init_node("Follower", anonymous = True)

    run_demo()
