import os
import re
from SalesController import SalesController
from SaleModel import SaleModel

FILE_REGEX = "(?P<salesFile>sales)/(?P<purchaseYear>\d{4})/(?P<purchaseMonth>[A-z]+)/(?P<salesAssociateName>[A-z]+).txt"

def sortYearArray(yearArray):
    return sorted(yearArray)

salesController = SalesController()
for root, dirs, files in os.walk("/Users/pjolender/School/Python Programming - CS3080/sales", topdown=True):
    for name in files:
        if name != ".DS_Store": # this is a catch for mac users. MacOs automaticlly adds this hidden file to every folder
            filePath = os.path.join(root, name)
            fileConventionsData = re.search(FILE_REGEX, filePath)

            monthSalesData = open(filePath, "r")

            for saleLine in monthSalesData:
                singleSale = saleLine.split("|")

                if fileConventionsData.group("salesAssociateName") not in salesController.salesAssociateArray:
                    salesController.salesAssociateArray.append(str(fileConventionsData.group("salesAssociateName")))

                if fileConventionsData.group("purchaseMonth") not in salesController.purchaseMonthArray:
                    salesController.purchaseMonthArray.append(str(fileConventionsData.group("purchaseMonth")))

                if int(fileConventionsData.group("purchaseYear")) not in salesController.purchaseYearArray:
                    salesController.purchaseYearArray.append(int(fileConventionsData.group("purchaseYear")))

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

salesController.purchaseYearArray = sortYearArray(salesController.purchaseYearArray)
salesController.salesAssociateArray = sortYearArray(salesController.salesAssociateArray)

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

# TODO: add choice selections
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
