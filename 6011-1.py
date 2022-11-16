from datetime import datetime, timedelta
import math


print("Arrival Time Estimator")
# function to calculate the time of travel
def dept_time(distance,speed):
    hours = math.floor(distance/speed)
    minutes = math.ceil((distance/speed - hours)*60)
    return hours,minutes

def calculate(date, time, distance, speed):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:0])
    minutes = int(time[3:5])
    hour = int(time[0:2])
    am_pm = time[-2:0]
    travelhours,travelminutes = dept_time(distance,speed)
    if am_pm =="PM":
        hour = hour+12
# finding the current date and time
    currentdate = datetime(year,month,day,hour,minutes)
    arrivaldate = currentdate + timedelta(hours=travelhours,minutes=travelminutes)
    timestamp = "AM"
# finding the arrival time
    arrival_hour = arrivaldate.hour
    if arrivaldate.hour >12:
        arrival_hour = arrivaldate.hour - 12
    timestamp = "PM"
# printing the required result
    print("\nEstimated Travel Time ")
    print("Hours:",travelhours)
    print("Minutes:",travelminutes)
    print("Estimated date of arrival: {}-{}-{}".format(arrivaldate.year,arrivaldate.month,arrivaldate.day))
    print("Estimated time of arrival: {}:{} {}".format(arrival_hour,arrivaldate.minute,timestamp))

while True:

    date = (input("Enter date of departure(YYYY-MM-DD): "))
    time = (input("Enter time of departure(HH:MM AM/PM): "))
    distance = int(input("Enter miles : "))
    speed = float(input("Enter miles per hour: "))
    calculate(date, time, distance, speed)
# asking whether user wants to continue
    string = input("Continue? (y/n): ")
    if string.lower() == "n":
            break