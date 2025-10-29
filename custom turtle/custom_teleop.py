#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# key to velocity mapping
key_bindings = {
    'w': (1.0, 0.0),   # forward
    's': (-1.0, 0.0),  # backward
    'a': (0.0, 1.0),   # turn left
    'd': (0.0, -1.0)   # turn right
}

def getkey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtle_custom_teleop')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)  # <-- Correct topic

    speed = 2.0
    turn = 2.0

    try:
        print("Use WASD keys to move the turtle. Press CTRL+C to quit.")
        while not rospy.is_shutdown():
            key = getkey()
            twist = Twist()

            if key in key_bindings:
                linear, angular = key_bindings[key]
                twist.linear.x = linear * speed
                twist.angular.z = angular * turn
                pub.publish(twist)

            elif key == '\x03':  # CTRL+C to exit cleanly
                break

            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0
                pub.publish(twist)

    except rospy.ROSInterruptException:
        pass

    finally:
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
