#!/usr/bin/env python
import sys, rospy

rospy.init_node('node_output')

while True:
    rospy.loginfo("loginfo: hello world!")
    rospy.logerr("logerr: hello world!")
    rospy.sleep(2)

rospy.spin()
