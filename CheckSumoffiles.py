
from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while(len(buf)>0):
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag ==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)            

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(" ")
    else:
        print("Invalide path")            

def main():
    print("______WELCOME TO CHECKSUM OF FILE SCRIPT________")
    print(" ")
    print("Application Name: "+argv[0])

    if(len(argv)!=2):
        print("Invalide number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("HELP : this script is used to traverse specific directory and display checksum")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("USAGE: Application_Name Absolute_path")
        exit()

    try:
        arr = DisplayCheckSum(argv[1])

    except Exception as E:
        print("ERROR : Invalide input",E)              

if __name__=="__main__":
    main()    