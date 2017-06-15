def change_finder(given, price):
    change = given - price
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    cent = 0.01
    print ('Tender change of:')
    if (change >= 1): 
        print ('$', int(change))
    fractional_change = round(change - int(change), 2) 
    if fractional_change != 0:
        if fractional_change >= quarter:
            print(int(fractional_change/quarter), 'Quarters')
            fractional_change = fractional_change - (int(fractional_change/quarter))*quarter
        if fractional_change >= dime:
            print(int(fractional_change/dime), 'Dimes')
            fractional_change = fractional_change - (int(fractional_change/dime))*dime
        if fractional_change >= nickel:
            print(int(fractional_change/nickel), 'Nickels')
            fractional_change = fractional_change - (int(fractional_change/nickel))*nickel
        if fractional_change >= cent:
            print(int(round(fractional_change, 2)*100), 'Cents')

x1, x2 = input('Enter amount given, price as ssv : ').split()
change_finder(float(x1), float(x2))
