import time, os, requests, pygame, urllib
from color import Color

dic = {}


def sys():
    print(Color.BOLD + Color.RED + ' /------------------------------\\' + Color.END)
    print(
        Color.BOLD + Color.RED + ' |    ' + Color.GREEN + 'mahsol' + Color.RED + '    |    ' + Color.GREEN + 'gheymat' + Color.RED + '    |' + Color.END)
    print(Color.BOLD + Color.RED + ' |------------------------------|' + Color.END)
    for SYS113 in dic.items():
        print(Color.BOLD + Color.RED + ' |    ' + Color.BLUE + SYS113[0] + Color.RED + ' \t|    ' + Color.BLUE + SYS113[
            1] + Color.RED + '\t|' + Color.END)
    print(Color.BOLD + Color.RED + ' \\------------------------------/' + Color.END)





def all():
    print(
        Color.BOLD + Color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+- " + Color.RED + "CODED" + Color.YELLOW + " BY " + Color.BLUE + "SYS113" + Color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+- " + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.GREEN + "  0 = exit             " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.BLUE + "  1 = add item         " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.RED + "  2 = show items       " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.MAGENTA + "  3 = remove item      " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.YELLOW + "  4 = remove all items " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.WHITE + "  5 = clear screen     " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.DARK_CYAN + "  6 = save             " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.RED + "  7 = cal              " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.BLUE + "\n\t\t\t\t\t\t      [" + Color.RED + "+" + Color.BLUE + "]" + Color.BLUE + "  8 = contact me       " + Color.BLUE + "[" + Color.RED + "+" + Color.BLUE + "]" + Color.END)
    print(
        Color.BOLD + Color.GREEN + "\n -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+- " + Color.RED + "CODED" + Color.YELLOW + " BY " + Color.BLUE + "SYS113" + Color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+- \n" + Color.END)


all()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    send = input(Color.BOLD + Color.BLUE + " >" + Color.RED + ">" + Color.GREEN + "> " + Color.YELLOW)
    print(Color.END)
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if send == "0":
        close = input(Color.BOLD + Color.DARK_CYAN + "motmaeni k mikhay kharj beshi ? [y / n] : " + Color.YELLOW)
        print(Color.END)
        if close in "y":
            print(
                Color.BOLD + Color.BLUE + " b" + Color.GREEN + "y" + Color.RED + "!" + Color.YELLOW + ":D\n" + Color.END)
            time.sleep(1)
            break
        elif close in "n":
            print(Color.BOLD + Color.DARK_CYAN + "besiar khob pas nmikhay kharj beshi :D\n" + Color.END)
        else:
            print(Color.BOLD + Color.DARK_CYAN + "faghat mitoni y , n vared koni!!!\n" + Color.END)
    # =====================================================================================================================================================================
    elif send == "1":
        jens = input(Color.BOLD + Color.DARK_CYAN + " esm jenso bego : " + Color.YELLOW)
        gheymat = input(Color.BOLD + Color.DARK_CYAN + "\n gheymatesho bego : " + Color.YELLOW)
        print(Color.BOLD + Color.DARK_CYAN + "\n hale ezafash kardam be list jensa! :|\n")
        dic[jens] = gheymat
    # =====================================================================================================================================================================
    elif send == "2":
        if len(dic) == 0:
            print(Color.BOLD + Color.DARK_CYAN + " hanoz k hich jensi ezafe nakardi!\n")
        elif len(dic) != 0:
            print(Color.BOLD + Color.DARK_CYAN + " ta alan {} jens ezafe kardi!\n".format((len(dic))))
            sys()
            print(Color.END)
    # =====================================================================================================================================================================
    elif send == "3":
        remove = input(Color.BOLD + Color.DARK_CYAN + " esm jenso bego : " + Color.YELLOW)
        if remove in dic:
            del dic[remove]
            print(Color.BOLD + Color.DARK_CYAN + "\n %s ro az list jensa pakidam! :|\n" % (remove))

        elif remove not in dic:
            print(Color.BOLD + Color.DARK_CYAN + "\n %s to list jensa nis k baradare man! :|\n" % (remove))
    # =====================================================================================================================================================================
    elif send == "4":
        if len(dic) == 0:
            print(Color.BOLD + Color.DARK_CYAN + " chio pak konm vaghti hanoz hichi ezafe nakardi ? :| \n" + Color.END)
        else:
            rm = input(Color.BOLD + Color.DARK_CYAN + " kol item haro bepakam ? [y / n] : " + Color.YELLOW)
            if rm == "y":
                dic.clear()
                print(Color.BOLD + Color.DARK_CYAN + "\n kol item haye list hazf shod :|\n" + Color.END)
            elif rm == "n":
                print(Color.BOLD + Color.DARK_CYAN + "\n ok pas item haye list ro hazf nmikonam :))\n" + Color.END)
            else:
                print(Color.BOLD + Color.DARK_CYAN + "\n faghat mitoni y , n vared koni!!!\n" + Color.END)
    # =====================================================================================================================================================================
    elif send == "5":
        print(Color.BOLD + Color.DARK_CYAN + " bezar safhe ro clear konam alan miam! :|\n" + Color.END)
        time.sleep(3)
        clean_terminal()
        all()
    # =====================================================================================================================================================================
    elif send == "6":
        shop_txt = desktop_directory + "shopping-list-by-SYS113.txt"
        SYS113_shop = open(shop_txt, "w")
        SYS113_shop.write(' /------------------------------\\\n')
        SYS113_shop.write(' |    mahsol    |     gheymat   |')
        SYS113_shop.write('\n |------------------------------|\n')
        for k, v in dic.items():
            SYS113_shop.write(' |    {} \t|    {}\t|\n'.format(str(k), str(v)))
        SYS113_shop.write(' \\------------------------------/\n')
        SYS113_shop.close()

        print(Color.BOLD + Color.DARK_CYAN + 'save shod list mahsolat dar %sshopping-list-by-SYS113.txt !\n' % (
            desktop_directory) + Color.END)
    # =====================================================================================================================================================================
    elif send == "7":
        calc1 = int(input(Color.BOLD + Color.BLUE + "\n add aval : " + Color.YELLOW))
        operator = input(Color.BOLD + Color.GREEN + "\n - , + , * : " + Color.YELLOW)
        calc2 = int(input(Color.BOLD + Color.RED + "\n add dovom : " + Color.YELLOW))

        if operator == "-":
            opera = calc1 - calc2
            print(Color.BOLD + Color.MAGENTA + "\n hasele %d - %d mishavad : %d ! :D\n" % (
                calc1, calc2, opera) + Color.END)

        elif operator == "+":
            opera = calc1 + calc2
            print(Color.BOLD + Color.MAGENTA + "\n hasele %d + %d mishavad : %d ! :D\n" % (
                calc1, calc2, opera) + Color.END)

        elif operator == "*":
            opera = calc1 * calc2
            print(Color.BOLD + Color.MAGENTA + "\n hasele %d * %d mishavad : %d ! :D\n" % (
                calc1, calc2, opera) + Color.END)

        else:
            print(Color.BOLD + Color.RED + "\nfaghat mitavanid - , + , * vared konid!\n")
    # =====================================================================================================================================================================
    elif send == "8":
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '-=' * 16 + '-' + Color.END)
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
        print(
            Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '| ' + Color.RED + '     telegram' + Color.YELLOW + ' : ' + Color.BLUE + '@SYS113' + Color.GREEN + '\t      |' + Color.END)
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
        print(
            Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '|  ' + Color.RED + 'github' + Color.YELLOW + ' : ' + Color.BLUE + 'github.com/SYS113/' + Color.GREEN + '  |' + Color.END)
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
        print(
            Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '| ' + Color.RED + 'mail' + Color.YELLOW + ' : ' + Color.BLUE + 'SYS113@protonmail.com' + Color.GREEN + '  |' + Color.END)
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
        print(Color.BOLD + Color.GREEN + '\t\t\t\t\t\t      ' + '-=' * 16 + '-\n' + Color.END)
    # =====================================================================================================================================================================
    else:
        print(Color.END + Color.BOLD + Color.DARK_CYAN + " faghat mitoni 1...7 ro vared koni! :D\n")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
