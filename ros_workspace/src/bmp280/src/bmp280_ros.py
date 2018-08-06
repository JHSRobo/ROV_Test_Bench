#!/usr/bin/env python

from bmp280_driver import BMP280

import rospy
from bmp280.msg import bmp280_data

sensor = BMP280(0x77)

def publisher():
	pub = rospy.Publisher('rov/bmp280', bmp280_data, queue_size=3)
	rospy.init_node('bmp280')
	rate = rospy.Rate(3) #3Hz data read
	
	while not rospy.is_shutdown():
		msg = bmp280_data()

		sensor.updateValues()

		msg.tempC = sensor.getTempuratureC()
		msg.pressureP = sensor.getPressureP()
		msg.pressureA = sensor.getPressureA()
		msg.altitudeM = sensor.getAltitudeM()
		pub.publish(msg)

		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
