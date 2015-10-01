import sys


def main_menu():
    print (u"Welcome")
    print (u"")
    print (u"Welcome to Mailroom Madness")
    print (u"")
    print (u"Choose from the following:")
    print (u"")
    print (u"T - Send a (T)hank You")
    print (u"")
    print (u"R - Create a (R)eport")
    print (u"")
    print (u"quit - Quit the program")
    print (u"")

    answer = True
    while answer:  # Using a while loop so that it will always give a responce

        x = str(input(u"Please choose T, R, or quit: "))
        x = x.upper()

        if x == "T":
            t_menu()
            answer = False

        elif x == "R":
            report()
            answer = False

        elif x == "QUIT":
            sys.exit()

        else:
            print (u"That is not an appropriate answer")

def t_menu():
    print (u"")
    print (u"Please enter a name, or choose from the following: ")
    print (u"")
    print (u"list - Print a list of previous donors")
    print (u"")
    print (u"quit - Return to main menu")
    print (u"")

    answer = True
    while answer:
        name = str(input(u""))
        name = name.title()

        if name == "List":
            donor_list()
            answer = False

        elif name == "Quit":
            main_menu()
            answer = False

        elif type(name) == str and len(name) > 4:

            while answer:
                print (u"")
                donation = int(input(u"Please enter a donation amount or \
                 'quit': "))

                if name in donor:
                    returning = donor.index(name)
                    amount[returning] = int(amount[returning]) + int(donation)
                    times[returning] = int(times[returning]) + int(1)
                    print (u"")
                    print (u"Dear %s,\nThank you so much for your kind donation of $%s. \
                        We here at the Foundation for Obese Pets greatly appreciate it. \
                        Your money will go towards creating healthy and humble lives for dogs.\
                        \nThanks again, Ki" % (name, donation))
                    print (u"")
                    print (u"")
                    main_menu()
                    answer = False
                elif name not in donor:
                    donor.append(name)
                    if type(donation) == int:
                        donation = str(donation)
                        print (u"")
                        print (u"Dear %s,\nThank you so much for your kind donation of $%s. We here at the Foundation for Obese Pets greatly appreciate it. Your money will go towards creating healthy and humble lives for dogs.\nThanks again, Ki" % (name, donation))
                        print (u"")
                        amount.append(donation)
                        times.append(int(1))
                        print (u"")
                        main_menu()
                        answer = False
                    elif donation == "quit":
                        t_menu()
                        answer = False
                    else:
                        print (u"Please enter a numerical value: ")
                        print (u"")
                elif name == 'quit':
                    main_menu()
                    answer = False
                else:
                    print (u"Please enter a valid command")
                    print (u"")
        else:
            print (u"Please enter a valid command")
            print (u"")
