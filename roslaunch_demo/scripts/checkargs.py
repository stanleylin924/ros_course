#!/usr/bin/env python
import sys, rospy

rospy.init_node('checkargs')
print sys.argv[1] + ",",
print sys.argv[2] + "!"

rospy.spin()

