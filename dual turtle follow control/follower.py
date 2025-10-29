#!/usr/bin/env python3
Import rose pie
from geometry_msgs.msg import Twist
from turtlesim.msg import pose
import math
class TurtleFollower:
  def __init__(self):
    rsopy.init_node('turtle_follower',anonymous = Ture)
    rospy.Subscriber('/turtle1/pose',pose,self.pose_callback)
    self.pub=rospy.publisher('/turtle2/cmd_vel',Twist,queue_size =10)
    self.turtle1_pose = none
    self.rate = rospy.rate(10)
    def pose_callback(self,data):
      self.turtle1_pose = data
    def follow(self):
      while not rospy.is_shutdown():
        if self.turtle_pose is none:
          self.rate.sleep()
          continue
        try :
          turtle2_pose = rospy.wait_for_message('/turtle2/pose',pose,timeout=1.0)
        except rospy. RosException:
          self.rate.sleep()
          continue
        distance =math.sqrt((self.turtle1_posex-turtle2_pose.x)**2 +(self.turtle1_pose.Y-turtle2_pose.Y)**2)
        angle_to_turtle1 =math.atan2(self.turtle1_pose.Y-turtle2_pose.Y,self.turtle1_pose.x-turle2_pose.x)
        twist = Twist()
        kp_linear =1.5
        kp_angular = 6.0
        twist.linear.x =kp_linear*distance
        angle_diff= angle_to_turtle-turtle2_pose.theta
        while angle_diff >math.pi:
          angle_diff -= 2*math.pi
        while angle_diff <-math.pi:
          angle_diff += 2* math.pi
        twist.angular.z =kp_angular * angle_diff
        if distance <0.5:
          twist.linear.x=0
          twist.angular.z=0
        self.pub.publish(twist)
        self.rate.sleep()
if __name__ == "__main__":
  try:
    follower = TurtleFollower()
    follower.follow()
except rospy.RosInterruptException:
  pass
