import sys


def main_menu():
    """will print and instruct what options are available. If the user
    chooses the option, it will send them to another function. They
    will have three different choices in order to proceed on the program.
    """
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
    while answer: # Using a while loop so that it will always give a responce
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


donor = [] # List meant to store the donors in the list
amount = [] # List meant to store the amount of donations per donor
times = [] # List meant to store the number of times they have donated


def t_menu():
    """Will have three options where they can quit, obtain a list, and generate
    a thank you report. Choosing any of the options should take them to a
    different location.
    """
    print (u"")
    print (u"Please enter a name, or choose from the following: ")
    print (u"")
    print (u"list - Print a list of previous donors")
    print (u"")
    print (u"quit - Return to main menu")
    print (u"")

    answer = True
    while answer: # Using a name variable to file the input, it will
                  # add the reponse to an appropriate action
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
                donation = int(input(u"Please enter a donation amount or \n\
                 'quit': "))

                if name in donor:
                    returning = donor.index(name)
                    amount[returning] = int(amount[returning]) + int(donation)
                    times[returning] = int(times[returning]) + int(1)
                    print (u"")
                    print (u"Dear %s,\nThank you so much for your kind donation of $%s. We here at the Foundation for Obese Pets greatly appreciate it. Your money will go towards creating healthy and humble lives for dogs.\nThanks again, Ki" % (name, donation))
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


def donor_list():
    for i in range(len(donor)):
        print (u"%s" % (donor[i]))
    input(u"Press enter to continue...")
    print (u"")
    main_menu()


def report():
    """Will open the report section of the program where you can either choose
    to quit or sort through the donors
    """
    print (u"        Name         |    Total    |  #  |   Average ")
    print (u"______________________________________________________")

    for i in range(len(donor)):
        print (u"%s           |     $%s |   %s |     $%s" % (donor[i], amount[i], times[i], (int(amount[i]) / int(times[i]))))

    print (u"")
    input(u"Press enter to continue...")
    print (u"")

    # response = response.upper()
    # answer = True
    # while answer:
    #     if response == "H":
    #         max_report()
    #         answer = False
    #     elif response == "QUIT":
    #         sys.exit()
    #         answer = False
    #     else:
    #         print (u"That is not a valid response")


# def max_report():
#     """Will open the report section of the program where you can either choose
#     to quit or sort through the donors
#     """
#     donorc = donor
#     amountc = amount
#     timesc = times

#     tempd = []
#     tempa = []
#     tempt = []

#     for i in range(len(donorc)):
#         m = int(max(amountc))
#         x = int(amountc.index(m))
#         d = str(donorc[x])
#         a = int(amountc[x])
#         t = int(timesc[x])
#         tempd.append(d)
#         tempa.append(a)
#         tempt.append(t)
#         donorc.pop(d)
#         amountc.pop(a)
#         timesc.pop(t)

#     print (u"        Name         |    Total    |  #  |   Average ")
#     print (u"______________________________________________________")

#     for i in range(len(donorc)):
#         print (u"%s           |     $%s |   %s |     $%s" % (tempd[i], tempa[i], tempt[i], (int(tempa[i]) / int(tempt[i]))))

#     print (u"")

#     input(u"Press enter to continue...")
#     print (u"")
#     main_menu()


main_menu()
