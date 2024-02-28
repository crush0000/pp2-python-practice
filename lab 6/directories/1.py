import os, string

def test1():
    print("Directories: \t", [dirc for dirc in os.listdir(path) if os.path.isdir(os.path.join(path, dirc))])
    print("Files: \t\t", [dirc for dirc in os.listdir(path) if not os.path.isdir(os.path.join(path, dirc))])
    print("All together: \t", [dirc for dirc in os.listdir(path)])
test1()



def test2():
    print("File Exists: \t", os.access(path, os.F_OK))
    print("For Read: \t", os.access(path, os.R_OK))
    print("For Writing: \t", os.access(path, os.W_OK))
    print("Executable: \t", os.access(path, os.X_OK))


def test3():
    print("Path exists: \t\t", os.path.exists(path))
    print("Filename: \t\t", os.path.basename(path))



def test4():
    with open("Sample.txt", "r") as f:
        print("The number of lines: ", len(f.readlines()))

def test5():
    list = ["fsdf","fdsfdsafsad",'fsdfdsaf',"fdsgdfs"]
    with open("Sample.txt", "a") as f:
        for i in list:
            f.write(f"\n {i}")


def test6():
    os.chdir("Letters")
    for i in string.ascii_letters:
        with open(i + ".txt", "w") as f:
            f.writelines(i)



def test7():
    with open(input("enter filepath to copy from\n"), "r") as f:
        text = f.read()
    with open(input("filepath to copy to\n"), "a") as s:
        s.write(text)


def test8():
    delpath = input("Enter filepath to delete\n")
    if not os.path.exists(delpath): print("Filepath does not exists"); return
    os.remove(delpath)



path = "Aldiyar"