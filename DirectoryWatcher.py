
import os
from sys import*

def DirectoryWatcher(Path):

    Flag = os.path.isabs(Path)
    if(Flag==False):
        Path = os.path.abspath(Path)

    exists = os.path.isdir(Path)

    if(exists):
        for foldername,subfolder,filname in os.walk(Path):
            print("Current Directory : ",foldername)

            for subf in subfolder:
                print("sub folder of "+foldername+" is"+subf)

            for file in filname:
                print("File inside "+foldername+" is "+file)
            print(" ")
        else:
            print("invalide path")                    

def main():

    print("---------------------WELCOME TO DIRECTORY WATCHER-----------------------")
    print(" ")

    print("Application Name : "+argv[0])

    if(len(argv)!=2):
        print("Invalide argument..")
        exit()

    if (argv[1]=="-H")or(argv[0]=="-h"):
        print("HELP : ---")
        print("This appliaction is used to traverse specific directory or folder")

    if (argv[0]=="-U")or(argv[1]=="-u"):
        print("USAGE : ---")
        print("Application_name Absolute_Path_of_Directory")

    try:
        DirectoryWatcher(argv[1])

    except Exception:
        print("ERROR : Invalide input")                



if __name__=="__main__":
    main()    