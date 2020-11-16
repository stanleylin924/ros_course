#!/usr/bin/env python
import rospy, unittest, rostest, time

class MyTest(unittest.TestCase):

    def test_a(self):
        self.assertTrue(True)

    def test_b(self):
        self.assertTrue(True)

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('test_tag')
    rostest.rosrun('roslaunch_demo', 'mytest', MyTest)

