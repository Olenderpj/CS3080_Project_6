""" @Author: PJ Olender
    DueDate: 7/9/2021
    Class: CS 3080 - Summer 2021
    Project: 6 - File I/O
    Description: Read from a specified directory and gather different summary information from all of the files
    based on the user's request. I took an object oriented approach to this project so that every file would only be
    read one time and an object would be created for each car sale. The sales controller then has the ability to
    parse all of these objects and get the required information for the user's output """


import os
import re
from SalesController import SalesController
from SaleModel import SaleModel

FILE_REGEX = "(?P<salesFile>sales)/(?P<purchaseYear>\d{4})/(?P<purchaseMonth>[A-z]+)/(?P<salesAssociateName>[A-z ]+).txt"


# used for sorting arrays that contain years or names in ascending or alphabetical order
def sortArray(array):
    return sorted(array)


salesController = SalesController()

''' To search a specific file, replace "sales" with the path of the directory that your test data is in. '''

# Iterate through all directories and create objects of all of the car data in each text file.
for root, dirs, files in os.walk("sales", topdown=True):
    for name in files:
        if name != ".DS_Store":  # Catch for macUsers, MacOS puts this hidden file in every directory.
            filePath = os.path.join(root, name)
            fileConventionsData = re.search(FILE_REGEX, filePath)

            monthSalesData = open(filePath, "r")

            # Iterate through each line in the text file
            for saleLine in monthSalesData:
                singleSale = saleLine.split("|")

                # Store the names of all of the sales Associates in an array
                if fileConventionsData.group("salesAssociateName") not in salesController.salesAssociateArray:
                    salesController.salesAssociateArray.append(str(fileConventionsData.group("salesAssociateName")))

                # Store the purchase month of all of the sales in an array
                if fileConventionsData.group("purchaseMonth") not in salesController.purchaseMonthArray:
                    salesController.purchaseMonthArray.append(str(fileConventionsData.group("purchaseMonth")))

                # Store the purchase year of all of the sales in an array
                if int(fileConventionsData.group("purchaseYear")) not in salesController.purchaseYearArray:
                    salesController.purchaseYearArray.append(int(fileConventionsData.group("purchaseYear")))

                # Create a sales model object and append it to the sales array in the sales controller
                salesController.salesArray.append(SaleModel(make=str(singleSale[0]),
                                                            model=str(singleSale[1]),
                                                            modelYear=int(singleSale[2]),
                                                            vinNumber=str(singleSale[3]),
                                                            salePrice=float(singleSale[4]),
                                                            purchasePrice=float(singleSale[5].strip()),
                                                            purchaseMonth=str(
                                                                fileConventionsData.group("purchaseMonth")),
                                                            purchaseYear=int(fileConventionsData.group("purchaseYear")),
                                                            salesAssociate=str(
                                                                fileConventionsData.group("salesAssociateName"))
                                                            ))

# sort these arrays before any more actions are taken
salesController.purchaseYearArray = sortArray(salesController.purchaseYearArray)
salesController.salesAssociateArray = sortArray(salesController.salesAssociateArray)

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
        salesController.getDealershipGrandTotalSalesToString()
    elif choice == 2:
        salesController.getDealershipAnnualGrandTotalsToString()
    elif choice == 3:
        salesController.getDealershipGrandMonthlyTotalsToString()
    elif choice == 4:
        salesController.getSalesAssociateGrandMonthlyTotalSales()
    elif choice == 5:
        print('Thank you!')
    else:
        print('Please make a valid selection')
