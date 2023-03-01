import psutil

def DisplayProcess():

    ProcessList=[]
    for process in psutil.process_iter():
        Pinfo = process.as_dict(attrs=['username','name','pid','status'])
        Pinfo['vms'] = process.memory_info().vms/1024*1024
        ProcessList.append(Pinfo)
           
    return ProcessList

def main():

    Process = DisplayProcess()

    for proc in Process:
        print(proc)


if __name__=="__main__":
    main()    