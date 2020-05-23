def tui():
    import os
    x = 0
    while (x != 3) :
        os.system("clear")
        os.system("tput setaf 1")
        os.system("tput bold")
        print('''
\t\t ########  ##     ##  ####
\t\t    ##     ##     ##   ##
\t\t    ##     ##     ##   ##
\t\t    ##     ##     ##   ##
\t\t    ##     ##     ##   ##
\t\t    ##     ##     ##   ##
\t\t    ##      ##   ##    ##
\t\t    ##       #####    ####
\t\t _________________________
\t\t  SERVICES AVAILABLE FOR 
\t\t _________________________
\t\t \  #  \  ________________
\t\t  \  #  \ #              #                 
\t\t   \  #  \#  DOCKER TUI  #  
\t\t    \  #  ----------------
\t\t     \  ##################
\t\t      \  _________________
\t\t       \ #               #
\t\t        \#   LINUX TUI   #  
\t\t         -----------------   
\n''')
        os.system("tput rmul")
        os.system("tput setaf 1")
        print('''
Press 1 : TO SWITCH INTO DOCKER TUI
Press 2 : TO SWITCH INTO LINUX TUI
press 3 : TO EXIT \n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")
        if ( x == 1 ):
            import p_docker_menu
            p_docker_menu.docker()
        elif ( x == 2 ):
            import Linux
            Linux.linux()
        elif ( x == 3 ):
            exit()
    else:
        print("invalid option plz press either 1 or 2")


tui()
