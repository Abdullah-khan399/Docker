def containers():
    import os
    
    x = 0
    while x != 10 :
        os.system("clear")
        os.system("tput setaf 1")
        os.system("tput bold")
        print('''
\t######     ########  ########  ##   ##  ########  ########
\t##   ###   ##    ##  ##        ##  ##   ##        ##    ##
\t##    ###  ##    ##  ##        ## ##    ##        ##    ##
\t##    ###  ##    ##  ##        ####     #####     ########
\t##    ###  ##    ##  ##        ## ##    ##        ##  ##  
\t##   ###   ##    ##  ##        ##  ##   ##        ##   ## 
\t######     ########  ########  ##   ##  ########  ##    ##
\t___________________________________________________________
\t___________________________________________________________
\t\*\                                                     /*/
\t \*\      _______________________________________      /*/
\t  \*\    /*/                                   \*\    /*/
\t   \*\   \*\  WELCOME TO DOCKER CONTAINER TUI  /*/   /*/
\t    \*\   ---------------------------------------   /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput setaf 1")
        os.system("tput rmul")
        print('''
Press 1 : To create a container
Press 2 : To show the list of all containers
Press 3 : To show the list of active containers
Press 4 : To start a container
Press 5 : To run a container
Press 6 : To stop a container
Press 7 : To execute a command in a container
Press 8 : To remove a container
Press 9 : To GO BACK to Main Menu
Press 10 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")

        if ( x == 1 ):
            import os
            name=input("enter the name of image : ")
            os.system("docker run -itd {}".format(name))
            print("Container created successfully")
        elif ( x == 2 ):
            print("List of docker containers..... \n")
            os.system("docker ps -a")
        elif ( x == 3 ):
            print("List of active docker containers..... \n")
            os.system("docker ps")
        elif ( x == 4 ):
            name=input("enter the name of container : ")
            os.system("docker start {}".format(name))
            print("Container started successfully")
        elif ( x == 5 ):
            name=input("enter the name of container : ")
            os.system("docker attach {}".format(name))
        elif ( x == 6 ):
            name=input("enter the name of container : ")
            os.system("docker stop {}".format(name))
            print("Container stopped successfully")
        elif ( x == 7 ):
            name=input("enter the name of container : ")
            cmd=input("enter the command : ")
            os.system("docker exec -it {} {}".format(name,cmd))
        elif ( x == 8 ):
            name=input("enter the name of container : ")
            os.system("docker rm -f {}".format(name))
            print("Container removed successfully")
        elif ( x == 9 ):
            import p_docker_menu
            p_docker_menu.docker()
        elif ( x == 10 ):
            exit()
        os.system("tput setaf 1")
y=input("\n\nEnter to continue.......")
containers()
