def linux():
    import os
    x = 0
    while (x != 7) :
        os.system("clear")
        os.system("tput setaf 1")
        os.system("tput bold")
        print('''
\t##       ####  ##      ##  ##     ##  ##     ##
\t##        ##   ###     ##  ##     ##   ##   ##  
\t##        ##   ####    ##  ##     ##    ## ##    
\t##        ##   ## ##   ##  ##     ##     ###    
\t##        ##   ##  ##  ##  ##     ##     ###     
\t##        ##   ##   ## ##  ##     ##    ## ##  
\t##        ##   ##    ####   ##   ##    ##   ## 
\t#######  ####  ##     ###    #####    ##     ##
\t________________________________________________
\t________________________________________________
\t\*\                                           /*/
\t \*\    _________________________________    /*/
\t  \*\  /*/                             \*\  /*/
\t   \*\ \*\  WELCOME TO LINUX TUI SHELL /*/ /*/
\t    \*\ --------------------------------  /*/
\t     \*\#################################/*/
\n\n''')
        os.system("tput rmul")
        os.system("tput setaf 1")
        print('''
Press 1 : For Linux Services
Press 2 : To Accesses Linux Locally
Press 3 : To Accesses Linux Remotely
Press 4 : To Know About Networks
Press 5 : To Linux Storage
Press 6 : To Configure Yum
Press 7 : To SWITCH BACK TO MAIN TUI SHELL 
press 8 : To EXIT\n''')
        os.system("tput setaf 1")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 15")
        if ( x == 1 ):
            import p_linux_services
            p_linux_services.services()
        elif ( x == 7 ):
            import tui
            tui.tui()
        elif ( x == 8 ):
            exit()
        





linux()
