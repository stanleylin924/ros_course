#!/usr/bin/env python
import os, rospy

rospy.init_node('checkenv')
print os.environ['MY_ENV_TEST']
rospy.spin()

