import os

def DeleteFile(FileName):

    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        print("Size of File: ",size)

        if(size==0):
            os.remove(FileName)
        else:
            print("You are really want to delete file Y/N:") 
            Option = input()

            if(Option=="Y"or Option =="y"):
                os.remove(FileName)
                print("File is delete")
            else:
                print("File deletetation process cancel")       


    else:
        print("File not exists")
        return  


def main():

    print("Enter the file name: ")
    Name = input()

    DeleteFile(Name)

if __name__=="__main__":
    main()    