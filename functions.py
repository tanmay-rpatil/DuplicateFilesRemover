def subdir_check(prim, sec):
    print("HI")
    if (len(prim)>len(sec)):
        if (prim.find(sec)==-1):
            print("Scanning...")
        else:
            print(prim+" is a sub-directory of "+sec)
            print("Invalid input. Please input folders/directories that are not sub-folders/directories of another ")
    elif(len(sec)>len(prim)):
        if (sec.find(prim)==-1):
            print("Scanning...")
        else:
            print(sec+" is a sub-directory of "+prim)
            print("Invalid input. Please input folders/directories that are not sub-folders/directories of another ")
    elif(prim==sec):
        print("Entered the same folder/directory. Please imput diffrent ones.")

