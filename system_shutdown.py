"""
Created By: Ubaidullah Effendi-Emjedi

Icon By: "https://icons8.com"
"""
import os
import datetime

ONE_MINUTE = 60
HOUR_IN_SECONDS = 3600


def shutdown(seconds: int = 0):
    """
    Shutdown Computer
    :param hours:
    :return:
    """
    
    
    if seconds <= 1:
        #os.system(f"shutdown /s /t {ONE_MINUTE}")
        h2 = int(seconds/3600)  
        min2 = int((seconds-(h2*3600))/60) 
        sec2 = seconds-((h2*3600)+(min2)*60)
        #above steps used to basically convert back to original format
        format1 = "{}h:{}m:{}s".format(h2,min2,sec2)
        print(format1+ "Before Shutdown!!!\n")
    else:
        #time_in_seconds = int(hours * HOUR_IN_SECONDS)
        #os.system(f"shutdown /s /t {time_in_seconds}")
        h2 = int(seconds/3600)
        min2 = int((seconds-(h2*3600))/60) 
        sec2 = seconds-((h2*3600)+(min2)*60)
        format1 = "{}h:{}m:{}s".format(h2,min2,sec2)
        print(format1+ " Shutdown Scheduled!\n")


def abort_shutdown():
    """
    Abort Shutdown
    :return:
    """
    #os.system("shutdown /a")
    print("Operation Aborted!\n")


def runtime():
    print("""
    You are required to enter a number of hours. 
    For example, inputting 1.5 hours is equivalent to 1 and a half hours.
    To get minutes you can use fractions.
    For example, inputting 0.5 hours is equivalent to half an hour. Exactly 30minutes.
    If you input 0 hours, the PC will Shutdown in 60 seconds!
    If you enter -1 hours, a Previous Shutdown Schedule will be aborted and/or the program will end!
        """)
    try:
        hours = input("Enter a number of hours: ")
        seconds = hours.split(":")
        hour1 = int(seconds[0]) *3600 #converts value of index 0[hours] to seconds
        min1 = int(seconds[1]) *60  #converts value of index 1[minutes] to seconds
        sec1 = int(seconds[2])  #finds the difference of the total seconds
        total = hour1 +min1 +sec1 # adds total seconds
        if total>= 0:
            shutdown(total)
        else:
            abort_shutdown()
    except ValueError as error:
        print(error)
        print("Try Again!")
        runtime()

   # os.system("pause")


if __name__ == "__main__":
    runtime()
