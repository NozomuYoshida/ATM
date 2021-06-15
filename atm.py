print('Welcome to Yoshida Bank ATM')
correct_pin = 1234
restart = 'Y'
chances = 3
balance = 1000
while chances >= 0:
    pin = int(input('Please enter your 4 digits pin: '))
    if pin == 1234:
        print('You entered pin correctly')
        print('Please press 1 for your balance')
        print('Please press 2 for to make a withdrawl')
        print('Please press 3 to pay in')
        print('Please press 4 to return card\n')
        while restart not in ('n', 'N', 'no', 'No'):
            print('You entered pin correctly')
            print('Please press 1 for your balance')
            print('Please press 2 for to make a withdrawl')
            print('Please press 3 to pay in')
            print('Please press 4 to return card')
            option = int(input('What whold you like to choose?: '))
            if option == 1:
                print('Your balance is $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'no', 'No'):
                    print('Thank you')
                    break
            elif option == 2:
                option2 = 'y'
            withdrawl = float(input('How much would you like to withdrawl? 10, 20, 40, 60, 100 or other enter 1: '))
            withdrawl_list = [10, 20, 40, 60, 80, 100]
            if withdrawl in withdrawl_list:
                balance -= withdrawl
                print('\nYour balance is now $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'no', 'No'):
                    print('Thank you')
                    break
            elif option == 3:
                pay_in = int(input('How much would you like to pay in? '))
                balance += pay_in
                print('\nYour balance is now $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'no', 'No'):
                    print('Thank you')
                    break
            elif option == 4:
                print('Please wait whilst your card is returned')
