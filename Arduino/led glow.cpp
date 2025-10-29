#include<ros.h>
#include<std_msgs/strings.h>
ros::NodeHandle nh;
int led_pin =7;
void message cb(const std_msgs::Bool&msg)
{
if(msg.data)
{
  digitalWrite(led_pin,High);
}else
{
  digitalwrite(led_pin,Low);
}
}
ros::Subscriber<std_msgs::Bool>sub("external-led",&messagecb);
void setup()
{
  PinMode(led_pin,output);
  nh.initNode();
  nh.Subscriber(sub);
}
void loop()
{
nh.spinOnce();
}

