#!/usr/bin/env python3
#----------------------------------------------------------------
#Note:
#ds18b20's data pin must be connected to pin7.
#replace the 28-XXXXXXXXX as yours.
#https://medium.com/@ramcesc/machine-learning-simple-linear-regression-with-python-cbc050dd0fbe
#----------------------------------------------------------------
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import array as arr
from scipy import stats
from sklearn.metrics import r2_score

ds18b20 = ''

currentTemp= np.array([])
time = np.array([])

#slope, intercept, r, p, std_err = stats.linregress(time, currentTemp)


#=====Linear Regression====
def lincalc(time):
    return slope * time + intercept

#=====Find the temeprature sensor=====
def setup():
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = '28-030697943135' #Find the name of your temperature sensor by following the instructions on the README file

#=====Read the temperature sensor data from a file=====
def read():
#global ds18b20
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature
    

def loop():
    while True:
        if read() != None:
            #print ("Current temperature : %0.3f C" % read())
            #print ("Array time : ", time)
            #print ("Array temp : ", currentTemp)
            
            global currentTemp
            currentTemp = np.append(currentTemp,read())
            global time
            time = np.append(time, currentTemp.shape)
            print(currentTemp)
            
            if len(currentTemp)%5==0:
                
                #Calculate Linear Regression
                global slope, intercept, r, p, std_err
                slope, intercept, r, p, std_err = stats.linregress(time, currentTemp)
                linModel = list(map(lincalc, time))
                #Plot linear model
                plt.plot(time, linModel,label="Linear Model")
                #State relationship of linear model 
                print ("LINE R: ",r)
                print ("LINE PREDICT: ",lincalc(len(currentTemp)+1))

                #Calculate polynomial regression
                polyModel=np.poly1d(np.polyfit(time,currentTemp,4))
                myline=np.linspace(1,len(currentTemp)+1,100)
                #Plot polynomial model
                plt.plot(myline,polyModel(myline),label="Polynomial Model")
                #State relationship of polynomial model
                print("POLY R: ",r2_score(currentTemp, polyModel(time)))
                print("POLY PREDICT: ",polyModel(len(currentTemp)+1))
                
                #Plot the line predicted point
                plt.plot(len(currentTemp)+1,lincalc(len(currentTemp)+1),marker='o', markersize=6, color="green", label="Linear prediction")

                #Plot the poly predicted point
                plt.plot(len(currentTemp)+1,polyModel(len(currentTemp)+1),marker='o', markersize=6, color="red", label="Polynomial prediction")
                
                
                #Plot the graph
                plt.scatter(time, currentTemp)
                plt.xlabel('Time', fontsize=16)
                plt.ylabel('Temperature (°C)', fontsize=16)
                plt.legend(loc="upper left")
                plt.show()
                
def destroy():
    pass

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: #CTRL + C
        destroy()


