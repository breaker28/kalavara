#include<ros.h>
#include<std_msgs/strings.h>
ros::NodeHandle nh;
std_msgs::float32 flex_msg;
ros::Publisher flex_pub("flex_sensor_data",&flex_msg);
const int flex_pin =A0;
int flexvalue;
float bendAngle;

void setup()
{
  nh.initNode();
  nh.advertise(flex_pub);
  serial.begin(57600)
}
void loop()
{
  flexvalue = analogRead(flexpin);
  bendAngle = map(flexvalue,600,800,0,90);
  flex_msg.data = bendAngle;
  flex_pub.publish(&flex_msg);
  nh.spinOnce();
  delay(100);
  Serial.print("Raw Value: ");
  Serial.print("flexValue");
  Serial.print(" bendAngle: ");
  Serial.print("bendAngle");
}

