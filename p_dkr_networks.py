def networks():
    import os
    import p_docker_menu
    x = 0
    while x != 7 :
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
\t   \*\    \*\      WELCOME TO DOCKER TUI      /*/    /*/
\t    \*\    -------------------------------------    /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput setaf 1")
        os.system("tput rmul")
        print('''
Press 1 : To create a Network
Press 2 : To show the list of all Network
Press 3 : To inspect a Network
Press 4 : To remove a Network
Press 5 : To show IP routing table
Press 6 : To GO BACK to Main Menu
Press 7 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")
        if ( x == 1 ):
            name=input("Enter the name of Network : ")
            os.system("docker network create {}".format(name))
            print("Network created successfully")
        elif ( x == 2 ):
            print("List of docker Networks..... \n")
            os.system("docker network ls")
        elif ( x == 3 ):
            name=input("Enter the name of Network : ")
            os.system("docker network inspect {}".format(name))
        elif ( x == 4 ):
            name=input("Enter the name of Network : ")
            os.system("docker network rm -f {}".format(name))
            print("Network removed successfully")
        elif ( x == 5 ):
            os.system("route -n")
        elif ( x == 6 ):
            p_docker_menu.docker()
        elif ( x == 7 ):
            exit()
        
networks()
