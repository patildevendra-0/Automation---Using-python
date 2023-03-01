
import schedule
import time
import datetime

def Current_time():
    print("Current time: ",time.time.now())

def Work():
    print("Courage + work = success. ...")

def Wake_Up():
    print("GOOD MORNING ..Every day is a new day. ...")

def Morning():
    print("Your thoughts become reality. Be positive!") 

def Bed_Time():
    print("GOOD NIGHT.... Follow your own path")   

def Motivation():
    print("Hard work matters. ...")       

def main():

    print("___________________________________WELCOME______________________________________________")
    print("")

    print("Current time: ",datetime.datetime.now())
    print("_________________________________________________________________________________________")
    print(" ")


    schedule.every(10).minutes.do(Motivation)
    schedule.every().day.at("05:45").do(Wake_Up)
    schedule.every().day.at("10:00").do(Morning)
    schedule.every().day.at("22:00").do(Bed_Time)
    schedule.every(5).to(10).minutes.do(Work)



    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()