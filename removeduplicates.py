from sys import *
import os
import hashlib
import time


def DeleteFiles(dict1):
    results = list(filter(lambda X:len(X)>1,dict1.values()))

    icnt = 0

    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt = 0        
    else:
        print("No duplicates file found")                

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while(len(buf)>0):
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalide path")

def printResults(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values())) 

    if len(results)>0:
        print("Duplicate found")
        print("following file are duplicates")

        for result in results:
            for subresult in result:
                print('t\t\%s'%subresult)  

    else:
        print("No duplicates file found")

def main():

    print("WELCOME TO DUPLICATES FILE REMOVAL")
    print(" ")

    print("Application Name: "+argv[0])

    if(len(argv)!=2):
        print("ERROR: Invalide number of arguments")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("USAGE: Application_name Absolute_path Extension")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("HELP: This scriptt is used to traverse specific directory and delete duplicates file")  
        exit()  

    try:
        arr = {}
        StartTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        EndTime = time.time()

        print("Took %s secounds to evalute"%(EndTime-StartTime))

    except Exception as E:
        print("ERROR: Invalide Input",E)       

if __name__=="__main__":
    main()
