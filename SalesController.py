from Models.SaleModel import SaleModel

import re


class SalesController(SaleModel):
    FILE_REGEX = "(?P<salesFile>sales)/(?P<purchaseYear>\d{4})/(?P<purchaseMonth>[A-z]+)/(?P<salesAssociateName>[A-z]+).txt"
    salesArray = []
    def __int__(self):
        self.filePath = ""
        self.fileData = ""
        self.purchaseMonth = 0
        self.purchaseYear = 0
        self.salesAssociate = ''
        self.salesAssociates = set()
        self.salesYears = set()


    def createSale(self, filePath):
        sale = SaleModel()


        fileLines = open(filePath, "r")

        for lineSale in fileLines:
            saleLine = lineSale.split("|")
            setattr(sale, "make", saleLine[0])
            setattr(sale, "model", saleLine[1])
            setattr(sale, "modelYear", saleLine[2])
            setattr(sale, "vin", saleLine[3])
            setattr(sale, "salePrice", saleLine[4])
            setattr(sale, "purchasePrice", saleLine[5])

            self.salesArray.append(sale)


 #   def setSalesAssociate(self):
 #       if self.filePath is not None:
 #           fileSearch = re.search(self.fileRegex, self.filePath)
 #           self.salesAssociate = fileSearch.group('salesAssociateName')
 #
 #   def setPurchaseMonth(self):
 #       if self.filePath is not None:
 #           fileSearch = re.search(self.fileRegex, self.filePath)
 #           self.purchaseMonth = fileSearch.group("purchaseMonth")
 #
 #   def setPurchaseYear(self):
 #       if self.filePath is not None:
 #           fileSearch = re.search(self.fileRegex, self.filePath)
 #           self.purchaseYear = fileSearch.group('purchaseYear')
 #
 #   def getSalesArray(self):
 #       return self.salesArray
 #
 #   # Compile the total Sales Information
 #   def dealershipGrandTotalsToString(self):
 #
 #       for sale in self.salesArray:
 #           rv = getattr(sale, "purchasePrice")
 #           print(rv)
 #










    def getDealershipTotalCarsSold(self):
        pass

    def getDealershipTotalSales(self):
        pass

    def getDealershipTotalProfit(self):
        pass

    def getDealershipAverageProfitPerCar(self):
        pass

    # Compile the annual Sales Information
    def dealershipAnnualGrandTotalsToString(self):
        pass

    def getDealershipAnnualTotalCarsSold(self):
        pass

    def getDealershipAnnualTotalSales(self):
        pass

    def getDealershipAnnualTotalProfit(self):
        pass

    def getDealershipAnnualAverageProfitPerCar(self):
        pass

    # Compile the Monthly Sales Information

    def dealershipGrandMonthlyTotalsToString(self):
        pass

    def getDealershipMonthlyCarsSold(self):
        pass

    def getDealershipMonthlyTotalSales(self):
        pass

    def getDealershipMonthlyTotalProfit(self):
        pass

    def getDealershipMonthlyAverageProfitPerCar(self):
        pass

    # Compile the SalesPerson Sales Information by month

    def dealershipGrandTotalByEmployee(self):
        pass

    def dealershipEmployeeTotalCarsSold(self):
        pass

    def dealershipEmployeeTotalSales(self):
        pass

    def dealershipEmployeeTotalProfit(self):
        pass

    def dealershipEmployeeAverageProfitPerCar(self):
        pass
