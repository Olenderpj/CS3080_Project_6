from Models.SaleModel import SaleModel

import re


class SalesController(SaleModel):
    FILE_REGEX = "(?P<salesFile>sales)/(?P<purchaseYear>\d{4})/(?P<purchaseMonth>[A-z]+)/(?P<salesAssociateName>[A-z]+).txt"
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    salesArray = []
    salesAssociateArray = []
    purchaseYearArray = []
    salesYears = set()

    def __int__(self):
        self.filePath = ""
        self.fileData = ""
        self.purchaseMonth = 0
        self.purchaseYear = 0
        self.salesAssociate = ''

    def createSale(self, filePath):
        sale = SaleModel()

        fileDetailsSearch = re.search(self.FILE_REGEX, filePath)
        fileLines = open(filePath, "r")
        saleLineCount = 0
        for lineSale in fileLines:
            saleLine = lineSale.split("|")

            #setattr(sale, "make", saleLine[0])
            #setattr(sale, "model", saleLine[1])
            #setattr(sale, "modelYear", int(saleLine[2]))
            #setattr(sale, "vin", saleLine[3])
            #setattr(sale, "salePrice", float(saleLine[4]))
            #setattr(sale, "purchasePrice", float(saleLine[5]))
            #setattr(sale, "profit", (float(saleLine[4]) - float(saleLine[5])))
            #setattr(sale, "purchaseYear", int(fileDetailsSearch.group("purchaseYear")))
            #setattr(sale, "purchaseMonth", fileDetailsSearch.group("purchaseMonth"))
            #setattr(sale, "salesAssociateName", fileDetailsSearch.group("salesAssociateName"))
            #
            #self.salesArray.append(sale)
            #
            #if fileDetailsSearch.group("salesAssociateName") not in self.salesAssociateArray:
            #    self.salesAssociateArray.append(fileDetailsSearch.group("salesAssociateName"))
            #self.salesAssociateArray = sorted(self.salesAssociateArray)
            #
            #if int(fileDetailsSearch.group("purchaseYear")) not in self.purchaseYearArray:
            #    self.purchaseYearArray.append(int(fileDetailsSearch.group("purchaseYear")))
            #self.purchaseYearArray = sorted(self.purchaseYearArray)


    def printArray(self):
        for sale in self.salesArray:
            print(getattr(sale, "make"), getattr(sale, "model"), getattr(sale, "vin"), getattr(sale, "salesAssociateName"))




    def getDealershipGrandTotalSalesToString(self):
        print("Total Nbr Sold {}\n"
              "Total Sales {}\n"
              "Total Profit {}\n"
              "Ave Profit Per Car {}".format(self.getDealershipTotalCarsSold(),
                                             self.getDealershipTotalSales(),
                                             self.getDealershipTotalProfit(),
                                             self.getDealershipAverageProfitPerCar()))

    def getDealershipTotalCarsSold(self):
        return len(self.salesArray)

    def getDealershipTotalSales(self):
        totalSales = 0
        for sale in self.salesArray:
            totalSales += getattr(sale, "salePrice")
        return totalSales

    def getDealershipTotalProfit(self):
        totalProfit = 0
        for sale in self.salesArray:
            totalProfit += getattr(sale, "profit")
        return totalProfit

    def getDealershipAverageProfitPerCar(self):
        return self.getDealershipTotalProfit() / self.getDealershipTotalCarsSold()

# Compile the annual Sales Information
    def getDealershipAnnualGrandTotalsToString(self):
        for year in self.purchaseYearArray:
            print("Results for {}\n"
                  "Annual Nbr Sold {}\n"
                  "Annual Sales {}\n"
                  "Annual Profit {}\n"
                  "Ave Profit Per Car {}".format(year,
                                              self.getDealershipAnnualTotalCarsSold(year),
                                              self.getDealershipAnnualTotalSales(year),
                                              self.getDealershipAnnualTotalProfit(year),
                                              self.getDealershipAnnualAverageProfitPerCar(year)
                                              ))

    def getDealershipAnnualTotalCarsSold(self, year):
        totalCarsSold = 0
        for sale in self.salesArray:
            if getattr(sale, 'purchaseYear') == year:
                totalCarsSold += 1
        return totalCarsSold

    def getDealershipAnnualTotalSales(self, year):
        annualTotalSales = 0
        for sale in self.salesArray:
            if getattr(sale, 'purchaseYear') == year:
                annualTotalSales += getattr(sale, "salePrice")
        return annualTotalSales

    def getDealershipAnnualTotalProfit(self, year):
        annualTotalProfit = 0
        for sale in self.salesArray:
            if getattr(sale, 'purchaseYear') == year:
                annualTotalProfit += getattr(sale, "profit")
        return annualTotalProfit

    def getDealershipAnnualAverageProfitPerCar(self, year):
        return self.getDealershipAnnualTotalProfit(year) / self.getDealershipAnnualTotalCarsSold(year)






# Compile the Monthly Sales Information
    def getDealershipGrandMonthlyTotalsToString(self):
        for year in self.purchaseYearArray:
            for month in self.MONTHS:
                for sale in self.salesArray:
                    if getattr(sale, "purchaseMonth") == month:
                        print("Purchase found in ", month, getattr(sale, "salePrice"))



    def getDealershipMonthlyTotalCarsSold(self, year, month):
        monthlyTotalCars = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseMonth") == month:
                print(month)

    def getDealershipMonthlyTotalSales(self, year, month):
        pass

    def getDealershipMonthlyTotalProfit(self, year, month):
        pass

    def getDealershipMonthlyAverageProfitPerCar(self, year, month):
        pass