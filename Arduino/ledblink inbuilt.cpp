#include<ros.h>
#include<std_msgs/strings.h>
ros::NodeHandle nh;
void message ch(const std_msgs::Empty&toggle_msg)
{
digitalWrite(LED_BuiltIn,High);
delay(3000);
digitalWrite(LED_BuiltIn,Low);
delay(3000);
}
ros::Subscriber<std_msgs::Empty>sub("Led_blink",&messagecb);
void setup()
{
  PinMode(LED_BuiltIn,output);
  nh.initNode();
  nh.Subscriber(sub);
}
void loop()
{
nh.spinOnce();
}

