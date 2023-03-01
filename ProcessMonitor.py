import psutil

def DisplayProcess():

    iCount = 0
    ListProcess = []

    for process in psutil.process_iter():
        Pinfo = process.as_dict(attrs=['pid','username','status','name',])
        iCount+=1
        ListProcess.append(Pinfo)
    print("Ruuning process count : ",iCount)    
    return ListProcess    

def main():

    print("_------------------WELCOME TO PROCESS MONITOR-----------------------_")
    print(" ")

    ProcessList = DisplayProcess()

    for elem in ProcessList:
        print(elem)

if __name__=="__main__":
    main()    