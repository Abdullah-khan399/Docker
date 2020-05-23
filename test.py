
def abd():
    import os
    x=0
    while x!=5:
        print('''
Press 1 : To create a container
Press 2 : To show the list of all containers
\n''')
        x = int(input("Enter your choices : "))
        if ( x == 1 ):
            import os
            name=input("enter the name of image : ")
            os.system("docker run -itd {}".format(name))
            print("Container created successfully")
        elif ( x == 2 ):
            print("List of docker Networks..... \n")
            os.system("docker network ls")
abd()
