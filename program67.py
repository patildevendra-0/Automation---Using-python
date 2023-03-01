import os

def Write_File(FileName):

    if (os.path.exists(FileName)):
        print("File is present pls enter the data")
        Data = input()

        fd = open(FileName,"a")
        fd.write(Data)

    else:
        print("file is not exists")    

def main():

    print("Enter the file name: ")
    Name = input()

    Write_File(Name)

if __name__=="__main__":
    main()    