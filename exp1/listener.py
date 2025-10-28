#!/usr/bin/env Python3
#license removed for brevity
import rospy
from std_msgs.msg import String
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s",data.data)
def listener():
        rospy.init_node('listener',anonymous=True)
        rospy.subscriber('chatter,String,callbback)
        rospy.spin()
if__name__=='__main__':
    listener()
