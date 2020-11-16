#!/usr/bin/env python
import sys, rospy

rospy.init_node('node_args')

for i in range(1,4):
    print sys.argv[i]

rospy.spin()
