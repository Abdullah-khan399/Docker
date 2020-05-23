def docker():
    import os
    x = 0
    while (x != 7) :
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
\t   \*\    \*\   WELCOME TO DOCKER TUI SHELL   /*/    /*/
\t    \*\    -------------------------------------    /*/
\t     \*\###########################################/*/
\n\n''')
        os.system("tput rmul")
        os.system("tput setaf 1")
        print('''
Press 1 : For Docker Services
Press 2 : For Docker Containers
Press 3 : For Docker Images
Press 4 : For Docker Networks
Press 5 : For Docker Volumes
Press 6 : For Docker Compose
Press 7 : To SWITCH BACK TO MAIN TUI SHELL 
press 8 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")
        if ( x == 1 ):
            import p_dkr_services
            p_dkr_services.services()
        elif ( x == 2 ):
            import p_dkr_containers
            p_dkr_containers.containers()
        elif ( x == 3 ):
            import p_dkr_images
            p_dkr_images.images()
        elif ( x == 4 ):
            import p_dkr_networks
            p_dkr_networks.networks()
        elif ( x == 5 ):
            import p_dkr_volumes
            p_dkr_volumes.volumes()
        elif ( x == 6 ):
            import p_dkr_compose
            p_dkr_compose.compose()
        elif ( x == 7 ):
            import tui
            tui.tui()
        elif ( x == 8 ):
            exit()
              
docker()

