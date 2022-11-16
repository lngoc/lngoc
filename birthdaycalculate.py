from calendar import month
from datetime import datetime

print("Welcome to Birthday Calculator")
while True:
        name = input('Enter your name:')
        birthday = input('Enter your birthday(MM/DD/YY)')
        list = []
        list = birthday.split('/')
        mm = int(list[0]);
        dd = int(list[1])
        yy = int(list[2])

        w = 19;
        if (yy<10):
                w = 200;
        elif(yy<=18):
                w = 20;
        yy = int(str(w)+str(yy))
        birthDate = datetime(yy,mm,dd)
        print("Birthday: ",birthDate.strftime("%A"),",",birthDate.strftime("%B"),",",birthDate.strftime("%d"),",",str(birthDate.year))
        tday = datetime.today()
        print("Today:",tday.strftime("%A"),",",tday.strftime("%B"),",",tday.strftime("%d"),",",str(tday.year))

        #calculate birthday
        years_old = tday.year - yy
        daysdiff = 0
        if(mm>tday.month):
                years_old = years_old - 1
                y = datetime(tday.year,mm,dd)
                age = y - tday
                daysdiff = age.days
        elif(mm==tday.month):
                if(dd>tday.day):
                        years_old = years_old - 1
                        daysdiff = dd-tday.day
                elif(dd<tday.day):
                        if(dd==tday.day-1):
                                daysdiff = -1
                        else:
                                y = datetime(tday.year+1,mm,dd)
                                age = y-tday
                                daysdiff = age.days
        else:
                y = datetime(tday.year+1,mm,dd)
                age = y-tday
                daysdiff = age.days

        if(years_old<2):
                print(name,"is",str(years_old*365+365-daysdiff),"days old")
        
        else:
                print(name,"is",str(years_old),"years old.")

        #calculate next birthday
        l = ""
        if(daysdiff==0):
                l = "is today"
        elif(daysdiff==1):
                l = " is tomorrow"
        elif(daysdiff==-1):
                l = " was yesterday"
        else:
                l = "is in "+" "+str(daysdiff)+"days."
        print(name,"'s birthday ",l,"\n")
        cnt = input("Continue yes/no?")
        if(cnt == 'no'):
                break





