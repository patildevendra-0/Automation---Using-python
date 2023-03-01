import os

def Read_File(FileName):

    if(os.path.exists(FileName)):
        fd = open(FileName,"r")
        Data = fd.read()
        print("Data of File______________")
        print(Data)

        fd.close()

    else:
        print("File is not existing")
        return    

def main():

    print("Enter the file Name: ")
    Name = input()

    Read_File(Name)

if __name__=="__main__":
    main()    