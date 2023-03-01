import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is already exists...")
        return
    else:
        fd = open(FileName,"w")
        print("File is successfully created")
def main():

    print("Enter the file name: ")
    Name = input()

    CreateFile(Name)

if __name__=="__main__":
    main()