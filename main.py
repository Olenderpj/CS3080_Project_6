import os
from SalesController import SalesController
sc = SalesController()
for root, dirs, files in os.walk("/Users/pjolender/School/Python Programming - CS3080/sales", topdown=True):


    for name in files:
        if name != ".DS_Store":
            filePath = os.path.join(root, name)


            sc.createSale(filePath)







#print(sc.purchaseYearArray)
#sc.getDealershipGrandTotalSalesToString()
#print("*********************************************")
#sc.getDealershipAnnualGrandTotalsToString()

#sc.getDealershipGrandMonthlyTotalsToString()




