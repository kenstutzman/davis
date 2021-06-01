#!/usr/bin/env python3
# pip install pyvantagepro

from pyvantagepro import VantagePro2

print("pyvantagepro")
device = VantagePro2.from_url('tcp:64.93.117.26:22222')
print("connected to device!")
#print(device.gettime())
#print("done with gettime()")
data = device.get_current_data()
#print(data)
print("Datetime,TempIn,HumIn,TempOut,HumOut,BarTrend,Barometer,RainDay,RainYear,WindSpeed,WindSpeed10Min,WindDir")
print(data['Datetime'],data['TempIn'],data['HumIn'],data['TempOut'],data['HumOut'],data['BarTrend'],data['Barometer'],data['RainDay'],data['RainYear'],data['WindSpeed'],data['WindSpeed10Min'],data['WindDir'])
#Datetime,BarTrend,Barometer,TempIn,HumIn,TempOut,WindSpeed,WindSpeed10Min,WindDir,HumOut,RainRate,UV,SolarRad,RainStorm,StormStartDate,RainDay,RainMonth,RainYear,ETDay,ETMonth,ETYear,BatteryStatus,BatteryVolts,ForecastIcon,ForecastRuleNo,SunRise,SunSet
