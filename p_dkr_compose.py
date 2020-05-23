def compose():
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
\t   \*\    \*\  WELCOME TO DOCKER COMPOSE TUI  /*/    /*/
\t    \*\    -------------------------------------    /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput setaf 1")
        os.system("tput rmul")
        print('''
Press 1 : To open the compose file
Press 2 : To show the content of compose file
Press 3 : To run docker compose to start
Press 4 : To run docker compose to stop 
Press 5 : To GO BACK to Main Menu
Press 6 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")

        if ( x == 1 ):
            os.system("vim docker-compose.yml")
        elif ( x == 2 ):
            os.system("cat docker-compose.yml")
        elif ( x == 3 ):
            os.system("docker-compose up -d")
        elif ( x == 4 ):
            os.system("docker-compose stop")
        elif ( x == 5 ):
            p_docker_menu.docker()
        elif ( x == 6 ):
            exit()
        os.system("tput setaf 3")
y=input("\n\nEnter to continue.......")
