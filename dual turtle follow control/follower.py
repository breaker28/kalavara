#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleFollower:
    def __init__(self):
        rospy.init_node('turtle_follower', anonymous=True)

        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

        self.turtle1_pose = None
        self.rate = rospy.Rate(10)

    def pose_callback(self, data):
        self.turtle1_pose = data

    def follow(self):
        while not rospy.is_shutdown():
            if self.turtle1_pose is None:
                self.rate.sleep()
                continue

            try:
                turtle2_pose = rospy.wait_for_message('/turtle2/pose', Pose, timeout=1.0)
            except rospy.ROSException:
                self.rate.sleep()
                continue

            # Distance between turtle1 and turtle2
            distance = math.sqrt((self.turtle1_pose.x - turtle2_pose.x) ** 2 +
                                 (self.turtle1_pose.y - turtle2_pose.y) ** 2)

            # Angle to face turtle1
            angle_to_turtle1 = math.atan2(self.turtle1_pose.y - turtle2_pose.y,
                                          self.turtle1_pose.x - turtle2_pose.x)

            twist = Twist()
            kp_linear = 1.5
            kp_angular = 6.0

            twist.linear.x = kp_linear * distance

            angle_diff = angle_to_turtle1 - turtle2_pose.theta

            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi

            twist.angular.z = kp_angular * angle_diff

            # Stop if too close
            if distance < 0.5:
                twist.linear.x = 0
                twist.angular.z = 0

            self.pub.publish(twist)
            self.rate.sleep()


if __name__ == "__main__":
    try:
        follower = TurtleFollower()
        follower.follow()
    except rospy.ROSInterruptException:
        pass
