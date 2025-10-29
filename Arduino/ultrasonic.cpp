#include<ros.h>
#include<std_msgs/strings.h>
ros::NodeHandle nh;
std_msgs::float32 range_msg;
ros::Publisher range_pub("ultrasonic_range".&range_msg);
const int trigPin =2;
const int echopin =4;
void setup()
{
  nh.initNode();
  nh.advertise(range_pub);
  PinMode(trigPin,output);
  PinMode(echoPin,Input);
}
void loop()
{
  long duration;
  float distance;
  digitalWrite(trigPin,Low);
  delayMicroseconds(2);
  digitalWrite(trigPin,High);
  delayMicroseconds(10);
  digitalWrite(trigPin,low);
  duration = PulseIn(echoPin,High);
  distance =duration *0.034/2;
  range_msg.data=distance;
  range_pub.publish(&range_msg);
  nh.spinOnce();
  delay(100);
}

