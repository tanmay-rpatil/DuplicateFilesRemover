def subdir_check(prim, sec):
    if (len(prim)>len(sec)):
        if (prim.find(sec)==-1):
            print("Scanning...")
            return False
        else:
            print(prim+" is a sub-directory of "+sec)
            print("Invalid input. Please input folders/directories that are not sub-folders/directories of another ")
            return True
    elif(len(sec)>len(prim)):
        if (sec.find(prim)==-1):
            print("Scanning...")
            return False
        else:
            print(sec+" is a sub-directory of "+prim)
            print("Invalid input. Please input folders/directories that are not sub-folders/directories of another ")
            return True
    elif(prim==sec):
        print("Entered the same folder/directory. Please imput diffrent ones.")
        return True
    else:
        print("Scanning...")
        return False

