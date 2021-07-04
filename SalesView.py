from SalesController import SalesController

class SalesView(SalesController):
    def __init__(self):
        self.salesController = SalesController
        self.salesArray = self.salesController.getSalesArray()

# Compile the total Sales Information
    def dealershipGrandTotalsToString(self):

        for sale in self.salesArray:

        pass

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