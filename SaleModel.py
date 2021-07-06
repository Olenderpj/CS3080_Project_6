class SaleModel:
    def __init__(self, make, model, modelYear, vinNumber, salePrice, purchasePrice, purchaseMonth,
                 purchaseYear, salesAssociate):
        self.make = make
        self.model = model
        self.modelYear = modelYear
        self.vinNumber = vinNumber
        self.salePrice = salePrice
        self.purchasePrice = purchasePrice
        self.purchaseMonth = purchaseMonth
        self.purchaseYear = purchaseYear
        self.salesAssociate = salesAssociate
        self.profit = (salePrice - purchasePrice)

    def __str__(self):
        return "\nMake: {}" \
               "\nModel: {}" \
               "\nModel Year: {}" \
               "\nVin: {}" \
               "\nSale Price: {}" \
               "\nPurchase Price: {}" \
               "\nTotal Profit: {:.2f}" \
               "\nPurchase Month: {}" \
               "\nPurchase Year: {}" \
               "\nSalesAssociate: {}".format(self.make,
                                             self.model,
                                             self.modelYear,
                                             self.vinNumber,
                                             self.salePrice,
                                             self.purchasePrice,
                                             self.profit,
                                             self.purchaseMonth,
                                             self.purchaseYear,
                                             self.salesAssociate)

