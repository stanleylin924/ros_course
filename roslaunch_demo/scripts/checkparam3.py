#!/usr/bin/env python
import rospy

rospy.init_node('checkparam3')
print rospy.get_param('myparam1')
print rospy.get_param('myparam2')
rospy.spin()

