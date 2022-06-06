

#import classes
from datetime import date, datetime, timedelta
import datetime
import yfinance as yahooFinance
from pandas.tseries.offsets import BDay

#Create Class for Stocks
class StockShares:
    def __init__(self, purchaseID, stock_symbol, number_shares, purchase_date):
        self.purchaseID = purchaseID
        self.stock_symbol = stock_symbol
        self.number_shares = number_shares
        self.purchase_date = purchase_date

    def yahooPurchasePrice(self):
        startDate = datetime.datetime.strptime(self.purchase_date, '%Y-%m-%d')
        endDate = startDate + timedelta(days=1)
        self.yahooStockInfo = yahooFinance.Ticker(self.stock_symbol)
        purchaseDatePrice = self.yahooStockInfo.history(start=startDate, end=endDate)
        self.purchaseDatePrice = purchaseDatePrice['Close'].iloc[-1]
        return self.purchaseDatePrice
    
    #Use Pandas BDay method to find previous business day, which will be used to view current stock price
    def businessDate(self):
        self.lastBusinessDay = (datetime.datetime.today() - BDay(1))
        lastBusinessDaytoString = self.lastBusinessDay.strftime('%Y-%m-%d')
        return lastBusinessDaytoString

    def businessDatePrice(self):
        endDate2 = self.lastBusinessDay + timedelta(days=1)
        businessDayPrice = self.yahooStockInfo.history(start=self.lastBusinessDay, end=endDate2)
        self.businessDayPrice = businessDayPrice['Close'].iloc[-1]
        return self.businessDayPrice

    #define function to calculate the total investment returns (gains or losses) as dollar amount
    def calcInvestmentReturn(self):
        #subtract current stock value and purchase value, multiply by stocks purchased
        try:
            investmentResult = (float(self.businessDayPrice) - float(self.purchaseDatePrice)) * self.number_shares
        except:
            print("String type variables provided, when expecting number")

        #format the variable with 2 floating decimal places
        investmentResult = "{0:.2f}".format(investmentResult)
    
        #return the total investment returns as dollar amount
        return investmentResult

#Create Class for Investors
class Investor:
    def __init__(self, first_name, last_name, investorID, address, phone_number):
        """Initialize Investor attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.investorID = investorID
        self.address = address
        self.phone_number = phone_number
    
    #print Investor info
    def investor_info(self):
        print(f" Investment report for {self.first_name} {self.last_name}, Investor ID = {self.investorID}")

