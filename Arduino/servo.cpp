#include<ros.h>
#include<std_msgs/strings.h>
ros::NodeHandle nh;
servo servo;
void servo_callback(const std_msgs::UInt16&angle_msg)
{
  servo.write(angle_msg.data);
}
ros::Subscriber<std_msgs::UInt16>servo_sub("servo_control",&servo_callback);
void setup()
{
  servo.attach(9);
  nh.initNode();
  nh.Subscriber(servo_sub);
  servo.write(20);
}
void loop()
{
nh.spinOnce();
  delay(10);
}

