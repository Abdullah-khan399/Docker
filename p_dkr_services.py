def services():
    import os
    import p_docker_menu
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
\t \*\       _____________________________________       /*/
\t  \*\     /*/                                 \*\     /*/
\t   \*\    \*\ WELCOME TO DOCKER SERVICES TUI  /*/    /*/
\t    \*\    -------------------------------------    /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput setaf 1")
        os.system("tput rmul")
        print('''
Press 1 : For Docker Installation
Press 2 : To start Docker services
Press 3 : To stop Docker services
Press 4 : To restart Docker services
Press 5 : To show Docker version
Press 6 : To show Docker information
Press 7 : To show Docker status
Press 8 : To Login in docker hub
Press 9 : To GO BACK to Main Menu
Press 10 : To EXIT \n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")

        if ( x == 1 ):
            os.system("yum install docker-ce")
            os.system("tput setaf 1")
        elif ( x == 2 ):
            os.system("systemctl start docker")
            os.system("tput setaf 1")
        elif ( x == 3 ):
            os.system("systemctl stop docker")
            os.system("tput setaf 1")
        elif ( x == 4 ):
            os.system("systemctl restart docker")
            os.system("tput setaf 1")
        elif ( x == 5 ):
            os.system("docker version")
            os.system("tput setaf 1")
        elif ( x == 6 ):
            os.system("docker info")
            os.system("tput setaf 1")
        elif ( x == 7 ):
            os.system("systemctl status docker")
            os.system("tput setaf 1")
        elif ( x == 8 ):
            os.system("docker login")
            os.system("tput setaf 1")
        elif ( x == 9 ):
            p_docker_menu.docker()
            os.system("tput setaf 1")
        elif ( x == 10 ):
            exit()
y=input("\n\nEnter to continue.......")

