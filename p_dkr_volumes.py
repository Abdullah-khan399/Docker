def volumes():
    import os
    import p_docker_menu
    x = 0
    while x != 6 :
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
\t \*\       _____________________________________       /*/
\t  \*\     /*/                                 \*\     /*/
\t   \*\    \*\  WELCOME TO DOCKER VOLUMES TUI  /*/    /*/
\t    \*\    -------------------------------------    /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput setaf 1")
        os.system("tput rmul")
        print('''
Press 1 : To create a Volume
Press 2 : To show the list of all Volume
Press 3 : To inspect a Volume
Press 4 : To remove a Volume
Press 5 : To GO BACK to Main Menu
Press 6 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")

        if ( x == 1 ):
            name=input("Enter the name of Volume : ")
            os.system("docker volume create {}".format(name))
            print("Volume created successfully")
        elif ( x == 2 ):
            print("List of docker Volumes..... \n")
            os.system("docker volume ls")
        elif ( x == 3 ):
            name=input("Enter the name of Volume : ")
            os.system("docker volume inspect {}".format(name))
        elif ( x == 4 ):
            name=input("enter the name of Volume : ")
            os.system("docker volume rm {}".format(name))
        elif ( x == 5 ):
            p_docker_menu.docker()
        elif ( x == 6 ):
            exit()
        os.system("tput setaf 3")
y=input("\n\nEnter to continue.......")
