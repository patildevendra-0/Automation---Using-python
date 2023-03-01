
import time
import schedule
import datetime

def Reminder():
    print(" This is Reminder.....")

def Wake_Up():
    print("Good Morning wake up...its time to learn new things")    

def Bed_Time():
    print("Good night ....go ton bed early..")

def Work():
    print("Study and work hard")    

def main():

    print(":::::::::::::::::::::::Welcome to Reminder:::::::::::::::::::::")
    print(" ")

    schedule.every(10).seconds.do(Reminder)
    schedule.every().day.at("20:00").do(Bed_Time)
    schedule.every().day.at("06:00").do(Wake_Up)
    schedule.every(5).to(10).minutes.do(Work)
    schedule.every().monday.at("12:00").do(Work)


    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
    