

#import classes
from ctypes import alignment
from tkinter import *

#import classes from file
from w10_classes_scoggin import *

#Instantiate investor objects
bob_smith = Investor('Bob','Smith','001', '123 Main St, Denver, CO, 80001', '303-485-9540')
#sally_jones = Investor('Sally','Jones','002', '456 Front St, Denver, CO, 80002', '720-835-1722')

#Reference external file for Bob's stocks
bobs_stocks_file = 'c:\Temp\w10_Bobs_Stocks.csv'

#Read external file for Bob's stocks
#Error handling for reading the stocks file
try:
    with open(bobs_stocks_file) as file_object:
        header = (file_object.readline()).rstrip()
        contents = file_object.readlines()
except FileNotFoundError:
    print(f"Sorry, the file {bobs_stocks_file} does not exist.")
    exit()

#Create index variables for the columns for Bob's stocks
header_split = header.split(',')
symbol_index = header_split.index('SYMBOL')
shares_index = header_split.index('NO_SHARES')
purchase_date_index = header_split.index('PURCHASE_DATE')

#Create list of Bob's stocks
bobs_stocks = []
stock_index = 1

#Loop through the external file lines and instantiate objects for Bob's stocks
for line in contents:
  line_split = line.split(',')
  stock_purchase = StockShares(stock_index, line_split[symbol_index], int(line_split[shares_index]), (line_split[purchase_date_index]).rstrip())
  bobs_stocks.append(stock_purchase)
  stock_index = stock_index + 1

#Define GUI window with tkinter
window = Tk()
window.title("Welcome to Investment, Inc")
window.geometry('800x600')

#Define a login message for the financial consultant
welcome_lbl = Label(window, text="**You are logged in as Joe Banker**", font=12, pady=10, padx=150)
welcome_lbl.grid(columnspan=7, row=0)

#Define a prompt for the financial consultant
info_lbl = Label(window, text="Select the investor profile to load")
info_lbl.grid(columnspan=2, row=1)

#Define an informational message
choice_lbl = Label(window, text="[pending investor choice]")
choice_lbl.grid(columnspan=7, row=2)

#Define method for button actions
def click_btn1():
    choice_lbl.configure(text="Bob Smith was selected", font=12)
    output_column = 0
    output_row = 4
    #loop Bob's Stocks print report 
    tableHeaders = ["Stock Symbol","# of Shares","Purchase Date","Purchase Price","Latest Date","Latest Price","Gains/Loss"]
    tableHeaderCount = 0
    #Print the headers in window
    for tableHeader in tableHeaders:
        Label(window,text=tableHeader).grid(column=tableHeaderCount, row=3, sticky=W)
        tableHeaderCount = tableHeaderCount + 1
    #Loop through all of Bob's stocks
    for stock in bobs_stocks:
        output_column = 0

        #Call yahooPurchasePrice() method to obtain the price of the stock at time of purchase
        purchase_price = float("{0:.2f}".format(stock.yahooPurchasePrice()))
        
        #Call businessDate() method to get the previous Business day which will contain stock data
        previousBusinessDay = stock.businessDate()
        
        #Call method to get previous Business day closing price
        recentPrice = stock.businessDatePrice()
        recentPrice = float("{0:.2f}".format(recentPrice))
        
        #Call method to get total gains/loss
        gains_loss = stock.calcInvestmentReturn()

        #Define information about the stock
        stock_info = stock.stock_symbol, stock.number_shares, stock.purchase_date, purchase_price, previousBusinessDay, recentPrice, gains_loss
        
        #Loop through the stock information to print to window
        for info in stock_info:
            Label(window, text=info).grid(column=output_column, row=output_row, sticky=W)
            output_column = output_column + 1
        
        #Move to the next row to print the next stock
        output_row = output_row + 1

'''
def click_btn2():
    choice_lbl.configure(text="Sally Jones was selected")
'''

#Define button for investor Bob Smith
investor_btn1 = Button(window, text="Bob Smith", command=click_btn1)
investor_btn1.grid(column=2, row=1)

'''
#Define button for invester Sally Jones
investor_btn2 = Button(window, text="Sally Jones", command=click_btn2)
investor_btn2.grid(column=3, row=1)
'''


window.mainloop()
