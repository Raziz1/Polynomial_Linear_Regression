# Polynomial_Linear_Regression 📊🌡
Predicting temperature values using a Raspberry PI, digital temperature sensor, and regression models

## Parts 🛠
* [Raspberry Pi 4 Model B](https://www.amazon.ca/LABISTS-Raspberry-Complete-Starter-Upgraded/dp/B084DQZP7P/ref=sr_1_7?crid=10KKB0KBUW5SG&dchild=1&keywords=raspberry+pi+4&qid=1609429444&sprefix=raspberry+%2Caps%2C199&sr=8-7)
* [DS18B20 Digital Temperature Sensor(SunFounder Kit V2.0)](https://www.amazon.ca/SunFounder-Modules-Sensor-Raspberry-Extension/dp/B014PF05ZA/ref=sr_1_8?dchild=1&keywords=sunfounder+starter+kit+v2.0&qid=1609429513&sr=8-8)

## Libraries  📚
* [NumPy](https://pypi.org/project/numpy/)
* [MatPlotLib](https://pypi.org/project/matplotlib/)
* [Scipy](https://pypi.org/project/scipy/)
* [Sklearn](https://pypi.org/project/scikit-learn/)

## Overview 
<p> 
  <img width=45% height=45% align='Right' src="https://github.com/Raziz1/Polynomial_Linear_Regression/blob/main/images/Figure_1.png? raw=true">
</p>

* The following code plots both linear and polynomial regression models and prints the appropriate prediction for the next temperature interval. It also prints the relationship value for the both models. 
* I have not used the Train/Test model method but there are some great resources to if you wante. 
    * [W3Schools Python ML Train/test](https://www.w3schools.com/python/python_ml_train_test.asp) 
    * [Machine Learning — Simple Linear Regression with Python](https://medium.com/@ramcesc/machine-learning-simple-linear-regression-with-python-cbc050dd0fbe)
* You can also edit the script to take temperature intervals throughout the day for more accurate readings.
* Keep in mind that the predictions and models may not show accurate relationships or predictions because your data might not show strong linear or polynomial correlations

## Schematics ⚡
<p> 
  <img align='Center' src="https://github.com/Raziz1/Polynomial_Linear_Regression/blob/main/images/schematics.png? raw=true">
</p>

|**Raspberry Pi**|**GPIO Extension Board**|**DS18B20 Temperature Sensor**|
| -------------   |:-------------:  |:-------------:|
| GPIO7           | GPIO4           | SIG            | 
| 3.3V            | 3.3V            |VCC          |  
| GND              | GND           |GND          |  

## DS18B20 Temperature Sensor Setup
1. Upgrade your kernel `sudo apt-get update sudo apt-get upgrade`
2. Edit the config file to setup the single wire communication bus `sudo nano /boot/config.txt`
3. Scroll down and type `dtoverlay=w1-gpio`
    * This enables the one-wire interface for the default GPIO4 pin
4. Reboot the Raspberry Pi `sudo reboot`
5. Mount the device drivers and confirm whether the device is working or not 
`sudo modprobe w1-gpio` 
`sudo modprobe w1-therm`
`cd /sys/bus/w1/devices/` 
`ls`
    * The result should be similar: `28-00000495db35 w1_bus_master1` This is the name of your temperature sensor. Keep it for the python script
6.  Check the temperature `cd 28-00000495db35` `ls`
    * The result should be: `driver   id    name    power   subsystem   uevent    w1slave   cat w1_slave`
7. Type in the following: `cat w1_slave`
    * The result should be similar: `a3 01 4b 46 7f ff 0d 10 ce: crc=ce YES` `a3 01 4b 46 7f ff 0d 10 ce t=26187` The second line is the current temperature value 
    
