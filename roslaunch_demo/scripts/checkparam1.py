#!/usr/bin/env python
import rospy

rospy.init_node('checkparam1')
print rospy.get_param('myparam')
rospy.spin()

