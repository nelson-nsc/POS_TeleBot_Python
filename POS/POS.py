import numpy as np
import pandas as pd
from tabulate import tabulate
import requests

item = []
qty = []
sub = []


def def_main():
    while True:
        print("*" * 34 + "Main Menu" + "*" * 34+ "\n\n" 
              "(1) Breakfast" 
              "\t(2) Lunch" 
              "\t(3) Dinner"
              "\t(4) Snacks"
              "\t(5) Drinks\n\n\n" +
              "\t"* 3 + "(P) Pay"
              "\t(E) Quit\n" + 
              "*" * 74)
        
        input_1 = str(input('Order: ').upper())
        if (len(input_1) == 1):
            if (input_1 == '1'):
                print("\n" * 2)
                def_breakfast()
                break
            elif (input_1 == '2'):
                print("\n" * 2)
                def_lunch()
                break
            elif (input_1 == '3'):
                print("\n" * 2)
                def_dinner()
                break
            elif (input_1 == '4'):
                print("\n" * 2)
                def_snacks()
                break
            elif (input_1 == '5'):
                print("\n" * 2)
                def_drinks()
                break
            elif (input_1 == 'P'):
                print("\n" * 2)
                def_payment()
                break
            elif (input_1 == 'E'):
                print("\n" * 2 +
                      "*"*33 +"Thank you" + "*"*33)
                break
                

            else:
                 print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        else:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_breakfast():
    while True:
        breakfast = pd.read_excel("breakfast.xlsx")
        breakfast.index += 1
        print(tabulate(breakfast,headers=['Items','$'], tablefmt='fancy_grid'))
        print('\n (Q) Main Menu  \t (P) Pay')

        input_1 = input('Order: ').upper()
        if (input_1 == 'Q'):
            print("\n" * 4)
            def_main()
            break
        if (input_1 == 'P'):
            print("\n" * 4)
            def_payment()
            break
        if (input_1 == 'E'):
            print("*"*34 + "Thank you" + "*"*34)
            break
        try:
            int(input_1)
            if (int(input_1) > 0 and int(input_1) <= len(list(breakfast.main))+1):
                try:
                    print(("\n" + "_" * 72 + "\n" + str(list(breakfast.main)[int(input_1)-1])))

                except:
                    pass
                input_2 = input('Qty: ')
                if int(input_2) > 0:
                    item.append(list(breakfast.main)[int(input_1)-1])
                    qty.append(int(input_2))
                    sub.append(list(breakfast.price)[int(input_1)-1] * int(input_2))

                    print('Order Placed')
                    def_breakfast()
                    break
                else:
                    print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        except:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_lunch():
    while True:
        lunch = pd.read_excel("lunch.xlsx")
        lunch.index += 1
        print(tabulate(lunch,headers=['Items','$'], tablefmt='fancy_grid'))
        print('\n (Q) Main Menu  \t (P) Pay')

        input_1 = input('Order: ').upper()
        if (input_1 == 'Q'):
            print("\n" * 4)
            def_main()
            break
        if (input_1 == 'P'):
            print("\n" * 4)
            def_payment()
            break
        try:
            int(input_1)
            if (int(input_1) > 0 and int(input_1) <= len(list(lunch.main))+1):
                try:
                    print(("\n" + "_" * 72 + "\n" + str(list(lunch.main)[int(input_1)-1])))

                except:
                    pass
                input_2 = input('Qty: ')
                if int(input_2) > 0:
                    item.append(list(lunch.main)[int(input_1)-1])
                    qty.append(int(input_2))
                    sub.append(list(lunch.price)[int(input_1)-1] * int(input_2))
                    print('Order Placed')
                    def_lunch()
                    break
                else:
                    print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        except:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_dinner():
    while True:
        dinner = pd.read_excel("dinner.xlsx")
        dinner.index += 1
        print(tabulate(dinner,headers=['Items','$'], tablefmt='fancy_grid'))
        print('\n (Q) Main Menu  \t (P) Pay')

        input_1 = input('Order: ').upper()
        if (input_1 == 'Q'):
            print("\n" * 4)
            def_main()
            break
        if (input_1 == 'P'):
            print("\n" * 4)
            def_payment()
            break
        try:
            int(input_1)
            if (int(input_1) > 0 and int(input_1) <= len(list(dinner.main))+1):
                try:
                    print(("\n" + "_" * 72 + "\n" + str(list(dinner.main)[int(input_1)-1])))

                except:
                    pass
                input_2 = input('Qty: ')
                if int(input_2) > 0:
                    item.append(list(dinner.main)[int(input_1)-1])
                    qty.append(int(input_2))
                    sub.append(list(dinner.price)[int(input_1)-1] * int(input_2))

                    print('Order Placed')
                    def_dinner()
                    break
                else:
                    print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        except:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_snacks():
    while True:
        snacks = pd.read_excel("snacks.xlsx")
        snacks.index += 1
        print(tabulate(snacks,headers=['Items','$'], tablefmt='fancy_grid'))
        print('\n (Q) Main Menu  \t (P) Pay')

        input_1 = input('Order: ').upper()
        if (input_1 == 'Q'):
            print("\n" * 4)
            def_main()
            break
        if (input_1 == 'P'):
            print("\n" * 4)
            def_payment()
            break
        try:
            int(input_1)
            if (int(input_1) > 0 and int(input_1) <= len(list(snacks.main))+1):
                try:
                    print(("\n" + "_" * 72 + "\n" + str(list(snacks.main)[int(input_1)-1])))

                except:
                    pass
                input_2 = input('Qty: ')
                if int(input_2) > 0:
                    item.append(list(snacks.main)[int(input_1)-1])
                    qty.append(int(input_2))
                    sub.append(list(snacks.price)[int(input_1)-1] * int(input_2))

                    print('Order Placed')
                    def_snacks()
                    break
                else:
                    print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        except:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_drinks():
    while True:
        drinks = pd.read_excel("drinks.xlsx")
        drinks.index += 1
        print(tabulate(drinks,headers=['Items','$'], tablefmt='fancy_grid'))
        print('\n (Q) Main Menu  \t (P) Pay')

        input_1 = input('Order: ').upper()
        if (input_1 == 'Q'):
            print("\n" * 4)
            def_main()
            break
        if (input_1 == 'P'):
            print("\n" * 4)
            def_payment()
            break
        try:
            int(input_1)
            if (int(input_1) > 0 and int(input_1) <= len(list(drinks.main))+1):
                try:
                    print(("\n" + "_" * 72 + "\n" + str(list(drinks.main)[int(input_1)-1])))

                except:
                    pass
                input_2 = input('Qty: ')
                if int(input_2) > 0:
                    item.append(list(drinks.main)[int(input_1)-1])
                    qty.append(int(input_2))
                    sub.append(list(drinks.price)[int(input_1)-1] * int(input_2))

                    print('Order Placed')
                    def_drinks()
                    break
                else:
                    print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")
        except:
            print("\n" * 2 + "Input Error (" + str(input_1) + "). Please try again")

def def_payment():
    while True:
        if (item != []):
            print("*"*34 + "Pay" + "*"*34)
            df = pd.DataFrame({'item':pd.Series(item),
                    'qty': pd.Series(qty),
                    'price': pd.Series(sub)})  
            total = {'item':'', 'qty':'  Total:', 'price':df['price'].sum()}
            df = df.append(total, ignore_index=True)
            df.index += 1 
            print(tabulate(df, headers=['Items','Qty','$'],tablefmt='fancy_grid',showindex=False))
            # msg = 'https://api.telegram.org/bot"your_telebot_API"/sendmessage?chat_id="your_chat_id"="{}"'.format(tabulate(df, headers=['Items','Qty','$'],tablefmt='simple',showindex=False));
            # requests.get(msg)
            break
        else:
            print("\n" + "="*32 + "Please place an order" + "="*32 + "\n\n")
            def_main()
            break

def_main()