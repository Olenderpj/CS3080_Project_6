from Models.SaleModel import SaleModel

import re


class SalesController(SaleModel):
    fileRegex = "(?P<salesFile>sales)/(?P<purchaseYear>\d{4})/(?P<purchaseMonth>[A-z]+)/(?P<salesAssociateName>[A-z]+).txt"

    filePath = ""
    fileData = ""
    #salesArray = []
    purchaseMonth = 0
    purchaseYear = 0
    salesAssociate = ''
    salesAssociates = set()
    salesYears = set()

    def __int__(self, filePath):
        self.filePath = filePath
        self.fileData = open(filePath, "r")
        self.createSale(self.fileData)
        self.setSalesAssociate()
        self.setPurchaseYear()
        self.salesArray = []

    def createSale(self, fileData):

        for saleData in fileData:
            saleData.split('|')

            sale = SaleModel()

            setattr(sale, "make", saleData[0])
            setattr(sale, "model", saleData[1])
            setattr(sale, "modelYear", saleData[2])
            setattr(sale, "vin", saleData[3])
            setattr(sale, "salePrice", saleData[4])
            setattr(sale, "purchasePrice", saleData[5])
            setattr(sale, "purchaseYear", )
            setattr(sale, "salesAssociate", )


            self.salesArray.append(sale)

    def setSalesAssociate(self):
        if self.filePath is not None:
            fileSearch = re.search(self.fileRegex, self.filePath)
            self.salesAssociate = fileSearch.group('salesAssociateName')

    def setPurchaseMonth(self):
        if self.filePath is not None:
            fileSearch = re.search(self.fileRegex, self.filePath)
            self.purchaseMonth = fileSearch.group('purchaseMonth')

    def setPurchaseYear(self):
        if self.filePath is not None:
            fileSearch = re.search(self.fileRegex, self.filePath)
            self.purchaseYear = fileSearch.group('purchaseYear')

    def getSalesArray(self):
        return self.salesArray

    # Compile the total Sales Information
    def dealershipGrandTotalsToString(self):

        for sale in self.salesArray:
            getattr(sale, "purchasePrice")




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
