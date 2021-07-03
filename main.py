import os
import re

# Numerical printing format for the number of cars sold
nbrSoldFormat = '{0:25s} {1:16d}'

# Numerical printing format for the currency values
currencyFormat = '{0:25s}${1:16,.2f}'

# Months in order
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


# Prints the results using the required formatting
def printResults(results):
    print(nbrSoldFormat.format(results[0], results[1]))
    for i in range(2, 7, 2):
        print(currencyFormat.format(results[i], float(results[i + 1])))
    print()


# Print the results for the entire data set
def printTotalValues(carData):
    nbrSold = 0
    sales = 0
    profit = 0
    profitPerCar = 0
    year = 0
    month = ''
    salesperson = ''

    # TODO: Calculate totals here

    # TODO: Print the following results for the entire data set
    printResults(['Total Nbr Sold', nbrSold, 'Total Sales', sales,
                  'Total Profit', profit, 'Ave Profit Per Car', profitPerCar])


# Print the results for each year
def printAnnualValues(salesData):
    nbrSold = 0
    sales = 0
    profit = 0
    profitPerCar = 0
    year = 0
    month = ''
    salesperson = ''

    # TODO: Calculate totals here

    # TODO: Print the following results for each year
    print("Results for", year)
    printResults(['Annual Nbr Sold', nbrSold, 'Annual Sales', sales,
                  'Annual Profit', profit, 'Ave Profit Per Car', profitPerCar])


# Print the results for each month of each year
def printMonthlyValues(salesData):
    nbrSold = 0
    sales = 0
    profit = 0
    profitPerCar = 0
    year = 0
    month = ''
    salesperson = ''

    # TODO: Calculate totals here

    # TODO: Print the following results for each month
    print("Results for", year, month)
    printResults(['Monthly Nbr Sold', nbrSold, 'Monthly Sales', sales,
                  'Monthly Profit', profit, 'Ave Profit Per Car', profitPerCar])


# Print the results for each salesperson for each month for each year
def printSalespersonValues(salesData):
    nbrSold = 0
    sales = 0
    profit = 0
    profitPerCar = 0
    year = 0
    month = ''
    salesperson = ''

    # TODO: Calculate totals here

    # TODO: Print the following results for each salesperson
    print("Results for", year, month, salesperson)
    printResults(['Salesperson Nbr Sold', nbrSold, 'Salesperson Sales', sales,
                  'Salesperson Profit', profit, 'Ave Profit Per Car', profitPerCar])


# Main application
carData = {}

choice = 1

# Print the menu and accept the user's choice
while choice != 5:
    print('******************************************')
    print('1 - Display Total Sales Info')
    print('2 - Display Annual Sales Info')
    print('3 - Display Monthly Sales Info')
    print('4 - Display Salesperson Sales Info')
    print('5 - Quit')
    print('******************************************')
    choice = int(input())

    if choice == 1:
        printTotalValues(carData)
    elif choice == 2:
        printAnnualValues(carData)
    elif choice == 3:
        printMonthlyValues(carData)
    elif choice == 4:
        printSalespersonValues(carData)
    elif choice == 5:
        print('Thank you!')
    else:
        print('Please make a valid selection')
