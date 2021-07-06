class SalesController:
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    salesArray = []
    salesAssociateArray = []
    purchaseYearArray = []
    purchaseMonthArray = []

    def printSaleArray(self):
        for sale in self.salesArray:
            print(sale)

    def printSalesAssociateArray(self):
        for employee in self.salesAssociateArray:
            print(employee)

    def printPurchaseYearArray(self):
        for year in self.purchaseYearArray:
            print(year)

    def getDealershipGrandTotalSalesToString(self):
        print("{0:25s} {1:16d}\n"
              "{2:25s}${3:16,.0f}\n"
              "{4:25s}${5:16,.0f}\n"
              "{6:25s}${7:16,.0f}\n".format("Total Nbr Sold", self.getDealershipTotalCarsSold(),
                                            "Total Sales", self.getDealershipTotalSales(),
                                            "Total Profit", self.getDealershipTotalProfit(),
                                            "Ave Profit Per Car", self.getDealershipAverageProfitPerCar()))

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
            print("{0}{1}\n"
                  "{2:25s} {3:16d}\n"
                  "{4:25s}${5:16,.0f}\n"
                  "{6:25s}${7:16,.0f}\n"
                  "{8:25s}${9:16,.0f}\n".format("Results for ", year,
                                                "Annual Nbr Sold", self.getDealershipAnnualTotalCarsSold(year),
                                                "Annual Sales", self.getDealershipAnnualTotalSales(year),
                                                "Annual Profit", self.getDealershipAnnualTotalProfit(year),
                                                "Ave Profit Per Car", self.getDealershipAnnualAverageProfitPerCar(year)
                                                ))

    def getDealershipAnnualTotalCarsSold(self, year):
        annualTotalCarsSold = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year:
                annualTotalCarsSold += 1
        return annualTotalCarsSold

    def getDealershipAnnualTotalSales(self, year):
        totalAnnualSales = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year:
                totalAnnualSales += getattr(sale, "salePrice")
        return totalAnnualSales

    def getDealershipAnnualTotalProfit(self, year):
        totalAnnualProfit = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year:
                totalAnnualProfit += getattr(sale, "profit")
        return totalAnnualProfit

    def getDealershipAnnualAverageProfitPerCar(self, year):
        return self.getDealershipAnnualTotalProfit(year) / self.getDealershipAnnualTotalCarsSold(year)

# Compile the Monthly Sales Information
    def getDealershipGrandMonthlyTotalsToString(self):
        for year in self.purchaseYearArray:
            for month in self.MONTHS:
                if month in self.purchaseMonthArray:
                    print("{0} {1} {2}\n"
                          "{3:25s} {4:16d}\n"
                          "{5:25s}${6:16,.0f}\n"
                          "{7:25s}${8:16,.0f}\n"
                          "{9:25s}${10:16,.0f}\n".format("Results for", year, month,
                                                         "Monthly Nbr Sold", self.getDealershipMonthlyTotalCarsSold(year, month,),
                                                         "Monthly Sales", self.getDealershipMonthlyTotalSales(year, month,),
                                                         "Monthly Profit", self.getDealershipMonthlyTotalProfit(year, month,),
                                                         "Ave Profit Per Car", self.getDealershipMonthlyAverageProfitPerCar(year, month,)))
                else:
                    pass

    def getDealershipMonthlyTotalCarsSold(self, year, month):
        monthTotalCarsSold = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseMonth") == month and getattr(sale, "purchaseYear") == year:
                monthTotalCarsSold += 1
        return monthTotalCarsSold

    def getDealershipMonthlyTotalSales(self, year, month):
        monthTotalSales = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseMonth") == month and getattr(sale, "purchaseYear") == year:
                monthTotalSales += getattr(sale, "salePrice")
        return monthTotalSales

    def getDealershipMonthlyTotalProfit(self, year, month):
        monthTotalProfit = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseMonth") == month and getattr(sale, "purchaseYear") == year:
                monthTotalProfit += getattr(sale, "profit")
        return monthTotalProfit

    def getDealershipMonthlyAverageProfitPerCar(self, year, month):
        return self.getDealershipMonthlyTotalProfit(year, month) / self.getDealershipMonthlyTotalCarsSold(year, month)

    def getSalesAssociateGrandMonthlyTotalSales(self):
        for year in self.purchaseYearArray:
            for month in self.MONTHS:
                for salesAssociate in self.salesAssociateArray:
                    if month in self.purchaseMonthArray:
                        print("{0} {1} {2} {3}\n"
                              "{4:25s} {5:16d}\n"
                              "{6:25s}${7:16,.0f}\n"
                              "{8:25s}${9:16,.0f}\n"
                              "{10:25s}${11:16,.0f}\n".format("Results for", year, month, salesAssociate,
                                                              "Salesperson Nbr Sold",
                                                              self.getSalesAssociateTotalCarsSoldPerMonth(year, month,
                                                                                                          salesAssociate),
                                                              "Salesperson Sales",
                                                              self.getSalesAssociateTotalSalesPerMonth(year, month,
                                                                                                       salesAssociate),
                                                              "Salesperson Profit",
                                                              self.getSalesAssociateTotalProfitPerMonth(year, month,
                                                                                                        salesAssociate),
                                                              "Ave Profit Per Car",
                                                              self.getSalesAssociateAverageProfitPerCarPerMonth(year,
                                                                                                                month,
                                                                                                                salesAssociate)
                                                              ))
                    else:
                        pass

    def getSalesAssociateTotalCarsSoldPerMonth(self, year, month, salesAssociate):
        totalCarsSoldPerMonth = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year and \
                    getattr(sale, "purchaseMonth") == month and \
                    getattr(sale, "salesAssociate") == salesAssociate:
                totalCarsSoldPerMonth += 1
        return totalCarsSoldPerMonth

    def getSalesAssociateTotalSalesPerMonth(self, year, month, salesAssociate):
        totalSalesPerMonth = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year and \
                    getattr(sale, "purchaseMonth") == month and \
                    getattr(sale, "salesAssociate") == salesAssociate:
                totalSalesPerMonth += getattr(sale, "salePrice")
        return totalSalesPerMonth

    def getSalesAssociateTotalProfitPerMonth(self, year, month, salesAssociate):
        totalProfitPerMonth = 0
        for sale in self.salesArray:
            if getattr(sale, "purchaseYear") == year and \
                    getattr(sale, "purchaseMonth") == month and \
                    getattr(sale, "salesAssociate") == salesAssociate:
                totalProfitPerMonth += getattr(sale, "profit")
        return totalProfitPerMonth

    def getSalesAssociateAverageProfitPerCarPerMonth(self, year, month, salesAssociate):
        return self.getSalesAssociateTotalProfitPerMonth(year, month, salesAssociate) / \
               self.getSalesAssociateTotalCarsSoldPerMonth(year, month, salesAssociate)
