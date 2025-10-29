#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, select,termios,tty
key to velocity mapping 
key_bindings ={
    'w':(1.0,0.0) #forward
    's':(-1.0,0.0), #backward
    'a':(0.0,1.0), # left
    'd':(0.0,-1.0) #right
}
def getkey():
  tty.setraw(sys.stdin.fileno())
  rlist,_,_ = select.select([system],[],[],0.1)
  if rlist:
    key = sys.stdin.read(1)
  else :
    key =' '
    termois.tcsetattr(sys.stdin,termios.TCSADRAIN,settings)
    return key
if __name__ = "__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('turtle_custom_teleop')
    pub = rospy.Publisher('/turtle/cmd-vel',Twist,queue_size=1)
    speed = 2.0
    turn = 2.0
    try :
        print("use WASD Keys to move the turtle.Press crtl +c to quit.")
        while not rospy.is shutdown():
            key =getkey()
            twist = Twist()
            if key in key-bindings:
                linear, angular = key-bindings[key]
                twist.linear.x =linear*speed
                twsit.angular.z = angular*turn
                pub.publish(twist)
            elif key =='\x03':#ctrl+c to quit
                break
            else:
                twist.linear.x = 0
                twist.angular.z =0
                pub.publish(twist)
    except rospy.RosInterruptException:
        pass
    finally:
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin,termios.TCSADRAIN,settings)
